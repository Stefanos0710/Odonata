"""
Verwendung der neuen Systemkamera OV5647 oder IMX219 des Raspberry Pi 
Wenn Sie das neueste Bookworm-System verwenden, müssen Sie sudo nano/boot/firmware/config.txt konfigurieren 
Nachdem Sie sudo nano/boot/firmware/config.txt eingegeben haben, suchen Sie nach: 
 
Schritt 1: Aussage „camera-auto-detect=1“ ändern Sie in „camera_outo_detect=0“. 
Wenn Sie es für die Raspberry Pi 4B- und Zero-Serie verwenden, ignorieren Sie den ersten Schritt der Modifikation.Probieren Sie es direkt mit dem Befehl libcamera jpeg - o test aus.jpg zum Testen.Wenn es nicht funktioniert, fahren Sie mit dem zweiten Schritt fort. 
 
Schritt 2: Fügen Sie am Ende der Datei: dtoverlay=ov5647 oder dtoverlay=imx219 hinzu s
Achtung: Wählen Sie ov5647, imx219 oder imx708 basierend auf Ihrem eigenen Kamerachip 
Wenn es nicht verwendet werden kann, können Sie dtoverlay=imx219, cam0 hinzufügen, um es auszuprobieren 
Strg+o Eingabe, dann Strg+x Beenden und zum Neustart „Reboot“ eingeben

Farbe:Rot
Vielen Dank, dass der Shop die notwendigen Informationen für die Einrichtung bereitstellt. In der /boot/firmware/config.txt habe ich Folgendes geändert: „Kamera-Auto-Erkennung=0“ und am Ende der Datei habe ich hinzugefügt dtoverlay=imx219, cam0 


Waht I want to happen get video stream from teh camera,
then get the april tag and its position
"""

import argparse
import cv2 as cv
from pupil_apriltags import Detector
import numpy as np
import threading
import time

class Camera:
    def __init__(self):
        # camera parameters: [fx, fy, cx, cy]
        self.camera_parameters = [460, 460, 320, 240]

        # is the camera running?
        self.running = False

        # the current data from the camera
        self.current_data = []

    def setup(self):
        # defining the arguments of the parser
        ap = argparse.ArgumentParser()
        ap.add_argument("--width", type=int, default=640, help="the width of the video stream")
        ap.add_argument("--height", type=int, default=480, help="the height of the video stream")
        ap.add_argument("--families", type=str, default="tagCustom48h12", help="the family of the april tag to detect")
        ap.add_argument("--nthreads", type=int, default=3, help="the number of threads to use for the detection (cpu cores)") # resberry pi zero 2 W has 4 cores, so using 3 of them for detection
        ap.add_argument("--quad_decimate", type=float, default=1.5, help="decimate input image by this factor")

        # pars the arguments
        self.args = ap.parse_args()
        
        # setup the camera
        self.cap = cv.VideoCapture(0)
        self.cap.set(cv.CAP_PROP_FRAME_WIDTH, self.args.width)
        self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, self.args.height)

        # setup the april tag detector
        self.at_detector = Detector(
            families=self.args.families, 
            nthreads=self.args.nthreads, 
            quad_decimate=self.args.quad_decimate
        )


    def get_yaw(R):
        """
        calculates the yaw angle from the rotation matrix R, which is part of the pose estimation of
        
        :param R: the rotation matrix from the pose estimation of the april tag, which is a 3x3 numpy array
        
        """
        sy = np.sqrt(R[0,0] * R[0,0] + R[1,0] * R[1,0])
        singular = sy < 1e-6
        
        if not singular:
            z = np.arctan2(R[1,0], R[0,0])
        else:
            z = 0
        return np.degrees(z)
    
    def start(self):
        # start the thread for the video stream and april tag detection
        self.running = True
        thread = threading.Thread(target=self.measure_data)
        thread.start()

    def stop(self):
        # stop the thread for the video stream and april tag detection
        self.running = False
        self.cap.release()

    def get_data(self):        
        """
        returns a list of 4 values: [x_pixel, y_pixel, z_meter, yaw], where:
        x_pixel: the x pixel position of the tag in the image
        y_pixel: the y pixel position of the tag in the image
        z_meter: the distance to the tag in meters
        yaw: the yaw angle of the tag in degrees
        """
        return self.current_data


    def measure_data(self):
        while self.running:
            # read a frame from the camera
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            tags = self.at_detector.detect(
                image,
                estimate_tag_pose=True,
                camera_params=self.camera_parameters,
                tag_size=0.046
                )

            # print the detected tags and their positions
            for tag in tags:
                # tag.center ist ein Array wie [x, y]
                x_pixel = tag.center[0]
                y_pixel = tag.center[1]
                
                # tag.pose_t ist ein 3x1 Array (Translation/Position)
                z_meter = tag.pose_t[2][0]
                yaw = self.get_yaw(tag.pose_R)
                
                print(f"Pixel-middle: X={x_pixel:.1f}, Y={y_pixel:.1f}")
                print(f"Distance: Z={z_meter:.2f} m, Yaw={yaw:.2f} Grad")

            time.sleep(0.1) # wait 100ms before the next frame

            self.current_data = [
                x_pixel, # x pixel position of the tag in the image
                y_pixel, # y pixel position of the tag in the image
                z_meter, # distance to the tag in meters
                yaw # yaw angle of the tag in degrees   
            ]

