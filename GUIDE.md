## How to build Odonata (Step-by-Step)

If you want to rebuild this drone without any modifications, you can follow these next steps. If you want to modify the drone, you can follow along the guide, you just have to adjust it to your changes:

### 1. Getting the parts

1. Download the whole repository on your computer by running these commands in your terminal to download the firmware, CAD, and PCB:

   ```bash
   git clone https://github.com/Stefanos0710/Odonata.git
   cd Odonata
   ```

   After that, you will have cloned the entire project onto your computer.

2. Next, you have to print out the 3D parts, and therefore you have 2 options, based on whether you have a 3D printer or not:
   1. If you have a 3D printer: upload the stl files from `/CAD/f3d_stl` into your slicer software. You have to print every file separately. So for the propguards you need 4, the motor arms you need 4, the base you need 1, the wall you need 1, the cover you need 1, and you need the camera holder. For the landing station, you need the catcher and the AprilTag holder.
   2. If you don't have a 3D printer, you can use a company like PCBWay, JLCPCB, or any other 3D printing service. There you have to upload the exact same files I mentioned previously and order them.
   3. Overall for the filament, if you can choose which one you can use, I would assume to use TPU for the propguards and print the rest with PETG for the best stability. For the color, if you like the style of the drone, it should be light/lime green and purple/blue.

3. Next, you should order the PCB. Therefore you need the gerber files which you find at `PCB/gerbers` as a `gerbers.zip` file. This file you can upload on a service like PCBWay, JLCPCB, or any other of your choice. Make sure to select 4 layers, and for the color it doesn't matter, but in this case I used the typical green one. Otherwise, I use the default options, so FR-4 as material.

4. Next, we need to get/buy the rest of the parts. A list with all parts you can find further down in the README, or in the `BOM.csv` file. There is the cost of the parts, the links, name, and description. INFO: the shipping cost is calculated for ordering to Bavaria, Germany, so it might change for you. But the rough price without shipping is 222,71€.

### 2. Setting up the Raspberry Pi Zero 2 W

After you got all the parts, we can start building the drone. And therefore we will start setting up the Raspberry Pi Zero 2 W:

1. Firstly, you need to download the Raspberry Pi Imager software on your computer, so that you can install the OS on the Raspberry Pi. First open this site https://www.raspberrypi.com/software/ and download it for your OS (Windows/macOS/Linux).
2. After downloading, you need to attach a micro SD card with at least 16GB to the computer, so that you can flash the OS and attach it later into the Raspberry Pi.
3. Then you choose the Raspberry Pi OS Lite, without the desktop, so that we don't waste resource power on that.
4. During that procedure, you will need to add the name (I assume to use "odonata" as the name), the WLAN (this must match the WLAN that you are connected to with your computer and later your server), and very important is to activate SSH, and lastly, you have to add a username and a password.
5. Then you detach the micro SD from your computer and attach it into the Raspberry Pi and connect it with a USB for power.
6. After waiting for about 5 min so that the OS can boot, you can type (for Windows):

   ```bash
   ssh yourusername@odonata.local
   ```

   And so you should be connected to the Raspberry Pi.
7. Now we update the system by typing in:

   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

8. After that, type in `sudo raspi-config` and activate the camera, the SPI, and the I2C.
9. After that, we have to install Python and Git. It's mostly already installed, but to update it's good:

   ```bash
   sudo apt install python3 python3-pip python3-venv git -y
   python3 --version
   pip3 --version
   git --version
   ```

   If you see no error, then everything is fine and installed.
10. And lastly, you have to copy the drone folder from firmware to the Raspberry Pi, and you can do it with this:

   ```bash
   git clone --depth 1 https://github.com/Stefanos0710/Odonata.git temp_repo
   mv temp_repo/firmware/drone ./drone
   mv temp_repo/firmware/requirements.txt ./
   rm -rf temp_repo

   cd drone
   pip install -r requirements.txt
   ```

11. Then, to activate the communication with the FC, you have to also add in `sudo raspi-config` under Interface Options -> Serial Port:
    - Login shell over serial? → No
    - Enable serial hardware? → Yes
    And then reboot.

### 3. Flight Controller Configuration

1. After we set up the Pi, we have to configure the FC (Flight Controller) so that we can use MAVLink on it. Therefore, you have to firstly install Mission Planner and then connect the FC with a USB cable to the PC.
2. Then you have to choose the COM port and the baud number that should be 115200, and then click Connect.
3. Then open the menu under Initial Setup and then Install Firmware, then select ArduCopter.
4. During that process, the firmware is installed and the FC is rebooted multiple times.
5. After that, you should read a text called ArduCopter Vx.x.x, and if Mission Planner connected again, then all is perfect.
6. Then we have to configure the parameters in Mission Planner. Therefore you go under Config to Full Parameter List and fill this out:
   - `SERIAL2_PROTOCOL = 2`
   - `SERIAL2_BAUD = 115`
7. This activates MAVLink2 which allows the communication with the Pi, and the baud number is the standard for drones with MAVLink. And after clicking on "Write Params", you are finished and you set everything up.

### 4. PCB Soldering

1. Now you have to solder all the SMD parts on the drone PCB. There isn't really a step-by-step for this, try to orientate yourself from the PCB renders, the schematics, and PCB layer 1.

### 5. Drone Assembly

After everything is soldered, you need to assemble the hardware parts:

1. Place the PCB on the base that was 3D printed, then add the placeholders (spacers) from the FC. Put the FC on it and screw it on with the M2 12mm screws.
2. Attach the Raspberry Pi to the male pins.
3. For the power, I firstly recommend to use a laboratory power supply so that you don't destroy your battery if something is wrong.
4. To connect everything, you need to connect the TX and RX cables from J2 with the RX and TX cables from the FC, and the rest of the parts are pretty easy to connect. Orientate yourself here again from the schematics and the PCB design.
5. Lastly run that command to install mavproxy:

   ```bash
   python3 mavproxy.py --master=/dev/serial0 --baudrate 115200 --aircraft MyCopter
   ```

6. And now we can attach the rest of the parts. Firstly, you have to insert the heat inserts with a soldering iron into the parts. Therefore you have to add them to the motor arms and the walls.
7. After that, you have to place the arms in the holding parts from the base and screw them with the M2 6mm screws into the base.
8. Next, you place the prop guards at the place where the motors go and screw them again with 6mm screws.
9. And now you have to lengthen the cables from the motors and place them in the cable canal from the arm into the inside of the drone, and solder the cables onto the FC pads for the motors.
10. Next, you have to attach the camera holder to the servo and also place the camera module into it, and place it in the front of the base. Make sure that the camera cable goes above the servo, connect the servo cable with its JST-GH cable, and attach it onto the PCB.
11. Next, solder the JST-GH cables to the ToF sensors and also add them to the PCB.
12. After all of this, you can place the walls and screw them on the base.
13. Next, place all the ToF sensors in their positions and make sure to press them in so that they hold their place. And now you are ready for the first test.

### 6. Server Setup

1. Go to your server computer or on the computer where you are currently working, and run these commands:

   ```bash
   git clone --depth 1 https://github.com/Stefanos0710/Odonata.git temp_repo
   mv temp_repo/firmware/server ./server
   mv temp_repo/firmware/requirements.txt ./
   rm -rf temp_repo

   cd server
   pip install -r requirements.txt

   fastapi dev
   ```

2. Then open `127.0.0.1:8000` and you will see the drone cockpit.
3. There you have to firstly add the IP by pressing "Connect Drone" or wait until the IP shows up, and connect the drone.
4. Then start the drone and test every motor and every component independently. If everything works fine, you are ready for the final step!

### 7. Final Touches

1. Now you can attach the propellers to the drone, and make sure they sit very tight.
2. After also attaching the battery and the on/off switch at the cover, you now have to print this paper out ([april_tag_print.pdf](images/april_tag_print.pdf)) and add it to the AprilTag holder.
3. Attach the AprilTag holder under the catcher, place the drone on the catcher, and let it start via the cockpit by pressing "Start Flight" and see the magic happen.
