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

# defining the arguments of the parser
ap = argparse.ArgumentParser()
ap.add_argument("--width", type=int, default=640, help="the width of the video stream")
ap.add_argument("--height", type=int, default=480, help="the height of the video stream")
ap.add_argument("--families", type=str, default="tagCustom48h12", help="the family of the april tag to detect")
ap.add_argument("--nthreads", type=int, default=3, help="the number of threads to use for the detection (cpu cores)") # resberry pi zero 2 W has 4 cores, so using 3 of them for detection
ap.add_argument("--quad_decimate", type=float, default=1.5, help="decimate input image by this factor")

# pars the arguments
args = ap.parse_args()

# setup the camera
cap = cv.VideoCapture(1)
cap.set(cv.CAP_PROP_FRAME_WIDTH, args.width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, args.height)

# setup the april tag detector
at_detector = Detector(
    families=args.families, 
    nthreads=args.nthreads, 
    quad_decimate=args.quad_decimate
)

try:
    while True:
        # read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        tags = at_detector.detect(image)

        # print the detected tags and their positions
        for tag in tags:
            print(f"Detected tag with id {tag.tag_id} at position {tag.center}")

except KeyboardInterrupt:
    print("breaking the loop... T-T")
    cap.release()
