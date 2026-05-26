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

import cv2
import pupil_apriltags