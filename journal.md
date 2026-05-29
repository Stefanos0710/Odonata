# Odonata — Journal Export

- Exported at: 2026-05-29T18:32:10Z
- Project ID: 130
- Entries: 32

## Entry 1
- ID: 3456
- Author: Stefanos
- Created At: 2026-04-22T21:31:00Z

### Content

### 22. April: Find out the basics and plan the fundamental 

Before I started, I only had a rough idea. I wanted to build a drone that can mostly fly on its own and also has a docking station for charging and keeping it safe. I also already had in mind that I want to use a Raspberry Pi as a kind of brain for internet control and later video stream, but I didn’t really know yet how I would integrate that into the drone.


![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzEwMCwicHVyIjoiYmxvYl9pZCJ9fQ==--d0b911524392dd0f7d7b83a617b7069ff6b509c3/image.png)

Since I never built a drone before and had almost no experience in this field, I started from zero and learned (by doing):

1. what a drone actually is  
2. how a drone works (lift, motors, control)  
3. what parts are needed and what they do  

This was important because otherwise every part I would pick later would feel random and would probably be wrong

After I saw that there are multiple drone layouts, like X, H and +, I chose the X design because:
- it is the most stable in flight  
- it is mostly used for indoor flying  
- it is easier to build for beginners  

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzEwOSwicHVyIjoiYmxvYl9pZCJ9fQ==--2c2c25496903fea0f741cddd9952164137f54380/image.png)

Then I learned that every drone is controlled by a flight controller (FC).

At first I thought they were almost the same and that I could just buy one and it would be fine, but there are HUGE differences.

There are a lot of different FCs and every choice depends on something else: frame size, sensors, voltage, UARTs, software, etc.

This is where I really got stuck in a loop:

I would pick a part, then realize another part doesn’t match, then change that part, and suddenly the first one doesn’t fit anymore. T-T

So it became like:
- choose FC, changes motor choice  
- choose motor, changes battery  
- choose battery, changes weight  
- weight, changes whole frame idea  

And then I had to go back again.

It felt like building one decision always breaks another decision...

Another HUGE problem was that:
- many parts were not available in local shops  
- some parts were completely sold out  
- China shops were (only sometimes) cheaper but had long delivery times (3 weeks, which was too long...)

But after a long time of searching I finally found some pretty good components for my drone.

At the same time I also shaped the system idea more clearly: the Raspberry Pi should not control the motors directly, but instead be as a higher level controller for things like internet connection, remote control and later video streaming, while the flight controller handles the real-time flight control. That split made the whole architecture much clearer.

At first I wanted an F4 flight controller with Betaflight because it is:
- powerful enough  
- widely used  

But then I ran into the same problem as before:
- many were too expensive  
- many were out of stock  
- some had long shipping delays  

So after a lot of switching and comparing, I decided on the:

**DarwinFPV F411 15A AIO**

because it was available, fit perfectly in the budget and supports all other parts that I chose.

The next problem I ran into was the weight / thrust ratio

At first my setup gave only ~2:1 thrust ratio.

That is theoretically enough to fly, but extremely slow and unstable.

So I decided to upgrade motors from 1104 to 1204 size

So I lastly decided on the **Happymodel 1204 5000KV**, because it has very good thrust, is compatible with the other components and is pretty cheap with fast delivery.

To combine everything, I adjusted the full system with the right battery:
> Tattu R-Line 850mAh 3S 150C

and for the props:
> Gemfan Hurricane 3016 (3 inch)

After checking again if everything was compatible with each other, I had my final components :

- FC: DarwinFPV F411 15A AIO  
- Motor: Happymodel 1204 5000KV  
- Battery: 3S 850mAh  
- Props: Gemfan 3016  

Estimated thrust:
~280g per motor × 4 = ~1120g total

This gives around a 3.7:1 thrust ratio, which is actually solid for this drone!

Pretty happy with the progress and learned very much!


### Recording Links

- https://lookout.hackclub.com/api/media/b6f6d021-7fbb-4be1-8b2f-5608a45261e2/video.mp4
- https://lookout.hackclub.com/api/media/3165a61b-8592-4b2d-a718-28b1a420eed7/video.mp4

## Entry 2
- ID: 3587
- Author: Stefanos
- Created At: 2026-04-23T18:17:14Z

### Content

### 23. April: Finished searching the main parts!

First of all, I searched for a raspberry pi. I decided to use the Raspberry Pi Zero 2 W because it is smaller than a Pi 4, but still powerful enough, has enough pins for sensors, FC, cameras etc., and is not too expensive.

I checked the official resellers for the Pi Zero 2 W and unfortunately only FUNK 24 Aachen had it in stock. All other shops were sold out, so I ended up with a price of about 23€, which is still good.

Next, I wanted to add cameras for automatic landing with April-tags, and another one for controlling the drone over the internet (video stream) or later object detection. But I wasn’t sure if it would be possible to connect 2 cameras to the Raspberry Pi Zero 2 W and if that would be too expensive

So I searched a bit and found out that there are devices from ArduCam that can connect 2 or more cameras and connect them into one camera interface (Raspberry Pi Multi Camera Adapter)

Then I searched for the cameras. One thing that shocked me was the price (around 20–30€ per camera), but luckily AliExpress helped :)

But then I had another decision/problem:
there were multiple camera angle options (77° / 130° / 160° / 200°)

After checking some examples and thinking about the recognision of the tags, I came up with this:
- the camera for landing needs a wide enough view to detect AprilTags even if the drone is not perfectly aligned  
- 77° is too narrow,
- 160° / 200° are too large, which makes picture curve -> detection harder  
- 130° is the sweet spot!

So I decided on 130° cameras

Then I moved to the connection problem. I wanted 2 cameras, but the Raspberry Pi Zero 2 W only has one CSI camera input.

So again I searched and found the ArduCam Multi Camera Adapter (V2.2), which allows multiple cameras on one Pi. But it was quite expensive (around 40–50€), and even on AliExpress it was still expensive and not really worth it for my budget.

At this point I thought about another solution: instead of using 2 cameras, I could just use one camera and move it with a servo motor (tilt up/down). 
That would be lighter and cheaper:

- Servo weight: ~6g  
- Camera weight: ~10g  
- Servo cost: basically 0€ (I already have one)

So I decided to go with the servo solution instead of the multi-camera adapter, even though 2 cameras would be nicer. But it just didn’t make sense...

Here is an example of how the servo camera setup would work:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzM0NCwicHVyIjoiYmxvYl9pZCJ9fQ==--f5d7e253afa1ffd3d386f5563af85f847840ab7b/image.png)

Additionally, I wanted to use distance sensors for more stable, controlled and safe flight (especially for landing without crashing).

The idea was to measure distance on the left/right side and front/ground side.

Here is a small drawing of the sensor placement:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzM0NywicHVyIjoiYmxvYl9pZCJ9fQ==--f9620f7ea662e208a43aa1a23f15cf27de18c085/image.png)

While researching, I learned that there are a few common sensor types:
- ultrasonic distance sensors  
- ToF (Time of Flight) sensors  
- IR distance sensors  
- (and a few others)

After comparing pros and cons, I decided to use the VL53L0X ToF sensor, because:
- it is accurate for short distances (under ~2 meters)  
- it is small and light
- it is cheap (~3€ on AliExpress)  

Now I have found all the main parts I need for the project, including good prices, availability, and shipping time.

Happy with this sessions progress. I learned a lot again. Next session will probably be PCB design!!! Yippee!!


### Recording Links

- https://lookout.hackclub.com/api/media/5040556b-7866-4573-afae-0b8f1bfa49fb/video.mp4

## Entry 3
- ID: 3825
- Author: Stefanos
- Created At: 2026-04-25T05:54:44Z

### Content

# 24 April: Drawing the first design of the drone!

Originally, I wanted to start today with the PCB, but when I thought about how everything should be connected and fit, the center of weight, and optimal design for the drone, that’s why I decided to first make a sketch and design the drone from a top view and side view (in 1:2 scale), for brainstorming positioning and finding the right distances and angles for the parts placement. Here’s how I started:

## 1. Wheelbase 

I decided to use a 180 mm wheelbase because, after looking it up for 3" propellers, the sweet spot is about 2x–2.5x the propeller diameter.

> 76 mm (propeller diameter) * 2.5 = 190  
> 76 mm * 2 = 152  
> → about 180 mm is best for me and indoor use because I have a bit more room, also for the Raspberry Pi, FC, etc. (which will become a problem soon T-T).

So the nearest motor-to-motor distance is about 127 mm, calculated by dividing the 180 mm wheelbase by √2:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Nzc5MCwicHVyIjoiYmxvYl9pZCJ9fQ==--61130a232f89b02ab9ec932839b370459180f175/image.png)


## 2. Propeller protection + base design

In the next step I drew the propellers with protection, which are 4 mm thick and will be 10 mm tall, so that it will hopefully be much safer, and because it’ll fly autonomously. For the base (the most important part for me ):

> For the main base (the red part), I chose an octagon shape because it fits the design perfectly. I drew lines that go straight through the center of each motor, and the corners of the red base sit exactly on these lines. By using an octagon instead of a simple square, I can cut away the extra corners to save weight. It also gives me flat sides to attach the arms easily and creates a clean space in the middle for all my electronics.

Additionally, I also added small squares on the ends of the octagon: the camera and servo (left) and (right) the battery.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Nzc1MiwicHVyIjoiYmxvYl9pZCJ9fQ==--a98659d76b9e0a7297b9b35f5d8abcddf0571064/image.png)


## 3. Motor arm design

Then I also planned the arms for the motors:  
I made them come in a 90-degree angle from the straight base that connects normally like every other drone, but I also added a second arm for every motor that is at a 45-degree angle from the first arm, for more stability and less vibrations during flight. I also tried to pay attention not to design the arms too thick, so that the air can flow nicely and without problems through the propellers, so I kept them at a thickness of 7 mm.


## 4. PCB and electronics layout

Now I was mostly finished with the main design and then I thought about the PCB.  
Here is a basic schematic of all the parts assembly and the position of the PCB:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Nzc2OSwicHVyIjoiYmxvYl9pZCJ9fQ==--54ede857f1e0ad684a1433958d6d935ace0fa3d2/image.png)


But then I encountered a problem: there wasn’t enough place for the FC and Raspberry Pi. But after googling and thinking, I came up with the idea that I could stack the Raspberry Pi over the FC to save space.  
But even after that I would have problems with routing, because the Raspberry Pi (which I would connect over GPIO pins (male/female)) would block most of the PCB because it would go from one side to the other, so I decided to only use GPIO pins for the signals I really need.

Position of the Raspberry Pi and FC:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Nzc3OCwicHVyIjoiYmxvYl9pZCJ9fQ==--d654944cb72eb7dfcd578dc41a4f821a801bbb06/image.png)

I also thought about the problem that the battery would be too far back and the center of gravity would be off, but then I had the idea that the battery could be mounted upright (vertical), and that should minimize the problem.

---
Overall happy with the progress! Tomorrow I’ll really start with the 3D design / PCB and I’m excited to continue (I had problems connecting Lapse with Fallout so if I didn’t find another solution, check here: https://lapse.hackclub.com/timelapse/HnbnaB-3Kzma ~1.3h)



### Recording Links

- https://public.lapse-hackclub.link/timelapses/HnbnaB-3Kzma/timelapse-HnbnaB-3Kzma.mp4

## Entry 4
- ID: 3943
- Author: Stefanos
- Created At: 2026-04-25T22:08:52Z

### Content

### 25. April: CAD the motor base and arm!

Firstly, I started with the 2D design and “copying” the motor sizes, holes, etc. At first I struggled finding the diameter tool and also understanding the motor sketch, especially with the 4× M2 holes. That confused me because I thought the 1.5 mm was the diameter of the holes, but it was actually the radius.

Then I made another mistake: I thought the 1.5 mm radius was for the holes, but it was actually for the outline. For the hole size I had to search it up on the internet, which was M2 (about 1.5 mm diameter). I also had to pay attention to a recess in the middle of the motor (the side where it will be mounted), so I had to cut out a small hole with a diameter of about 4 mm.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODA4MSwicHVyIjoiYmxvYl9pZCJ9fQ==--0c6449d27580e3daa657de19a8402f00c6ab9bba/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODA5NywicHVyIjoiYmxvYl9pZCJ9fQ==--2ea9790a8c5b482dd000ee9ad1710e15cfb1464b/image.png)

After that I continued with the 3D design. I extruded the platform to 5 mm for stability, but not more, to save weight.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODA5NiwicHVyIjoiYmxvYl9pZCJ9fQ==--85f37c947c112a5ff8775582d3068661d5202d06/image.png)  


I also thought about making the plate a bit bigger than the motor itself, so I added about 5 mm around it for more stability and so the arms can connect better to the motor platform.

Then I remembered that I should include about 0.2 mm tolerance, so I updated the design for that.

After that I checked the screw length. The holes have a depth of about 1.5 mm and the plate is 5 mm thick (total ~6.5 mm). The screw head also takes about 1.5 mm (hidden in the platform), so I calculated:

7.5 mm − 1.5 mm = 6 mm

So I will use M2 6 mm screws, which luckily exist.

At the end I extruded all the holes, so it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODA5NCwicHVyIjoiYmxvYl9pZCJ9fQ==--e1cb0f644d6c1a8274d305643845cb9ff0d1e1a7/image.png)



After that I started with the “2 arms per motor” design.

First, I checked where the cable from the motor comes out, because the cable should go through the 45° angled arm that goes directly to the center.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODExNywicHVyIjoiYmxvYl9pZCJ9fQ==--1bddfdd7cba55e7ce23894f2beda133a59b4bb04/image.png)  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODEzOSwicHVyIjoiYmxvYl9pZCJ9fQ==--5f5dade929c4c615920db31184dc19fcdfac55e0/image.png)

I made the arm go exactly 44 mm from the center of the motor, based on my previous planning. For the width I used 6 mm, and for the height I used the same as the base: 5 mm.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODEyOSwicHVyIjoiYmxvYl9pZCJ9fQ==--4c78bf4ab4dfb4fb1292fad37fbc2fddb7b50e99/image.png)

Then I also rounded the edges between the arm and the motor base:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODEzMCwicHVyIjoiYmxvYl9pZCJ9fQ==--ee09a19a4962984db12dc5f5bac7567b63c4247b/image.png)

Happy with today’s progress. I learned a lot in CAD design and I like the arm design for the motor. Tomorrow I will continue with the cable channel in the arm and then the main base of the drone!!! Pretty excited!


### Recording Links

- https://lookout.hackclub.com/api/media/5584e5fc-6911-425c-9b65-d1d5dc9f0595/video.mp4

## Entry 5
- ID: 4111
- Author: Stefanos
- Created At: 2026-04-26T20:03:32Z

### Content

### 26. April: Finished the Motor-Arm CAD design!

1. I started with the cable canal, but I wasn’t sure if I should use a lid or just leave it open. I decided to first leave it open and not design a lid because it would be pretty complicated, increase the weight, and make debugging or modifying the drone harder.

While starting to design the tunnel in the 2D sketch, I noticed a mistake: I saw that the ends of the arms were rounded by mistake.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODQ3MCwicHVyIjoiYmxvYl9pZCJ9fQ==--39e335943898dcb37d735fb0ab5fceb4ba71d701/image.png)

So I added corners for better next design.

After fixing this, I draw the tunnel which is 3 mm width, because the cable is 2.4 mm.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODQ3MywicHVyIjoiYmxvYl9pZCJ9fQ==--9d413b8d45fb5211bc8f37ed2986b1fc1b06b93d/image.png)

Then I extruded the canal by 3 mm so that the cables can perfectly fit:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODQ3NCwicHVyIjoiYmxvYl9pZCJ9fQ==--f9a76b5a974444e4486e2ac19d258f840cc6bbe7/image.png)

But it didn’t look clean, so for better cable handling I rounded the corners / sides:
- the back line I added a 3 mm fillet  
- the side parts I added a 1 mm fillet  

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODQ4MSwicHVyIjoiYmxvYl9pZCJ9fQ==--953655c6c6bebcbdc2c063956340742db3740be1/image.png)

Then I continued: I started designing a small part that extrudes from the end of the 2 arms so that I can put an M2 heat insert in it and later screw it onto the base for more stability. But because I didn’t really have a clear plan where everything should be / look like and how all sizes should fit, I first started with a design of how the arm connects to the base and how the PCB and other parts should be positioned.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODQ5OCwicHVyIjoiYmxvYl9pZCJ9fQ==--21c1f46e897b8465fecc61edb33f8f57621f6cc3/image.png)

After I had a plan, I decided to make the height exactly 3 mm because the insert is the same size. I also made it 10 mm long for more stability so the screw has enough space, but also the cable can go into the base without any problems.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODUwMywicHVyIjoiYmxvYl9pZCJ9fQ==--42dfddfb945b23f5b96c399435bc59e0d9eebf0c/image.png)

After that I also rounded the corners (2 mm) and extruded the hole for the insert, then I copied and redesigned this part on the other arm.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODUwNywicHVyIjoiYmxvYl9pZCJ9fQ==--3d839a2459d969edc481180c3942e0faa2fa290a/image.png)

Lastly, I also added an extra height of 0.1 mm to the whole arm to compensate for small errors, for example from the insert.

This session today was nice and I managed to finish the arms! I am happy with the design! In the next session I will start with the base (hopefully also today!).

### Recording Links

- https://lookout.hackclub.com/api/media/eadea0cb-7eba-4867-9160-201d867545b6/video.mp4

## Entry 6
- ID: 4655
- Author: Stefanos
- Created At: 2026-04-30T18:22:41Z

### Content

### 30. April: Designing the base of the drone!!

Firstly, I created the base file where the main base of the drone should be. But before I started designing, I wasn’t sure if the center of gravity would actually be in the middle. So I wanted to calculate everything first to avoid any problems later.

The problem was that I didn’t really know how to do that, but after a bit of googling I found this:
https://www.wikihow.com/Calculate-Center-of-Gravity

For calculating the center of gravity you need the position of each part relative to the center and its weight. So I found all values by measuring distances and looking up the weights online:

- Raspberry Pi: +1 cm, 10 g → +10  
- Camera: +10 cm, 15 g (took a while to figure out)  
- Servo: 7.7 cm, 9 g  
- Battery: 76 g, -5 cm  
- FC is directly in the middle → no effect  
- all other parts are symmetric (motors etc.)

> Calc:
> 10 + 150 + 69.3 − 380 = −150.7  
> Total weight:
> 10 + 9 + 76 + 15 = 110 g  
> Center of gravity:
> −150.7 / 110 = −1.37 ≈ −1.4 cm  

This is not good because the center of gravity should be at 0 cm. So I had a few ideas:
- add weight at the front (about 9 cm in the front)  
- increase infill in the front area to add “hidden weight”  

After that I started designing:

I first made a circle based on my previous drawing. The distance was 2.3 mm, and I scaled it up 4x (to become a diameter and for the sscale 1:2), so I got 9.2 mm diameter.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTcxMCwicHVyIjoiYmxvYl9pZCJ9fQ==--069e8304c8790e6dddd5356f1535ae05086e07ad/image.png)

Then I draw the edges where the arms connect to the base at 45° and 4.6 cm length.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTcxMiwicHVyIjoiYmxvYl9pZCJ9fQ==--ed65c56e21807a7c7998ebd1298aadf47cdfb956/image.png)

But then I wasn’t sure how big the connection area for the arms should be. So I measured the arm width (6 mm) and multiplied it by 3, which returned 18 mm. From the center that meant about 6 cm spacing on both sides.

While doing that I realized I had made a mistake with some values:
- I accidentally wrote 4.8 mm instead of the correct value 48mm...

So I had to fix and update all doistances… T-T

After fixing everything, I added the final connection lines for the arms:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTcxMywicHVyIjoiYmxvYl9pZCJ9fQ==--033fafb16065a030658b1f0ffefedb59d5e25395/image.png)

And finally connected everything:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTcxNSwicHVyIjoiYmxvYl9pZCJ9fQ==--ce964e7430426b5aaec7bb2b0e6de417ed999204/image.png)

Afterwards, I started designing the rectangle where the camera and servo will sit, and where the second arm connects with the base. For that I first checked my drawing to get the correct scale. In my sketch it was 30 mm, so in real size (1:2 scale) it became 60 mm, and the width was 17 mm → 34 mm in real.

So I created a rectangle with those values:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTcxOCwicHVyIjoiYmxvYl9pZCJ9fQ==--09e2d92a364f32a0490c11fb5fbc31739705a830/image.png)

But then I got confused because the rectangle didn’t match my original sketch. I kept checking the measurements, but it still didn’t fit . At that point, I realized that my sketch wasn’t very accurate.

So I decided to first draw the motor positions and propeller radius to understand where everything actually is positioned and where everything should be:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTcyNywicHVyIjoiYmxvYl9pZCJ9fQ==--096d307463033de8a99b56f030d17b101b547def/image.png)

Then I saw that the diagonal arm connections actually matched the larger circles in my sketch, and the smaller ones were the propellers. But the vertical arms didn’t fit properly, so I had to fix the layout.

So I updated the box size to 39 mm and kept the length at 60 mm:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTcyOSwicHVyIjoiYmxvYl9pZCJ9fQ==--ea23d5197451006cdd9cf7a1789ec1d91004a39d/image.png)

After that I started designing the bottom box for the battery. To help fine tuning the center of gravity later, I increased the length by 5mm (from 40mm to 45mm) so I can shift the battery if needed.

So the design looked like this:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTczMCwicHVyIjoiYmxvYl9pZCJ9fQ==--24978d242b7fca1e7bfbefa98cd1aa1445e63393/image.png)

Then I exited the sketch and wanted to extrude the base, but I wasn’t sure how thick it should be. Then I remembered I still need the mounting system for the motor arms, so I checked the screw sizes.

At first I couldn’t find any of that in my notes, so I had to google again and realized there are SOOO MANY different screw types. But after searching, I decided to use ultra thin low head M2×6 mm screws because they allow a thinner and cleaner design.

The screw head is about 0.8 mm thick, so I added 1 mm sothat the screw head can hid in that. Together with the 3 mm arm and base structure, everything fits:
3 + 3 + 1 − 1 = 6 => M2×6 mm screws

Next I cut the screw holes. I first marked the center lines, extruded 5 mm into the base, and created 2 mm holes. Because of 3D printing error, I increased them to 2.2 mm.

At first I thought the holes didn’t match the arm holes, but then I realized:
one is for the heat insert, the other one is for the screw,  so everything was actually fine...

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTczNSwicHVyIjoiYmxvYl9pZCJ9fQ==--72746da0adb68062e0262014c039bb8939092da1/image.png)

Lastly, I extruded the holes and added an extra hole so the screw heads can sit inside the base:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTczNiwicHVyIjoiYmxvYl9pZCJ9fQ==--e0f395c367271dd708437bb610a45e91f8ef45bd/image.png)

Happy with the progress today. I solved a lot of problems and started the base design. Next journal will be about the attachment mechanism for the arms and base.


### Recording Links

- https://lookout.hackclub.com/api/media/5f0e2622-11b6-4270-88bf-668afe9c8a60/video.mp4

## Entry 7
- ID: 4731
- Author: Stefanos
- Created At: 2026-05-01T08:48:43Z

### Content

### 1 March: Finishing the arm holders and a TON of problems!

I had the idea to move the thing where the heat insert is placed (to hold the screws and the arm on the base) a bit higher, so that the arms wouldn’t be so high and the drone would look cleaner.

But while starting, I recognized that the holes for the screws on the base were 1mm offset (they were 5mm from the edge), so I moved them to 4mm. While doing that, I accidentally deleted the holes for the screw head T-T, but I could fix that pretty quickly.

And after moving it up, it looked like this:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTc2NCwicHVyIjoiYmxvYl9pZCJ9fQ==--e72be59b2d2f85537d722e89e160f42fc94c90dc/image.png)

And I also added that for the second arm.

But then I also added a slope for better grip and stability

After that, I decided to also add a slope on the underside of the arm. Here’s how it looks now:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTc2NSwicHVyIjoiYmxvYl9pZCJ9fQ==--a66991fcc26da216b2217f38d8ec287cd6e94ec1/image.png)

And here is how it would look then:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTc2NiwicHVyIjoiYmxvYl9pZCJ9fQ==--0d59371fabf58110e3529c77a47e5be0fe3ab478/image.png)

I decided to use the slope for more stability, but also so that the drone looks better and cleaner.

After adding the slope, it looked like that:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTc3NCwicHVyIjoiYmxvYl9pZCJ9fQ==--baef181d1c5a030581b2c69fb6a437f632778528/image.png)

But I wasn’t completely happy, because the line where the slope ended was very back, so it didn’t look very clean:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTk4NCwicHVyIjoiYmxvYl9pZCJ9fQ==--66822ec0b8de28d0d66d6c5214f659cbd2568fe5/image.png)

But after fixing and moving the slope a bit more forward, it looked much better and really nice:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTc3NywicHVyIjoiYmxvYl9pZCJ9fQ==--3f90a79873d5b268e7ecc44c7141dbd29e2bb853/image.png)

Now, after I fixed and implemented the slope for the arm and moved the heat insert part higher, I continued with the cable tunnel because now the insert part is higher and the cable has now nowhere to go through:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTc4MCwicHVyIjoiYmxvYl9pZCJ9fQ==--9f3ab6a5c8feae19646a98a8014667501526c8d1/image.png)

So I extruded the cable tunnel for 3.3 mm and rounded the edges with a radius of 1 mm:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTc4MSwicHVyIjoiYmxvYl9pZCJ9fQ==--c8e4d86699deca1ed5b93a9520c5a423eda8df47/image.png)

After completely finishing the arm, I continued with the connection of the arms to the base plate of the drone.

To start adding the case where the arms could slide in, I first needed to redesign the arms on the base, which took an ENORMOUS amount of time:
- I first had to measure everything  
- design the rectangles  
- then, because I have rounded corners:  
  1. calculate how big the circles are  
  2. calculate where the circles have to be placed  
- and then draw everything together  

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTgwMSwicHVyIjoiYmxvYl9pZCJ9fQ==--9804a2e052cb7a3651b0d1f8e255b8e6b1ca8ec6/image.png)

But then I forgot that I should add a tolerance of 0.2 mm to everything, so I had to update everything AGAIN.

So after repeating everything 4 times for the sloped arms, I had this result:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTgwMiwicHVyIjoiYmxvYl9pZCJ9fQ==--789d2a82926d427d7e3ffc092bc13afb2e08d3c7/image.png)

After that, I had to outline the parts, which was a challenge, but fortunately I managed it:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTgwNSwicHVyIjoiYmxvYl9pZCJ9fQ==--1b692d1e48989f295380c2f3a4944cdf097a76d1/image.png)

And again reconstructed that for all 4:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTgwNywicHVyIjoiYmxvYl9pZCJ9fQ==--bc942581c106bfd84dc6e2a102c9db1781e1b65e/image.png)

And lastly, after all this work (which was really suffering), I extruded the parts for 3.3 mm because the arm part is 3.1 mm tall and I wanted some buffer for the screw and heat insert.

After that, I also rounded the base with a radius of 4 mm:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTgyMCwicHVyIjoiYmxvYl9pZCJ9fQ==--eff4a712159c560de791ea7ca28c3199522ff2d2/image.png)

---

After the first part of this session, I started with the vertical arm holders.

For that, I first drew again the radius of where the arms and motors are located to know the exact positions:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTgyMiwicHVyIjoiYmxvYl9pZCJ9fQ==--97cbbf3051f4201e231c29ce46eaf1b37de2bdaf/image.png)

Then I marked where and how the arms are located to start again with the case for the arms:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTgyNCwicHVyIjoiYmxvYl9pZCJ9fQ==--f53e9cad2b53def3a4f0c7fc0ba8ce6580b169d1/image.png)

Then I drew the screw holes for the second arms with a diameter of 2.2mm (0.2 tolerance):  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTgyNywicHVyIjoiYmxvYl9pZCJ9fQ==--a9ada23a591dcf24defd1b60ddd68c333969746b/image.png)

And extruded them to -5 mm to create the holes:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTgyOCwicHVyIjoiYmxvYl9pZCJ9fQ==--a9dfb23d7a9e4f4cb301122392de3ed49dfb21f8/image.png)

Then I proceeded like before with sketching the arm outline case:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTg1NiwicHVyIjoiYmxvYl9pZCJ9fQ==--2b808cfa311cf86cb58d302551a645f0ef194eb6/image.png)

And also recreated it for all 4:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTg1NywicHVyIjoiYmxvYl9pZCJ9fQ==--d4e54b8519e3ebef3c4dc16fa2b48401215db087/image.png)

After extruding them again for 3.3mm, I saw a missing part, but I quickly redrew and extruded it:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTg2MSwicHVyIjoiYmxvYl9pZCJ9fQ==--8de233ab4faf3f7d7e224469a08918ada2758810/image.png)

Then I noticed that I forgot to make the holes for the screw head on the other side:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTg2MiwicHVyIjoiYmxvYl9pZCJ9fQ==--016b521f07d67721016beaa7bfdb83753708bf28/image.png)

Then I thought I was finished… but had AGAIN a problem:
the holes didn’t fit perfectly because the centers were different (4mm at the base and 5mm the arm), so I fixed that.

Before:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTk2OSwicHVyIjoiYmxvYl9pZCJ9fQ==--7a9177017aa347f4caf6d399ae92a96591fae614/image.png)

After:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTk3MiwicHVyIjoiYmxvYl9pZCJ9fQ==--4f2628ce2ce86e22e21ef96561f390e8fe8d230c/image.png)

It worked, but somehow other holes disappeared again, so I had to redo them.

Then another problem: one part didn’t extrude:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTk3MywicHVyIjoiYmxvYl9pZCJ9fQ==--0a335c3e8752c07d398b00f26d493d1e4eb4f211/image.png)

So I fixed the borders and extruded again:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTk3NCwicHVyIjoiYmxvYl9pZCJ9fQ==--aa0a05108e76de1024e83aa97f557504b9b4c978/image.png)

Then AGAIN I thought I was done… but the distance didn’t match (on the base it was 9.5mm but the arm was 10mm):  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTk3NSwicHVyIjoiYmxvYl9pZCJ9fQ==--27dbfcd8db12256bc7ac842cf8f81a8c65ec404f/image.png)

After fixing the lines, everything finally aligned perfectly:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTk3OCwicHVyIjoiYmxvYl9pZCJ9fQ==--cfce186eefd1f757d3dffad03cd7350d4ce01c8b/image.png)

After repeating that for all arms and fixing a TON of extrusion bugs, it finally looked like this and everything fits perfectly!!!  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTk4MSwicHVyIjoiYmxvYl9pZCJ9fQ==--af7b4a49c8a3bd43574708b73b5756a014b160e8/image.png)

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTk4MiwicHVyIjoiYmxvYl9pZCJ9fQ==--0979ad8b03abea1d3b0f29774f32881bd08674eb/image.png)

P.S. While writing this journal, I had a mini heart attack because the images didn’t load and only showed "image.png", but after refreshing they appeared again.

Also, I learned a new Fusion skill: you can go back to old sketches and apply changes. Soooo cool!!

Exhausting session but happy with progress.

### Recording Links

- https://lookout.hackclub.com/api/media/767e64b0-7fa2-45ec-92db-6d659050f224/video.mp4
- https://lookout.hackclub.com/api/media/1597db2d-4a67-44e4-9acd-be2e7ee1701c/video.mp4

## Entry 8
- ID: 4783
- Author: Stefanos
- Created At: 2026-05-01T16:17:49Z

### Content

### 1 May: Adding the combiner for the wall part and designing the small wall on the platform

In this session I wanted to make the connection between the base and the wall, because I plan that the main case (where the drone is connected with the arms) will be in 3 parts: the platform, the walls and the top dil

So in this session I focused on making the walls as a separate part.  
My plan is to have 3 main parts in the end: the base with the bottom plate, middle walls and the top cover.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwNjIsInB1ciI6ImJsb2JfaWQifX0=--ca8cd5d415cab5c6d281aba46a32dc5d95ee6c5e/image.png)

I want to connect the wall and the platform, like all other parts, with M2 screws and M2 heat inserts.

After starting the design, I wasn’t really sure where the inserts and screw holes should be placed, because in the front it’s mostly open and the camera takes a lot of space and has to rotate.  
So I first made a drawing and planned where everything should go, and decided to use this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMDQsInB1ciI6ImJsb2JfaWQifX0=--4cb15c5a846e5c47f5c381402c732fc3a9b6ae79/image.png)

Afterwards, I sketched where the screws should be and tried to figure out how to position them so they use as little space as possible:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMDYsInB1ciI6ImJsb2JfaWQifX0=--77541c52fd2dcfbdbead9f451db819c8685cd74c/image.png)

Next, I drew the hole for the screw itself and its head to check where it can be placed so it doesn’t collide with anything or doesn´t look good. I also had to consider the screw head hole on the other side:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMDcsInB1ciI6ImJsb2JfaWQifX0=--b223c83e77de4c062390a1edaca347628b52a6ab/image.png)

After finding a good position, I applied it to all four corners:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMDksInB1ciI6ImJsb2JfaWQifX0=--3e3ddc444ba6468745420f49adc6b2050e5a2487/image.png)

Then I cleaned up the sketch so it would be easier to check and extrude later:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMTAsInB1ciI6ImJsb2JfaWQifX0=--dc70f60c9c074bca4b8bdb2aaf11c548e327ac95/image.png)

I also changed the wall thickness from 2.5 mm to 2 mm because that should still be stable enough and saves weight:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMTUsInB1ciI6ImJsb2JfaWQifX0=--eef5607bed48920d54133f21449618dbca0a16c6/image.png)

After that, I added a 2 mm outline to all sides of the platform (except the front, because it will probably stay open due to the camerarotation).  
I also discovered that there is a tool for the outline, which I didn’t know before!!! That would have been SOOO useful in the last session

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMTcsInB1ciI6ImJsb2JfaWQifX0=--861d71936bbc45552ca1af5c708693a507670d8b/image.png)

Next, I continued with designing the mounting hole between the platform and the wall at the back (where the battery will be):

1. I found the center to align the hole  
2. I drew the screw hole (2.2 mm) and the screw head hole (4.3 mm, 1 mm depth)

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMTgsInB1ciI6ImJsb2JfaWQifX0=--bbbc46049647595e7c023f94ec653535627bc73d/image.png)

But the distance to the edge was too small, so I added +1 mm.

Then I noticed that the 4 corner holes were also WAY too close to the edge (only 0.3 mm), so I increased that as well:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMjIsInB1ciI6ImJsb2JfaWQifX0=--8336a09fd81199c3cbd3c2e124d8845e7467a391/image.png)

Then I added tangents from the screw head circle at 45° into the edge, so I can later split the platform and wall and still have a strong connection.  
(actually, I made all connections with 45° angles for better grip and stability.)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMjMsInB1ciI6ImJsb2JfaWQifX0=--7bfab22370af1e0392a4e04bc0d3a5373d591d8e/image.png)

Then I worked on the front connectors (where the camera and servo will be). Here I had to be VERY careful to leave enough space for the rotating camera.
I started by drawing two circles and kept a distance of 3.15 mm from the edge and from the arm holder. Then I added tangents and parallel lines so I can later split wall and platform cleanly:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMjQsInB1ciI6ImJsb2JfaWQifX0=--638f5d9a6bde421c12b8fb69a49e05e6013c0b2e/image.png)

Then I built that on the other side aswell:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMjksInB1ciI6ImJsb2JfaWQifX0=--7e29ad0f660fecaca0ab2911b1ca3e8adde87ea5/image.png)

So in the end it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMzAsInB1ciI6ImJsb2JfaWQifX0=--05800fa3303b7ecb658d3df51cbb0dcc87118d12/image.png)

But then I realized the inserts need thicker walls, otherwise they might break.  
So I modified the 4 corner connectors and made them stronger:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMzgsInB1ciI6ImJsb2JfaWQifX0=--5b9719144c82bce4b26a91dbd191676a1ed04de0/image.png)
and again, I made that for every of the 4

After designed the fist I applied that to the other 4.

Then I also improved the back connection by making the outer circle bigger and moving the hole deeper into the platform:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwNDEsInB1ciI6ImJsb2JfaWQifX0=--8801f1e02a5c67af29e1319be891d2ca41594d6b/image.png)

After modifying it, it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwNDIsInB1ciI6ImJsb2JfaWQifX0=--9afa29673202e25228841c08473a2d20785f1e13/image.png)

Then I realized I forgot to add a 0.2 mm tolerance between platform and wall (again), so I fixed that and extruded everything to 3.3 mm:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwNDgsInB1ciI6ImJsb2JfaWQifX0=--ea05788fdd2c494fbf09000966ce6095debeb9b7/image.png)

And finally it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwNTYsInB1ciI6ImJsb2JfaWQifX0=--5455bbe6b7683a0b613c2ced05ead39ecec8a173/image.png)

After cutting the screw holes and screw head holes, I got this beaufully piece:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwNTksInB1ciI6ImJsb2JfaWQifX0=--d91679675f26f5b77f59bbd159587dc0e2a57959/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwNjAsInB1ciI6ImJsb2JfaWQifX0=--557d82259e5a7a1acd1f0155451b1d710d0c5492/image.png)

P.S. I noticed I wrote "1 March" in the last journal, that should be May, sorry ;)

Happy with the progress. Next session will be about the walls. Pretty excited!!


### Recording Links

- https://lookout.hackclub.com/api/media/1f9980de-f783-43fc-88d0-abf6451be263/video.mp4

## Entry 9
- ID: 5082
- Author: Stefanos
- Created At: 2026-05-02T08:45:23Z

### Content

### 2. May: Designing the connection to the walls and designing them!!!

First, I inserted the sketch (using Insert Derive, a new feature that I learned) with the combination sketch from the platform and the walls. Then I projected the important parts (here only the connections) to a new sketch so that I can redesign them. I also learned the tool to project points, lines, and bodies, sooo cool!

And after doing that it looked like that:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAxNjksInB1ciI6ImJsb2JfaWQifX0=--9c2cf0a0f4928726437140448c8b69f1998e7846/image.png)

Afterwards I added a tolerance on all sides (where I haven't already applied one) of 0.2 mm so that everything will fit perfectly:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAxNzQsInB1ciI6ImJsb2JfaWQifX0=--68eb062abbcad8ee4fdd4d9736cea3a84632a2d2/image.png)

For the beginning, I extruded them to the height of the connector, so 3.3 mm, but I will probably have to adjust that in the future (and I forgot to say I also added a tolerance of 0.05 mm):
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAxNzksInB1ciI6ImJsb2JfaWQifX0=--983b69a8cdeb25ef4535dc9a27a51b6a3a5a2036/image.png)

Then I continued making the holes for the heat inserts:

1. I again projected the center points of the connectors to draw the circles  
2. Luckily I knew which diameter I should use for the heat insert holes: 3.3 mm, because I already did that for the arm holder heat insert holes, so I just copied that value  
3. Then I drew the circles with the projected points as centers  

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAxODEsInB1ciI6ImJsb2JfaWQifX0=--5531d8ab55676e1fb16aa8d24fe3036ff41d4971/image.png)

Then I proceeded with extruding them:

I extruded them 3mm + 1mm in height because the insert has a height of 3mm and needs 1mm buffer for optimal grip (thanks Google). And added additionally 4mm for more strength! 

But during that, I encountered a problem: the extruded connectors were only 3.3 mm high, while the holes were 4 mm.

So it looked like that after extruding. The only problem was that I extruded the holders only to 3.3 mm and the holes to 4 mm. That’s why I had to go back to the beginning (T-T) and extrude them more so that they properly contain the holes:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAxODMsInB1ciI6ImJsb2JfaWQifX0=--9d6ea0a38e4e88bb266fad10379b04b5212d7d29/image.png)

But after repairing and redesigning everything, it looked like that:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAxODgsInB1ciI6ImJsb2JfaWQifX0=--818f57269e53dde9e3037a599d782f6b2714fd21/image.png)

After all this progress, I wanted to properly see how everything looks assembled, so I:

1. Created a new file called “All-together”  
2. Then I had to google how to combine or insert everything into one file, because I first thought you just copy the parts (completely wrong). I found out about the feature “Insert Derive” which lets you insert bodies, sketches, etc. into another file and it updates automatically if you change the original file  
3. Then I inserted the base file and the walls, which were perfectly aligned already, so I didn’t have to move them. But the arms were a pain: I had to move them manually and align them perfectly. Then, because I didn’t know about the mirror tool at first (which would have saved me sooo much time before T-T), I copied one arm again. After that I found the mirror tool and mirrored them along the Y-axis  
4. I also organized the bodies folder by creating two subfolders called “walls” and “arms” so I can work more cleanly  

Then after doing all that, I saw the drone fully assembled for the first time  and it was ABSOLUTELY FANTASTIC!!!

To continue, I inserted the sketch from the walls and projected it to a new sketch so that I can modify it independently from the other parts:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAxOTMsInB1ciI6ImJsb2JfaWQifX0=--95695dfc55a208d6f3babdc06ae8954cd9718efa/image.png)

Then I redrew the walls and also extended them over the arm connectors so that there are no holes and everything is nicely connected:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAxOTcsInB1ciI6ImJsb2JfaWQifX0=--7078ea3331abcc46ca1218864e08c97fb30d9b60/image.png)

After selecting all the wall parts, I extruded them to 8 mm as a new body, so I can later cut the bottom part because otherwise it would collide with the base:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAxOTksInB1ciI6ImJsb2JfaWQifX0=--0978c0733c5248e048a94e0c30792165e38166b8/image.png)

The problem during cutting was that I couldn’t find a cutting tool, but I discovered that you can extrude and enable “cut mode” and that worked perfectly (cut for 3.3 + 0.1 mm tolerance):
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAyMDEsInB1ciI6ImJsb2JfaWQifX0=--be514dd3e5c324b25f8b917e31a357b6476b39fd/image.png)

After saving that file and updating the All-together file, it looked like that (almost perfect):
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAyMDIsInB1ciI6ImJsb2JfaWQifX0=--a9c13bbeff164d430119fb1a0a0259d03d066aa6/image.png)

But there was a small detail that didn’t look nice and made the CAD unclean:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAyMDQsInB1ciI6ImJsb2JfaWQifX0=--5e73756e57729062e867094fe6064fd5cd2d8a6b/image.png)

To remove this small wall cut , I went back to the sketch and drew the missing part by making a +0.2 mm outline. That fixed the problem, and after extruding it looked clean again:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAyMDgsInB1ciI6ImJsb2JfaWQifX0=--b51afa541c1c14b1d40e8026a97d6abd81c840e0/image.png)

I was almost finished, but there were a huge number of edges and corners, so I decided (for better look and better 3D printing) to round them all.

I mostly chose the rounding radius by feeling (look + space saving), and after doing that it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAyMTMsInB1ciI6ImJsb2JfaWQifX0=--677b5d05a34ba797fdf895637b68c9a36a33da63/image.png)

A positive side effect of rounding was also that I gained more space for the PCB.

And lastly I updated the All-together file again, and now the drone looks like this (amazing, jippy!!):
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAyMTQsInB1ciI6ImJsb2JfaWQifX0=--d929d84e51fc2480a3a6867f928fbb1b3e7589bb/image.png)

VERY happy with the progress today, because I was really afraid of starting with the wall connections since I didn’t really know how to design them, but in the end I got this!!

### Recording Links

- https://lookout.hackclub.com/api/media/24cd763d-6736-4204-b814-cc2be1a67d77/video.mp4
- https://lookout.hackclub.com/api/media/8c2a5f22-0b6b-4388-be14-7067c33dfd82/video.mp4

## Entry 10
- ID: 5152
- Author: Stefanos
- Created At: 2026-05-02T17:59:32Z

### Content

### 2. May: Finished the Main CAD design on the drone!!!
At the beginning, I firstly saw that the cable flow/canal wasn’t perfect and big enough because there was about 1 mm space for the cable, which isn’t really good (and enough):
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzNTEsInB1ciI6ImJsb2JfaWQifX0=--9f93637393fc6aedb85c0dd92da8a92603b5578d/image.png)

So I had 2 ideas on how to fix the problem:
1. Complete the bridge over the connector but make a half-circle cutout to make the cable flow bigger  
> would look like that  
> ![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzNTIsInB1ciI6ImJsb2JfaWQifX0=--36fb9b704263b7fcc5973e23749e69e2f05aa864/image.png)

2. Or make it from the inner side of the drone (at this part oblique), so that I can gain another 1 mm and from the outside it would look completely normal  

btw, my goal was to get a "tunnel" of 2–3 mm, not 1 mm like now  

So I firstly tried the 2nd option because I liked it more:  
1. Measured exactly where the connector begins and ends so that I know where the oblique should be, and got these values  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzNTMsInB1ciI6ImJsb2JfaWQifX0=--a1abf610a127a93db241341c20a3dfada9b1a44e/image.png)

2. After knowing where everything fits and all values, I created a new sketch and started drawing the distances  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzNTQsInB1ciI6ImJsb2JfaWQifX0=--bec268960107a0aa8c665b911cc69c9f0ab75623/image.png)

But when I started to make the oblique, it became a horror!  
Because I didn’t know how to create an oblique, I googled and saw that you can deselect tangent chain, then just mark your line and it would work. But I had the problem that the whole line was connected with the curving tool, which was very annoying. After like 10 minutes of trying, I gave up and searched for another way to make it. I saw that you could split the thing into 2 bodies and completely separate the lines, but for some reason that didn’t work either. So I gave up on the oblique and continued with the half circle:

Because I had all values, it was pretty easy and I just had to find the center of the line of the circle and made a circle so that it looked like that:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzNTksInB1ciI6ImJsb2JfaWQifX0=--a8d2af3e62009dff37806f65eade7033367277f3/image.png)

But I wasn’t completely happy with this because it was too big and didn’t give the arm support for stability. So my plan was to make the circle thinner so that it does have friction with the arm, so that it isn very stable. So I wanted to make it thinner like this:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzNjAsInB1ciI6ImJsb2JfaWQifX0=--12bcd604cfd6d246069ce3335451fd9721544f80/image.png)

So after measuring the new distances and drawing the new circle and cutting it out, it looked like that, which is much better:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzNjEsInB1ciI6ImJsb2JfaWQifX0=--7c6477e06cfa45e1b016b7c59fb2816a9d9b1e1f/image.png)

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzNjcsInB1ciI6ImJsb2JfaWQifX0=--fbd5b96d9f45633883dedaaa188102c5ff768f1c/image.png)

But then I noticed that I had added a small tolerance between the wall and the platform, which is for the grip and stability not the best, so I removed it and then it looked like that:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzNzAsInB1ciI6ImJsb2JfaWQifX0=--b507b9af18c8982aee48fa7293a71bd92858a6ac/image.png)

And after everything was fine, I applied the holes to all other 4 corners:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzNzUsInB1ciI6ImJsb2JfaWQifX0=--c2e57eb03e1afb4111baf6736bc9a1e3f06e5d8d/image.png)

---
Next I wanted to continue with the walls, but I couldn’t just extrude the base right now because there are also the connectors, and if I extruded it, I would also extrude the connectors.

So I had to first create a new sketch on the walls, project the original walls, fill gaps, and then make an outline of 2 mm:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzODEsInB1ciI6ImJsb2JfaWQifX0=--cab35507641e13c1cf6a6b577ee23f062730d534/image.png)

After that I could extrude the walls, but I had to think about the height of the drone, so I looked up how tall the parts will be. The tallest parts were (camera and battery) (in my opinion before I searched it up):
- for the camera I couldn’t find any dimensions, but it seems small like 2–3 cm, and the battery is 22 mm high, so I decided to make the drone 40 mm high so that everything fits for sure and I have some buffer and also space to add later stylistic accents  

But after looking at the drone in All-together, it looked pretty chunky...  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzOTksInB1ciI6ImJsb2JfaWQifX0=--3ea7a4219798141b3b67843d4d8c3128d4dc8822/image.png)

So I then tried adding only 30 mm, which looks much better:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MDIsInB1ciI6ImJsb2JfaWQifX0=--16ab2b4e71ac6ef8d5fb4cd0e9fdb692bdf4f532/image.png)

After the walls were standing, I wanted to focus on rounding the connector to save weight, material, and space, and so that the 3D printer can print the parts more easily, faster, and without errors.

But I didn’t want to use the rounding tool because if I print the parts upside down, it’ll need many supports and would be harder to print. So I decided to use straight corners that kinda round the connector. For that reason, I searched online and found the perfect tool/feature from Autodesk Fusion for that: chamfer, which makes edges, and this is perfect for my case.

So I directly applied that and this is:

before  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MDQsInB1ciI6ImJsb2JfaWQifX0=--e509134cbce06d05117e2c32e718451f268a06b6/image.png)  
after:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MTAsInB1ciI6ImJsb2JfaWQifX0=--151d4092d13c6805d350cc943ab0efce704dd2f9/image.png)

---

After the walls were firstly finished, I continued with the case of the drone.

Therefore, I started by creating a new file called "cover" and inserted by derive the sketch of the walls of the wall part:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MTEsInB1ciI6ImJsb2JfaWQifX0=--95d4257b8cf8a188f9afa91cd0c6ee2f54ba1cb1/image.png)

After projecting and drawing all missing parts of the walls, I outlined the inner wall edge by 0.3 mm per side and extruded the whole cover by 5 mm:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MTUsInB1ciI6ImJsb2JfaWQifX0=--0f59cdb4c4d039bb47f77854985feae16ef4e559/image.png)

Then I wanted to add a bit of an oblique to the cover because I saw in a very good video that it is helpful (https://www.youtube.com/watch?v=XKrDUnZCmQQ). If the cover originally doesn’t fit because of 3D printing, in that case you can add an oblique so that it at least fits a bit.

So after searching, I found out that the best solution for the oblique would be to use the draft method. So I tried implementing it and it worked on the first try!!! I made it go down by 10°, and after that it looked like this:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MjQsInB1ciI6ImJsb2JfaWQifX0=--6ceda075e7768d6dc9ff2f55ee7c457bfd87de1d/image.png)

I also decided to remove the inner part of the cover to gain more space, lose weight, and get more flexibility if it doesn’t fit very well. I decided to leave an edge of 2 mm and a depth of 1 mm (because on the top comes again 3 mm).

So I began with the removing. Like I said before, I left 2 mm width and it looked like that:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MzQsInB1ciI6ImJsb2JfaWQifX0=--46bc4695d76828459bbe54cc7dd3d45b98a4e740/image.png)

And now I had to design the thing that holds the cover because now it would just drop into the box. I decided to make it only 3 mm height because it’s stable enough, looks the best, isn’t too big, and has the least weight. After projecting and drawing again the lines, it looked like that:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MzUsInB1ciI6ImJsb2JfaWQifX0=--4a8e14ddfc47504cfb65b41e5c9a2a907a24f141/image.png)

And then, like I said before, I extruded everything by 3 mm:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MzcsInB1ciI6ImJsb2JfaWQifX0=--267540a520b058b896b1c58b9718703ef4864161/image.png)

Lastly, I also attached the cover into the All-together to see the final result:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA1MDAsInB1ciI6ImJsb2JfaWQifX0=--93f6ae1635d059d170cd8b5cea88777fe03c0f6c/image.png)

Overall, very happy because I finished the main drone CAD and now only have to design the holder for the servo + cam, the PCB holder, the sensor holder, and the pogo pins holder, but that will happen later (excited for the servo, although it’ll be very hard). Oh, and the wind guards (very important), almost forgot.

### Recording Links

- https://lookout.hackclub.com/api/media/def8403b-72f5-4a88-9f0d-cbc23318e899/video.mp4

## Entry 11
- ID: 5483
- Author: Stefanos
- Created At: 2026-05-04T20:31:08Z

### Content

### 3 May: Building the camera and servo mechanism

**FOR CLEARANCE!!!**: I accidentally left the recording running while printing and measuring one part. It begins from there on where the screen is black! Please **DO NOT** count these hours. I do not want to get banned (so I think the last 30 minutes were not stopped, so don’t count them).

Today I wanted to make the servo camera stand rotating thing, so that I could finish the main CAD.

To start, I searched for the camera size and where all the holes are positioned.

But after going to the AliExpress page of the camera I’m going to buy,

I quickly realized the problem: there were NO sizes of the camera. So I decided to search the camera on other sites, but I couldn’t find the exact product. After finding the manufacturer, I found some more products from other sellers, but again: NO DIMENSIONS

So I decided to take the dimensions of another camera that had dimensions and decided to draw the holes for the camera, then when I bought the cam. But now I will just design the plate and the holes later in the build phase.  
The size of the camera is 24×25 mm.

So I first made a drawing to test and make a plan. I decided to make an arm that connects to the holder of the cam and can be rotated via the servo, so that the camera can look to the front but also down.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA2NjAsInB1ciI6ImJsb2JfaWQifX0=--9eec1d36fa4c4a89b077c0f2613315bb8ec019c7/image.png)

Then, after drawing, I searched for the dimensions of the servo motor to start with the design of the servo motor holder.

And then I found a perfect sketch of all sizes:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA2NjMsInB1ciI6ImJsb2JfaWQifX0=--339a74b3ee9b84e6d7bf642a527271faec31f994/image.png)

But then I planned the thing I was the most afraid of: the camera holder and connector to the servo:

But before I continued, I thought about the servo-to-arm holder connector, because I remembered that I once (3 years ago) built one of these, but they broke very easily and I had to glue them together, etc.
![WhatsApp Image 2026-05-02 at 22.22.46.jpeg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA2NjcsInB1ciI6ImJsb2JfaWQifX0=--0b3250becfab271d9f24e4167ec92468cf44d98d/WhatsApp Image 2026-05-02 at 22.22.46.jpeg)

But I think the problem was that the part around the servo rotator was too thin, so I didn’t have enough place to get grip on it, and also it was too thin, so it broke. So this time I’ll try to build that bigger and also more stable. 

But because I firstly didn’t know that my printer could print the rotator which is clipped on the servo, because there were tiny components of 0.1 mm, I sadly decided to design a part around it and glue it with super glue and then connect it to the arm/cam...

---

So after clearing everything, I started with the 3D design. I decided to start with the servo motor holding case.

Therefore, I created a new file called "servo_holder" to design the holder of the servo motor first.

Then I continued by making a first draft sketch of how big the servo is and drew all the sizes from the side view.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA2OTIsInB1ciI6ImJsb2JfaWQifX0=--b0f52541751ec0a69d5349ad58a1e3494a55c943/image.png)

After that, I added a tolerance of 0.2 mm to every side so that it would fit well, and then I also made a bigger hole on the lower left side of the holder, which has a radius of 4.5 mm, to make sure the cable can go through it.

On the bottom left corner, I also made a hole because I saw in a previous video that if you make holes in the corner, the parts that have to fit in the case can fit better and with a higher percentage.

And lastly, I also rounded the corners to optimize the 3D process.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA2OTMsInB1ciI6ImJsb2JfaWQifX0=--e4eb96747df66cdfc9638adaffffd31066674642/image.png)

After that, I also extruded the whole thing (bottom) by 1 mm, then the walls, where the servo motor will sit for 12 mm, and then an additional 3 mm on the top.

But because the servo is completely still and doesn’t move, I thought of this:

To connect the servo to the connector, I had to screw in the screws that are delivered with the servo directly into the 3D-printed material. I directly tried that out on the holes of some older benchies:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA2OTUsInB1ciI6ImJsb2JfaWQifX0=--4da1ed9a230480b3b8d22fc611ba44140c98be39/image.png)

And then I found out that the best diameter for the hole was 1.5 mm, so I went to the next step:

After searching the positions of the holes on the 3D model and applying them to the 3D model with a tolerance of 0.2 mm, it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA2OTYsInB1ciI6ImJsb2JfaWQifX0=--9510172087d2a261c82e25fb4513f9442567d8a6/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA2OTcsInB1ciI6ImJsb2JfaWQifX0=--d1df4bdfcc002ed52f68997574c0a814ed7a8856/image.png)

And after that, I rounded the corners of the 3D model:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA3MDEsInB1ciI6ImJsb2JfaWQifX0=--dcbd1f22cb584ab3cb4f88d1a11febebc0cdec2f/image.png)

After all that, I also added the bottom and the top, so that the servomotor is perfectly covered and clean.

For the bottom, I first made it only 1 mm, because the height would be experimented with because of the rotation of the camera.

- I started by creating a sketch on the underside of the connector, projecting the essential points and lines and drawing over the gaps.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA3MDIsInB1ciI6ImJsb2JfaWQifX0=--5b5733ea08356446b495f6758770004d21a2afc4/image.png)

After that, I exactly did that on the top/cover:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA3MDgsInB1ciI6ImJsb2JfaWQifX0=--21641326ae228b402ae01c676180823fd683393d/image.png)

And after all this, this part was finished (just on the top 3 mm).

---

After finishing the servo holder, I continued on the servo connector with the camera holder.

And then I thought of another idea because I did not like the idea with the glue:

I found a 3D model of the horn and printed it quickly to see how good it would be (it took only 3 minutes to print, yippe!!!).

During the print, there were many crispy sounds, so the filament is very wet. I need to dry it later in the build phase (btw it’s currently 0:15 am T-T).

Some insight of the print :3
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTE0MzgsInB1ciI6ImJsb2JfaWQifX0=--a0ff19ab6681486937245908a8eb43bdaf6ca3e7/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTE0MzksInB1ciI6ImJsb2JfaWQifX0=--47f60d9baa60475280231aba733ce73476340eed/image.png)

..., and it fitted PERFECT!!!

Next, I started by importing the 3D model so that I could then take the parts that I needed and design the camera holder.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA4ODgsInB1ciI6ImJsb2JfaWQifX0=--10692ed1a3e135b409079144512fb3f6b9009446/image.png)

After importing, I saw that the model did not have any sketches, so I couldn’t use it. But luckily, after finding the designer again, he showed all the important instances:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA4OTMsInB1ciI6ImJsb2JfaWQifX0=--8cf3b160b47ecb8b29df85a721a1269951bfb641/image.png)

So I started designing:

I started with the circles, which were very easy to design:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA4OTQsInB1ciI6ImJsb2JfaWQifX0=--e63fcc89383d50347f9b78ffb1a37f3343f26f52/image.png)

(Btw my lookout is crashing ALL THE TIME and it didn’t record for some reason for some minutes, the 2nd monitors where I am writing this. Not sure what it missed, but FYI I searched up again, like I said before, the 3D thing and the website and wrote that during this time.)

But then I had to think about how to make those teeth, because I didn’t want to do everything manually.

So, after searching online for the best way to make this, I found out that I first had to create one tooth manually and then there is a feature called circular pattern that can create the others. So I started by creating only one first:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA4OTgsInB1ciI6ImJsb2JfaWQifX0=--260bbdbfd57e814fe272d6aa9fdd9b96a4d4a892/image.png)

And after that, I opened the circular pattern tool, selected the tooth and then the middle points of the circle, counted on the reference how many there are (21), typed that into the settings of the pattern tool, and... FIRST TRY!!!! It worked.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA5MDAsInB1ciI6ImJsb2JfaWQifX0=--50ff51682d3927b31ddc04938ecd4735f0903814/image.png)

Amazing!!! Next, I drew the holes around the teeth so that there is a wall, and I also did that with 1.5 mm for best stability:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA5MDIsInB1ciI6ImJsb2JfaWQifX0=--1598c928608b17e8cb751645a9e7efc5ee4554f2/image.png)

After that, I extruded everything for 2.5 mm because that part of the servo is about 2.5 mm.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA5MDMsInB1ciI6ImJsb2JfaWQifX0=--dd52e70794e798d69e35cc9981491592dfccc6f8/image.png)

Then, after that, I added the separation so that you can screw the holder to the servo with a screw and the screw really holds the connector to the servo and puts pressure on it.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA5MDQsInB1ciI6ImJsb2JfaWQifX0=--724273f707373532099ba36793f3d26777b3bdbd/image.png)

And lastly, I extruded the walls again, so that in the end it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA5MDUsInB1ciI6ImJsb2JfaWQifX0=--c36a2beb2a3f9a63498efa5fd316b230f1a572b1/image.png)

Then I made the arm that goes from the connector to the camera and made it exactly 20 mm long because it is the closest possible distance from the arm that does not hit the servo, and the servo has to be 20 mm above the ground so that the camera can rotate perfectly under the drone without making it look unclean. And I made the thickness 5 mm like the whole connector, so that it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA5MDksInB1ciI6ImJsb2JfaWQifX0=--03c7341ba9491c95bb150e68c448973804b388f8/image.png)

But then I wasn’t sure how to position the plate that holds the camera onto the arm:
- Should the arm connect to the middle of the plate, the top, or the bottom?

And I asked myself so many of these questions!!!

But in the end, I decided to make it in the middle first because it is the most reliable and you can calculate more easily where the camera will be. But the 3D print would be bad because it had to print the teeth upwards, and this would cause bad grip, so I decided first to make it from the top. But then I thought that the servo had to be 20 mm up in the air, and if the camera is about 25 mm high, then the camera would be over the drone, which would look horrible. So I decided to calculate roughly: the camera is 20 mm high, but the camera has to be in the middle, so 25 mm - 20 mm = 5 mm. The connector should connect from the top 5 mm down, so something like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA5MTYsInB1ciI6ImJsb2JfaWQifX0=--8364f18b79045361763967b445f87b925b84e224/image.png)

After drawing the camera holder with the dimensions of 24×25 mm, it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA5MTksInB1ciI6ImJsb2JfaWQifX0=--63b08f182dca509e154334e426007e5071deef97/image.png)

And I extruded that for 1.5 mm.

Then I saw that I built the direction from the camera holder wrong (the servo connector had to be rotated 90 degrees to the left T-T).

So after deleting and turning everything, I drew it again and it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA5MjIsInB1ciI6ImJsb2JfaWQifX0=--398525769b1aa8b6824f0cab79de47ca44365b86/image.png)

After that, I wanted to print that part, so I exported it and printed it out...

And after testing it out, they were PERFECT!!!!!
![WhatsApp Image 2026-05-03 at 14.13.46.jpeg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA5NTQsInB1ciI6ImJsb2JfaWQifX0=--a4d227cb1e919b9921e95c328f9b01e9aae0e00c/WhatsApp Image 2026-05-03 at 14.13.46.jpeg)

Next, I want to combine both parts and add them to the base:
So, I
1. opened the base file again and measured the middle to first see where the camera would be positioned
2. drew where the camera will be (the camera is about 25 mm wide)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA5NTcsInB1ciI6ImJsb2JfaWQifX0=--4b05c21605ae764edc431b5931e2dfc056f844f0/image.png)

And after measuring how long the arm to the center exactly is, to see where the servo should be positioned, it was 21.5 mm. But I also have to add 1.5 mm for the thickness of the camera platform.

> So together it is 21.5 + 1.5 = 23 mm

I also wanted to bring everything about 2 mm more back because the camera is pretty chunky and I do not want it to be completely outside.

> So in total it is 23 mm + 2 mm = 25 mm

So after I drew the middle points of the servo gear:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA5NjIsInB1ciI6ImJsb2JfaWQifX0=--d9b2dc64b9860a3792d4622fb643628fd04dabbc/image.png)

But then I realized that I was extremely dumb and that, how I designed it, it would not fit:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA5NjUsInB1ciI6ImJsb2JfaWQifX0=--5849aaa6ea43229cf8773f2a4f0710f2be4025d3/image.png)

So after measuring how much space I had on that thing and on the inner sides (inner wall to inner wall I only had 35 mm, which is very small because the servo itself is 30 mm),

But to fix that problem I had 3 ideas:

1. make the servo connector/arm thinner  
   > ![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA5NjcsInB1ciI6ImJsb2JfaWQifX0=--cfc44f94cd78620b9d435c137bc7fc8b6e64af60/image.png)  
   would save me 1.5 mm, and then I would also need to remove the back side of the servo motor holder  
   > ![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA5NjgsInB1ciI6ImJsb2JfaWQifX0=--eab515589a88b3763c23e96310b7725cf1a4dcc5/image.png)

2. I had to remove the back wall of the servo holder to save 5 mm, and that would mostly solve the problem.

3. If I would implement that, I would only have a width of 32 mm, but then the whole servo construction would still be outside the case. If I want the camera to be in the middle, then I also have to change the arm of the camera holding module so that the servo can be at the center.

So, I started by removing the back of the servo holder.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEwMDAsInB1ciI6ImJsb2JfaWQifX0=--83f645a505dafb812ca577d90893b913f95609ab/image.png)

After I drew the servomotor and the camera, I tried multiple positions, like the distances to the walls of the servo when it is connected to the connector with the arm, how far away it should be, where I also had to pay attention to the motor arm connector being higher than them and also higher than the platform-wall connectors, and lastly I also drew how the arms should be designed to hold the camera:

And so it all locked then together:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEwMDksInB1ciI6ImJsb2JfaWQifX0=--5c97807577602723015950acca418f460a870caa/image.png)

And after that, I inserted the servo holder into the file to position it right.

After I positioned it, I wanted to import a servo 3D model to see if it was fine.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEwMTAsInB1ciI6ImJsb2JfaWQifX0=--88a3ad3a53f2fe105696354fadc63753d5c4661d/image.png)

And after adding the servo into the servo holder, I saw that it didn’t fit perfectly, and after I also checked it with mine, it also didn’t fit perfectly. So I quickly fixed the values.

And then I had to recreate the servo motor arm/connector with the sketch I did previously, and then it looked like this:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEwMjEsInB1ciI6ImJsb2JfaWQifX0=--7c14b650a3efae4d1ff09cbab4283a56d8d11bf4/image.png)

After rounding like that:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEwMjIsInB1ciI6ImJsb2JfaWQifX0=--33459958e3b72ff6c911aaec205d631508f6da2d/image.png)

And after combining:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEwMjMsInB1ciI6ImJsb2JfaWQifX0=--a5f27f053e8ace75caaedcd1a8735768b716bf44/image.png)

Then I wanted to see if the rotation would be fine. That’s why I searched up how it works, and you could have done that with joints, which I wanted to do, but I first did not find the joints and then it also didn’t work, so I ended up just using the move copy tool.

But after it worked and I tried it, it was (after rotating) inside the connector for platform and wall and the arm connectors:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEwNzAsInB1ciI6ImJsb2JfaWQifX0=--0be7069fce9889ee47f5fc71c615e66e5d6e8bd7/image.png)

But then I thought for almost 30 minutes about how to solve this and thought: should the camera be inside the case, or can it also exit it for better compatibility? But what happens with the cable and where does it go? And if I let the camera go outside the frame, where will the cable go? And on and on and on...

So I decided to take a short break and go outside, and while doing that I had (firstly) a BRILLIANT idea!!!

- I could just connect the arm that connects the servo and the camera, and not at the top with the camera frame, but on the bottom, so that the camera does not go that far back when rotating. And after measuring it, it  works perfectly.

But I still had some issues:

1. The connector from the walls to the platform was blocking the camera arm and the camera itself

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEwNzEsInB1ciI6ImJsb2JfaWQifX0=--a83a07fd250c0e0ea6e58fbf0ffcdea4f40098e9/image.png)

> Solution: after a bit of thinking I had the idea to just curve the arm a bit earlier and deeper in the middle, and also cut a bit of material at the connector and make the camera arm a bit shorter, so that the whole construction can go further in the front.

2. I didn’t really know whether the camera should still be inside the frame or go outside, but I decided on the first option because during landing, the second option would just damage the cam.

And after finding an amazing solution, I started designing the arm of the drone again and changed what I said before.

So I started completely redesigning the arm and deleted everything except the gear in the middle:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEwNzUsInB1ciI6ImJsb2JfaWQifX0=--ce7e76412fe95071cb230491713c335234249144/image.png)

And then started designing that:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEwODYsInB1ciI6ImJsb2JfaWQifX0=--ff7a97d737caa1b82e093f2f421740e971dfc2b4/image.png)

---

BUT while doing that, I was completely shocked. I WAS SOOOO WRONG!!!! Making the arm go from the top to the bottom would NOT change the position of the camera, and then I almost cried because I worked on this mechanism for 5 hours and now everything was for the trash, and I had to almost redesign everything. But after a bit of depression time, I had a new idea:

I could just flip the servo motor 90 degrees to the right so that it does not lie on the ground (it stands upwards now), and the gear is on the bottom. Then I save a ton of place, and the height is fine, and then I wouldn’t have the problem with the camera size and motor arm connectors, because the camera would turn not completely to the back but further to the front and just be under the drone, but only by 8 mm, and that should be fine because my landing station will be about 20 mm high. So this time I really had the perfect idea:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEwODgsInB1ciI6ImJsb2JfaWQifX0=--993264e45139e659c073d954a93a4b391f1e3cd0/image.png)

So now I was SUPER motivated again and directly started modifying the servo holder.

I actually decided to build the motor holder again because I messed it up a bit, and I want to fix that now.  
I went through it exactly like before:

First of all, I drew the rectangles:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEwOTAsInB1ciI6ImJsb2JfaWQifX0=--9e9ee7806f1dbe2a68e1e24c8cd8c9f03121ed72/image.png)

Then I added at the top boxes in the center holes with 1 mm diameter for the screw:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEwOTEsInB1ciI6ImJsb2JfaWQifX0=--7ee6aa3545092d0a8f2b65c0b56038334b4f2038/image.png)

And lastly, I rounded everything for better printing:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEwOTIsInB1ciI6ImJsb2JfaWQifX0=--1b2e2ac27da253ac75a1b9227f440b393d830990/image.png)

And after positioning the base it looked like this:  
For the position, I paid attention to the center of gravity/mass position and the distance to the sides, so that the arm has enough room and is not too far away from the camera.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTExMDMsInB1ciI6ImJsb2JfaWQifX0=--56e42da3ede79c98261d32881323067e926ce7d9/image.png)

After placing the servo motor in the correct place, I measured where the center point of the rotating part on the servo motor was. I calculated and measured all distances so that everything would work.

And then I started designing the arm:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTExMDgsInB1ciI6ImJsb2JfaWQifX0=--2dec8c160228d5dfcdacf279a7746400a5cf1f20/image.png)

For the camera holder, I measured the distances for applying:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTExMTAsInB1ciI6ImJsb2JfaWQifX0=--67f6e7c17f588112332c957054bc71dcd6731dbd/image.png)

And after hours of trying, I got this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTExMTksInB1ciI6ImJsb2JfaWQifX0=--a58fcfc49312f51100ec749100ba0ff081691c6e/image.png)

And after all that, it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTExMjIsInB1ciI6ImJsb2JfaWQifX0=--e9dbf023df79eb0b4274940c93216576ac3fbe63/image.png)
<- fire

Happy with the progress: 7h!!! (sorry that the journal and session became so long <3, next one will be shorter) But also completely exhausted, do not want to touch that part again!!!


### Recording Links

- https://lookout.hackclub.com/api/media/95a0c005-7fa1-45bd-ac90-e32c879c7230/video.mp4
- https://lookout.hackclub.com/api/media/fd2ae5aa-daa7-4065-9fdf-1736ad547949/video.mp4

## Entry 12
- ID: 5794
- Author: Stefanos
- Created At: 2026-05-06T20:48:33Z

### Content

### 6. May: Fixing some issues with the servo motor and FINALLY finishing it!

Btw I’m currently in school and forgot my mouse, so designing will be tough with just a trackpad!

I started optimizing the servo motor sizes because after printing that part I noticed that it doesn’t fit:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIyMTEsInB1ciI6ImJsb2JfaWQifX0=--bd30f23a0ae5b175b25f7bc677133f19820b886b/image.png)

SO I decided to make the holder bigger by adding an additional 1mm to every side.  
But before doing that I had to remove the roundings from the holder to better make it bigger:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIwODcsInB1ciI6ImJsb2JfaWQifX0=--a65f0c3d0abd0514d36ab2d43a9bf46c7fc8ac5e/image.png)

After that, like I said before, I added 1mm to every side so that the parts would fit perfectly:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIwODgsInB1ciI6ImJsb2JfaWQifX0=--3075083a52b5fbe38d8f2caecb0e5ce235a5adf4/image.png)

And after rounding again it looked like this:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIwOTAsInB1ciI6ImJsb2JfaWQifX0=--9f7c6b38f425957d7974f2c123f6fd95bb48b9f4/image.png)

Then I saved the file and updated it in the all-together file,  
but for some reason I got thousands of errors and warnings that it couldn’t update the part. After checking what happened, I saw that I accidentally didn’t save some changes. But I also found out that I had one problem:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIwOTQsInB1ciI6ImJsb2JfaWQifX0=--d838d53cb2a867267998180400cc2f27d3ea6b64/image.png)

The holder and the wall connector were colliding....

So I had the idea to cut some material so that the servo would perfectly have its place. After cutting some material it looked like this, and I only had to delete one thin thing that looked strange:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIwOTcsInB1ciI6ImJsb2JfaWQifX0=--1f719a1d7212eb092057defcc6ad9c030ffb4f3e/image.png)

Then I had to head to my violin lesson and then back home. After doing German homework, I directly continued. (7pm now)

But for some reason it didn’t save my progress and I had to redo some steps T-T, like the rounding of the holder:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIxNDcsInB1ciI6ImJsb2JfaWQifX0=--274df9527c7559f6e7448342031090d534a0c2b4/image.png)

But the problem was that I was on the wrong timestep in the timeline, and after that everything was fine again...

(and then I noticed I didn’t record that T-T)

But after that I finally deleted this part that was overhanging.

And after rounding it looked like this:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIxNTUsInB1ciI6ImJsb2JfaWQifX0=--f99ce520bcee6942d468a735fbd0b081a9c0e889/image.png)

So after that process I am going to continue cutting the platform because the camera needs room and a cut in the platform to go underneath the drone.

But before that I had to position the camera arm perfectly, but that TOOK A LOOOOOT OF TIME. After trying, I found the perfect spot and positioned it:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIxNTgsInB1ciI6ImJsb2JfaWQifX0=--9ad7e7f91e99a6840aab7e06e495d16bb0d20498/image.png)

But while doing that I encountered 2 problems:  
1. The camera wasn’t perfectly centered  
2. The arm was too thick so that it almost touched the wall  

For the camera centering, I first measured both distances from the corner to the platform:  
left 2.476mm and right 4.586mm. After subtracting them and dividing by 2, I got 1.057mm that the whole thing had to move to the left. So after changing the sketch it looked like that.

But for some reason it didn’t update...

After googling, I saw that I should check if the Capture Design History is disconnected, if the link is broken, etc. But nothing worked, SOOO I decided to relink the arm and position it again, and it actually worked. It looked like this:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIxNjQsInB1ciI6ImJsb2JfaWQifX0=--c9f4178f39601c5b52274f68275537b2626db133/image.png)

And after making the arm thinner it looked like this:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIxNjUsInB1ciI6ImJsb2JfaWQifX0=--2eca0ddc83470ca3238b5cc420489188140ffa6a/image.png)

After that whole process I finally could cut the hole, but I wasn’t sure how to do this. After a couple of minutes of research I found out that you could use the revolve function, but it didn’t work for me, so I had to find another solution.

But after searching I checked again and understood that I was wrong, because I first thought that I had to select the whole body for that feature, but I just had to use faces. It was possible, I just forgot to apply some faces.

After finding that out I applied it, but I quickly realized that for some reason it was always shifted and not correct, which freaked me out:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIxNzgsInB1ciI6ImJsb2JfaWQifX0=--3f866075008c2c698772fd71bae407606e5bed70/image.png)

And after a ton of googling I found out that the face should be at the same height as the center rotating point, otherwise the point gets shifted and, like before, it would be wrong. So I had to cut the arm in half. For that I again searched online and found out that I had to create a plane and bring it to the right height, then select the object I want to cut with this thing, and THEN IT WORKED:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIxODQsInB1ciI6ImJsb2JfaWQifX0=--d7c82f05bf6476ed41a85071c8fb4abd9cbb2a1e/image.png)

After that I applied it to all sides on the inside, an outline so that everything sits perfectly:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIxOTgsInB1ciI6ImJsb2JfaWQifX0=--745e0f8532a5dc6fd13fc84bdcaec841ea40ca75/image.png)

Lastly I also deleted this part of the platform:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIxOTksInB1ciI6ImJsb2JfaWQifX0=--fb176e82ed4eb0fbc95c5dc28e4b02a9265bb0ba/image.png)

So that the camera thing can go through.

And after rounding the edges it looked like this:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIyMDUsInB1ciI6ImJsb2JfaWQifX0=--4b46bfd25fde6e8731a0a7cf5ddd37be63b96bce/image.png)

So one problem was left and then I go to sleep: the servo motor holder is higher than the walls:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIyMDYsInB1ciI6ImJsb2JfaWQifX0=--b2e4ddd93cfe5aaf33c79f46781654aa42a038fc/image.png)

That’s why I have to make the walls 4mm higher.

Final look of today:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIyMDcsInB1ciI6ImJsb2JfaWQifX0=--3fe116676f27643cfa4d8d0113b61937841a681f/image.png)

Happy, happy today, but it was a bit stressful with the cutting. Still happy that I managed that and excited for tomorrow!

### Recording Links

- https://lookout.hackclub.com/api/media/177c508f-c163-44e8-9c2b-65a405c1201e/video.mp4

## Entry 13
- ID: 5950
- Author: Stefanos
- Created At: 2026-05-07T20:39:42Z

### Content

### 7 May: Added the ToF-Sensors to the CAD Model and optimized it!

Today I wanted to make the holders for all 4 ToF sensors that I chose in an older journals.

But before I started doing that, I first created the meshes for the servo holder for printing the servo holder to test if now everything is fine (from the last journal).  
Therefore I first created a mesh, then opened it in the slicer, saved it to a stick, and started the print. But while the print was running I continued with the "real" part of the journal.
 
Some pics from the print :3

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI0NzQsInB1ciI6ImJsb2JfaWQifX0=--7dda47aa6317a8993b35c104332587905b9ee3dd/image.png)

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI1NzgsInB1ciI6ImJsb2JfaWQifX0=--24f14fa84c98f720c65d9f7fdddc2ff5d3c73ddd/image.png)

Then I started with the ToF sensor holders on the front, right, left, and the bottom.  
Next I continued with adding the holes for the sensors, but I wasn’t sure how to connect them and place them in the platform/wall:  
Should I make something like pins to connect them, glue them, or screw them, because they have holes?

And after a bit of searching online for solutions I found 2 typical solutions:  
1. Use normal screws  
2. Make little 3D-printed pins where you can place the sensor on it  

And I decided to use the 2nd option because it is less weight and easier to design. But therefore I had to find the sizes of the holes and the distances.  
Because I AGAIN couldn’t find the real sizes in the AliExpress store from the distance sensors. But then I found the sizes and searched for the best position for the sensor that was in front looking to the bottom, and then I first realized how BIG these sensors are. So I chose this position and drew them:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI0OTQsInB1ciI6ImJsb2JfaWQifX0=--12af1cff49a9421cbb5173f8423a686653a06149/image.png)

First I created a new sketch, found the center, drew the rectangles of the sensor and then the circles, made them slightly thinner, and after extruding and cutting the hole from where the sensor is looking, rounding the corners, and drafting the pins for optimal fastening, it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI0OTcsInB1ciI6ImJsb2JfaWQifX0=--0aefd69516d6aee3a2b1b483e585a961ef462ab1/image.png)

Then I continued with the left and right side sensors.

And after building the holder pins and the hole for the sensor it looked like that  
(same process like before):

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI1MjEsInB1ciI6ImJsb2JfaWQifX0=--4ee9d1d4d36b2035995a6929c9e3bb21fb734dae/image.png)

And then I wanted to copy that to the other side but I wasn’t sure how. But then I got the idea to just mirror the thing because it was identical, just that the holes and the pins would add to the other side.

For doing that I had to split the body into two parts so that I could mirror it and combine it.

But then I saw that I couldn’t just mirror it because that part is different from the other side, so I had to split it shortly before these parts:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI1MjIsInB1ciI6ImJsb2JfaWQifX0=--4d3b449729b653cdc2261ed8b221d6fa323f291b/image.png)

So I first created a new plane, split the object that shouldn’t be mirrored, then split it in half to copy the sensor plate, and then it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI1MjcsInB1ciI6ImJsb2JfaWQifX0=--ba4421c8e185129e62ae94cc79c800b25c49c464/image.png)

And after doing the bottom, right, and left sensors I continued with the front sensor, but there I quickly saw a problem: there wasn’t enough space for the sensor.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI1MjgsInB1ciI6ImJsb2JfaWQifX0=--0094e4d8114266c4bfc0f0e71c9577431efe1270/image.png)

So I decided to move the camera plate further down so that I can get a bit more space and can position the motor above it. I also think that it will look better because then it won’t be that open anymore right now. SOO I started by measuring it and it actually would be possible to do. After measuring it should fit, but very knapp, only 1mm free between them. But I started by moving the camera plate further to the bottom (8mm).

And after I edited that it looked like this:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI1MzQsInB1ciI6ImJsb2JfaWQifX0=--250029a8143b50823b219e7617064b79c530650e/image.png)

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI1MzUsInB1ciI6ImJsb2JfaWQifX0=--9e4cc2e514acd18a1c838e173ae1b2b4d5c3fc03/image.png)

The next step was to make a wall above the camera for holding and placing the sensor.  
But therefore I had to remove the case holder on that spot so that I have more space for the sensors.

But to start with I switched to the cover file and made a new sketch, selected that part that I didn’t need anymore, extruded it in cut mode, and after rounding it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI1MzgsInB1ciI6ImJsb2JfaWQifX0=--029c6f854e3d992ff378103451ab6e60792d5cf3/image.png)

Next I added this small “wall thingy” because there was too much room there and it looked unclean, so I had to change that and it was important for the next step (hope with that image it’s more recognizable):

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI1NDIsInB1ciI6ImJsb2JfaWQifX0=--3a2130dbba91f47c15ae90e846edcec0c955a80b/image.png)

So I first started by extruding that part in the platform and then adding the new fillet and then copying that to the other side:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI1NDMsInB1ciI6ImJsb2JfaWQifX0=--843fd32aa2d6e80f92bdf38d56574c0f41953555/image.png)

And after extruding that part for 1.495mm and rounding it, it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI1NTcsInB1ciI6ImJsb2JfaWQifX0=--7a6ec24166c71b1b2eee9b148c642bc6f849c4cf/image.png)

And after extruding the pins and making the hole (FOR THE 4th TIME now T-T) it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI1NjAsInB1ciI6ImJsb2JfaWQifX0=--b32ff037d52a0b79f5b03626b1d2c4fc4e6ba527/image.png)

And in total:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI1NjEsInB1ciI6ImJsb2JfaWQifX0=--f8dd10a65a6320e2858aac6967487f77d2d12f71/image.png)

And lastly for today I wanted to find the correct pogo pins and then also make the holes for them.

But after finding the best pogo pins (decided for them because shipping is very fast, very cheap, small, and only 2 pins for charging), I will do the implementing tomorrow because I’m tired a gotta finish presentation for school...

Here’s the link btw: [https://de.aliexpress.com/item/1005006525401310.html](Pogo pins)

Happy with the progress because I’m almost completely finished with the CAD model of the drone. Tomorrow I’ll implement the pogo pins and make the landing station, and then on the weekend I’ll do the electronics!!!!! (very excited!!)

### Recording Links

- https://lookout.hackclub.com/api/media/49cf092d-5564-4cd1-9689-c9ab40cbbf67/video.mp4

## Entry 14
- ID: 6140
- Author: Stefanos
- Created At: 2026-05-08T19:09:51Z

### Content

### 8. May: Finishing the Drone CAD: adding the prop guards!

Today I wanted to make the prop guards so that I don’t cut my fingers during testing (scared).

So I started by first creating a new file for the guards.  
2. created a new sketch

Then I continued with finding the propeller sizes: they are 76.5mm diameter.

And after searching how tall, how wide, and how much distance between prop guards and props there should be and how tall they should be, etc., I got this:  
4-10mm thick, 4mm distance between the prop and the guard, and make them higher than the prop for more safety.

After that I also decided that I will cut 2mm of the motor arm away where the motor will be placed so that I can recreate that 2mm and clamp the guards between the arm and the motor.

So I first drew how big the props should be and then added 4mm so that everything will work fine, and lastly also made an outline so that the prop will be 2mm thick:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI4ODMsInB1ciI6ImJsb2JfaWQifX0=--aede22889077582dea35b9ce3b8295e69a2559cf/image.png)

Next I measured how tall the motor props are so that I can extrude that part, but for some reason there were 2 values:

Thickness: 5.5mm

Maximum propeller thickness: 8.84mm

But I didn’t understand which was the real size of the propeller.

But after checking and googling I saw that the 8.84mm was the real one, and after seeing that you should use about 2x the height of the props for indoor use, I chose to use 16mm height. That is why I extruded that for that much.

Then I continued with calculating how tall the connector to the guard should be, because the guards also need arms. I decided to use a design like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI4OTAsInB1ciI6ImJsb2JfaWQifX0=--60e2738ede6eea02a22d90a932839d31dfe03a00/image.png)

For that I took the height of the props: 8.84, divided them by 2 because I want the center of the guards to be at the same height as the center of the props. Then I added the height of the motor and so I got my arm height size:

> 8.84mm / 2 + 11mm = 5.42

So I had to make the 2 arms 5.42 high but angled to the center. So I first started by making it.

So after that I drew the plate that should be screwed between the holder and the motor, so I drew the arm:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MDMsInB1ciI6ImJsb2JfaWQifX0=--4882d918148671bb108432b0852bec9efab86c8f/image.png)

And after I extruded it and rounded it I did that process also 90° to the right:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MDUsInB1ciI6ImJsb2JfaWQifX0=--59c71fee06751f369e20ae9c200554b8ff3fd012/image.png)

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MDcsInB1ciI6ImJsb2JfaWQifX0=--b0a25d092160f7d689b0e539bb6d0aaf12c2ebd3/image.png)

And lastly I added the plate between the arm and the motor.  
And after copying the upper 2mm of the motor holder it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MTIsInB1ciI6ImJsb2JfaWQifX0=--f17696851f2d66a360a948569ee15703c85c14a5/image.png)

And lastly rounded it.

After that I deleted the upper 2mm of the motor holder:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MTMsInB1ciI6ImJsb2JfaWQifX0=--c173ad9e5f81ba3d5c97f6287def6588ff3bc2cc/image.png)

But then I remembered that I forgot to add the hole for the cable tunnel.

But before fixing that I implemented everything into the all-together file to check if everything was fine.  
After adding the first one I mirrored the 2nd and then the 3rd and 4th, and after that it looked like this:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MTYsInB1ciI6ImJsb2JfaWQifX0=--79005654b4d72d62928cecf352ace1477ed92483/image.png)

But I still had the problem that the cable channel was blocked:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MTgsInB1ciI6ImJsb2JfaWQifX0=--8da0ac6b48ce3fcf64ff00085d4ea2236d408442/image.png)

SO I quickly edited a hole into that.

And after drawing the cable channel part:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MjAsInB1ciI6ImJsb2JfaWQifX0=--8e76bec8fa735cd627836915ff7cd5b94a4c377f/image.png)

I quickly extruded it in cut mode and rounded the corners:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MjEsInB1ciI6ImJsb2JfaWQifX0=--dc991c32f93bebbc3bfdd774033aa0107d861d23/image.png)

Lastly on the arms I wanted to round these corners because it looked very unprofessional:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MjcsInB1ciI6ImJsb2JfaWQifX0=--7a3315e18c09cb77726fab4b4ba8393d086413c7/image.png)

And after rounding it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MzEsInB1ciI6ImJsb2JfaWQifX0=--9ca21f5229598bf5c881451ccdfc54f74639e977/image.png)

So after all it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MzIsInB1ciI6ImJsb2JfaWQifX0=--701b8df09d1291cc2957e082deb2ae1261e4347a/image.png)

Then I noticed that I had unnecessarily much weight on the drone because these parts of the guards were unnecessary:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MzksInB1ciI6ImJsb2JfaWQifX0=--452cbf84a605e076bffa081f706335a765660fd8/image.png)

So I decided to remove them and rounded the corners, and then it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5NDIsInB1ciI6ImJsb2JfaWQifX0=--ff3950dd232d4a2314bdd22f972e2a856d4d79e6/image.png)

But I quickly realized that it wouldn’t fit if I implemented that like that because the guard would go into the walls of the drone:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5NDMsInB1ciI6ImJsb2JfaWQifX0=--f6b8291dead5b19fd5cb6ba32af5b74117e5b7b6/image.png)

So I decided to remove an additional 22.5° so that no problems appear:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5NDYsInB1ciI6ImJsb2JfaWQifX0=--c67f49d19699e59f8eb422ff39f6e798e134c68a/image.png)

And after saving and updating the inserted items it looked like that and was perfect!!!

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5NDgsInB1ciI6ImJsb2JfaWQifX0=--4ceda3771784d3c2881f99a37156fa52e825bd26/image.png)

But while I was correcting and rereading my journal I saw that I calculated that  
8.84mm / 2 + 11mm = 5.42  
and that is completely wrong.

So after checking the height I took in my sketch, it was 7.5mm for some reason, so I had to add 8mm to it.  
So I split the bodies and added the 8mm so that it was correct again, and after rounding, saving, and updating the CAD it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMwMDUsInB1ciI6ImJsb2JfaWQifX0=--239a63e52f7a906b77282ee2ec58adb733b8e316/image.png)

After I was basically finished with the CAD (for the drone), I wanted to see how much it weighed.  
So I put the whole drone into the slicer (without supports) and it weighed about 170g, which is actually good and about what I planned!

The only things that are missing in the drone are the holders for the PCB and the holes for the pogo pins, but I’ll do them while building the landing station (next journal).

Overall happy that I finally (almost) finished the CAD of the drone. Excited!!

### Recording Links

- https://lookout.hackclub.com/api/media/bb94bc1f-ba94-47e5-aa7d-022d8d77b695/video.mp4

## Entry 15
- ID: 6487
- Author: Stefanos
- Created At: 2026-05-10T20:22:48Z

### Content

### 10. May: Starting the PCB!!!

First I created a new folder in Autodesk Fusion 360 project called “landing station” because now I will start with the landing station!!!!

Yesterday in class we had a substitution lesson and I had 90 minutes to think of a concept for my landing station, and my planning looked like this:

![WhatsApp Image 2026-05-09 at 21.38.32.jpeg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM0MDYsInB1ciI6ImJsb2JfaWQifX0=--b2b3a544b6c2124d6444fb399c68ceee0f1f5ffd/WhatsApp Image 2026-05-09 at 21.38.32.jpeg)

Basically:
1. I thought of making a funnel-like structure on the top that is 10mm wide so that if the drone has an error of max 10mm it would center itself  
2. It’s separated into 2 parts: the platform with the walls, and the funnel part — I’ll do it in two parts so it can be printed better and without problems  
3. I decided to make a plate exactly under the position of the camera so the drone can land perfectly  
4. There will be LEDs or a small display that shows the battery percentage and whether it is charging, and the landing station will be powered by USB-C and the power goes through pogo pins into the drone  
5. The whole thing will be about 50mm tall so the drone can still recognize the AprilTag in the last centimeters of landing  
6. Everything will be mountable without screws so parts like the AprilTag holder can be moved forward/backward for adjustment  

After that (now), I first wanted to create a new file called “platform”, but when I tried I got a message that I reached the document limit, so I was cooked T-T.

So I submitted the form for pro for students, but it takes up to 24h. SOOO I decided to make the PCB of the drone instead (scared, never did a PCB before!!!).

So I started KiCad and created a new project.  
Then I had to check how I could add a Raspberry Pi and the flight controller so I can make my circuits.

For that I first opened the MAVLink connection video again to check which pins I needed. I saw that I needed TX2, RX2, and GND → so 3 wires.

Then I remembered JST-GH connectors, which are like safer and better male/female connectors. So I decided to use them. The Raspberry Pi would then connect like this:

RX2 → TX2  
TX2 → RX2  
GND → GND  

At first I didn’t really understand what these pins do, so I started researching:

TX (Transmit): sends data out  
RX (Receive): receives data  

So basically they allow communication, and the drone can receive commands from the Pi.

After that I wanted to add a 2x20 pin header so the Raspberry Pi can connect later. I didn’t know KiCad, but I found out that you just press “S” and search the component, and then I found `Conn_02x20_Odd_Even`.

Then I added JST-GH 3-pin connectors and after checking I found `Conn_01x03`.

But the KiCad workflow confused me at first!!! But then I understood that you first design the logic in the schematic and then define the physical PCB layout.

So I started drawing the Raspberry Pi and the flight controller:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM0NjcsInB1ciI6ImJsb2JfaWQifX0=--355f7659a28fb1dab273330fa54b4f99e3840817/image.png)

Then I continued adding the servo motor JST-GH and the 4 sensors, but I was so tired (0:20am) that I went to sleep:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM0NzAsInB1ciI6ImJsb2JfaWQifX0=--481dde09a012348a3ea3839faaab402b1d5ed9ec/image.png)

---

Next day: continuing PCB  
(Btw my Fusion 360 student pack got approved!!!)

I started adding the 4 connectors (JST) for the ToF sensors. They have 4 pins:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM3OTgsInB1ciI6ImJsb2JfaWQifX0=--f52e390b69d7fbfe44092d00c65187ccf2fc42f7/image.png)

After that I started wiring Raspberry Pi ↔ Flight Controller connections.  
I didn’t know how to connect them, so I searched and found:

- W = create wire  
- L = create label  

So I checked which pins are TX2/RX2/GND on the controller:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM3OTksInB1ciI6ImJsb2JfaWQifX0=--b561243d9e2c557ae7f10af38c31c26f741d1c02/image.png)

Then I added labels:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM4MDMsInB1ciI6ImJsb2JfaWQifX0=--519dfe40cd7304ad48a6079c0bbeecd769665dab/image.png)

After wiring the FC and Raspberry Pi, I continued with the 4 sensors.  
But then I realized I should combine them properly, so I researched and found that I should use I2C.

I2C allows multiple sensors to connect to one controller using only 2 wires. It avoids conflicts that would happen if each sensor had a separate connection.

At first I wasn’t sure how it worked, but then I understood it better:

Instead of directly asking each sensor, the controller communicates through a shared bus.

But then I still wasn’t sure, so I chose the TCA9548A, because:
- very common  
- 8 channels (very good)  
- well documented  

So I started integrating it:

After reading the datasheet I understood:

- SCL/SDA → Raspberry Pi I2C pins  
- GND → GND  
- VCC → 3.3V  
- pull-up resistor (10kΩ) for safety  

Then I connected A0/A1/A2 to GND to set the I2C address (0x70).

Then SCL/SDA of the sensors connect to channels 0–7.

But while doing that I noticed something important: the ToF sensors actually have 6 pins, not 4:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM4NTcsInB1ciI6ImJsb2JfaWQifX0=--653dc970f900b39ff86634d6b89ad670ed4e3928/image.png)

Pins:
- VCC → 3.3V  
- GND → GND  
- SDA → data  
- SCL → clock  
- XSHUT → enable/disable sensor  
- GPIO → not used  

So I updated everything and changed the connectors to 5–6 pin layouts.

Quick update:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM4NjYsInB1ciI6ImJsb2JfaWQifX0=--e4c52c506c356946a41bfcb4fb48a229bb52f927/image.png)

Then I connected:
- VCC + GND  
- XSHUT → 3.3V  
- SDA/SCL → I2C bus  

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM4NzMsInB1ciI6ImJsb2JfaWQifX0=--051580c5f663fb7825e4321657a3824ff9d23447/image.png)

After that I moved on to the servo motor.  
I wasn’t sure if I could power it directly from the Pi or not, so I searched and found out:

You should use an external 5V supply for better stability.

So I decided I need to design the full power system of the drone first. That will be harder, but I will need it anyway.

But since it was already late and I have a physics test tomorrow, I stopped here and will continue tomorrow with the power system.

---

Overall I’m really happy with the progress. I learned a LOT about KiCad, PCBs, I2C, and electronics in general. Tomorrow will be power supply day!!

### Recording Links

- https://lookout.hackclub.com/api/media/70a425be-f833-4f29-b735-de8990243e05/video.mp4

## Entry 16
- ID: 6662
- Author: Stefanos
- Created At: 2026-05-11T20:42:40Z

### Content

### 11. May: Designed the MP1584 Buck Converter for the Raspberry Pi!

Now I started and remembered during that day that I forgot to add the pullups for SCL and SDA, and I did the pullup for the RESET wrong, because it must always be connected in parallel to 3.3V. For the reset I can use the 10kΩ, but for SDA and SCL I will use 4.7kΩ because of the required I2C speed requirements. 

But then I thought that it didn't really make sense
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQyMDgsInB1ciI6ImJsb2JfaWQifX0=--fdfe5edd8e51577523df115f3f2360e1de9a18fb/image.png)

And then I also thought that I maybe should actually connect the reset pin to a GPIO pin on the Raspberry Pi so that if for some reason the I2C crashes, I can easily restart it.

So after reading the datasheet again, I agreed with myself that this would work, and so I decided to connect it to the GPIO pin 17. And after updating everything, it looked like this: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQyMTEsInB1ciI6ImJsb2JfaWQifX0=--9133cc18b2153120d753337ba55fccd9330c2ac3/image.png)

And after all of that, I had continued working on the power supply, which I was a bit afraid of because it was the MOST IMPORTANT THING for the drone PCB.

To start with, I searched up the battery to check which cables it has and the ampere/volt ect.

But after seeing the battery again, it confused me. There were 6 cables (I thought I would just need + and - T-T) 

But after googling, I found out that the two thick cables were for + and -, and the other 4 smaller cables were for measuring the capacity of the 3 individual cells(I will need that for percentage and low battery tracking).

So lastly I found out that the 2 cable types were an XT30 port, and for the 4 cables it was a JST-XHR-4P connector. So after finding that out, I implemented them into KiCad.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQyMjMsInB1ciI6ImJsb2JfaWQifX0=--b7b560254d7131dd7ea94d3adfd554fc2108a97d/image.png)

Then I started by searching how much power the Raspberry Pi needs, and I found out:
 > 5V power supply and typically works best with at least 2A or 2.5A

But then I was a bit shocked. 2-2.5A?!?! My battery only has 850mAh capacity??

So I searched up if that was ok and how I could fix that, and then I realized the voltage of the battery is toooo high for the Raspberry Pi. So I would need a buck converter! And then my problem would also be solved, because if you reduce the voltage, you gain more current/amps (flashbacks from my physics class ;) )

Sooo, I quickly searched for an SMD 5V buck converter and I found the MP1584EN. But after that, I realized that it wasn't only that single component, it requires many others. I wasn't sure if I should use a finished module or build one myself. So I searched up which other parts are needed, what's with the price, and how hard it would be to solder, and then I would decide.

* The Controller IC (MP1584EN): A Monolithic Power Systems (MPS) IC that handles switching at a high frequency (up to 1.5 MHz).
* External Coil Inductor: Crucial for energy storage in a switching regulator, working in conjunction with the IC.
* Trimming Potentiometer: A blue, small potentiometer used to adjust the output voltage, allowing user adjustment from 0.8V to nearly input voltage levels.
* Capacitors and Resistors: Input and output capacitors, along with feedback resistors, to manage stability and reduce output ripple.

How much do they cost together in SMD? About 2-3€, which is really fine. And after that, I decided to build the buck converter by myself because no risk, no fun, and I wanna learn sth new....

So then I started learning how this module works by finding some nice spots in the datasheet. But then I had the problem that the MP module wasn't in the KiCad library, so I had to manually import it. I got it from the KiCad GitHub repo and added it into KiCad. But I wasn't sure which net label I should use as a reference, as the only one I found was one that said 4.5V-28V input, and I wasn't sure if that would be fine.

But this should be fine, because after being on Reddit, I saw that if you calculate the voltage, you actually get 5.18V, which is perfect for the Raspberry Pi because it needs slightly more than 5V to run perfectly under load. And this was the 5V schematic for the circuit: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQzMDksInB1ciI6ImJsb2JfaWQifX0=--3052174985acf6ffb5857f766d9f677d9c7e669c/image.png)


Then I found out waht the pins of the MP1584 are for:
The chip itself has 8 pins:
- VIN: Input for the + of the battery.
- EN: Enable pin. If there is voltage on it, it runs, and if GND is connected, it stops.
- FREQ: Here you define how fast the chip switches with a resistor (R6).
- SW: The switch node where the power is toggled.
- BST: The bootstrap pin for the extra voltage boost.

But finally, after like 1h, I understood how the process of the chip and the convert worked. The MP1584 lets the voltage through to the inductor (coil), and there it switches the flow. The diode keeps the current flowing so that the energy is saved in the inductor, and this voltage is going to the Raspberry Pi with 5V. The MP chip decides how fast it has to "cut the flow" to get exactly 5V at the end.

Additionally, you can define that there is exactly 5V as output by just changing R1 and R2. The formula for calculating that is:

$V_{OUT} = 0.8 \cdot (1 + \frac{R1}{R2})$

The 0.8V is a reference value for the chip so that it knows whether it has to switch faster or slower. And lastly, there are capacitors for making the power smoother so that it's perfect.

That was the basics of the chip, and then I started drawing that in KiCad.

Buuut while doing that, the problem was that I couldn't find capacitors. But then I saw online that you have to type "C_small" to find one (why?!?!).

But then I had to place the GND tag, but then (AGAIN) I wasn't completely sure if I could use the same GND like I use for the internal Raspberry Pi. But after checking, you can and should combine the GND into one system, so I did it.

But then I was confused. There was the ground symbol that I knew, but also another symbol like a triangle. So after searching, I found out that at the positions with the 3 lines (GNDREF), tons of power is flowing, and at the "normal" triangle GND, only small signal currents flow. Both are connected, but I decided to separate them so that in the design process I don't forget to make thick and large copper plates for the power GND.

After drawing the first half I got this: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQzNjQsInB1ciI6ImJsb2JfaWQifX0=--1c44b44c9719fbfad87298119faba85d1e1e2ae7/image.png)

I then wanted to make the EN pin but didn't know how to connect it properly. But then I realized that I had already combined the EN with power from VCC because I had connected it with the VOn net. And after adding the voltage divider resistors R4 and R5, I would get exactly 2.2V, which is perfect for the EN pin.

Then I continued on the COMP pin, which is necessary for the control of the correct voltage. There I have to use a resistor (R3) for defining how fast the chip is allowed to react to changes. The C3 acts like a shock absorber. Normally you also use the C6 capacitor, but the datasheet mentions it is only used if the output capacitor is an old electrolytic capacitor (Elko). Since I am using a modern Ceramic one, I don't need the C6!
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQzNzMsInB1ciI6ImJsb2JfaWQifX0=--9c56b6759c0d55087323256509745646cce175b8/image.png)

Next I continued on the BST, SW, and FB pins: They are there for actually dropping the voltage. The SW pin is like a crazy insane fast light switch that toggles the flow of current through a diode, which only lets electricity flow one way to the inductor. The FB gets the feedback so that it can adjust how fast the switch should be. But so that the chip can pump so fast, it actually needs a higher voltage than the battery. So the capacitor C4 gives the chip an extra boost so the internal switch can work (BST pin).

For the diode I used the B340 Schottky diode because the datasheet recommends it and it can handle up to 40V and 3A. And after also adding the inductor L1 with 15uH, it looked like this: 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQzOTAsInB1ciI6ImJsb2JfaWQifX0=--f81323ad2cc40a43898d8f79add17ed8520b4f17/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQzOTEsInB1ciI6ImJsb2JfaWQifX0=--534bc17e6c80468873f2e5f8737042d47e1a743b/image.png)

And after I finished, it looked like this: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ0MTEsInB1ciI6ImJsb2JfaWQifX0=--c58c3b9ed8b494ba93a3d5ed386abc235a423a82/image.png)

Lastly, I tidied it up a bit so that it is more compact and better to read:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ0MjEsInB1ciI6ImJsb2JfaWQifX0=--7e45151505fdf16ee150418378160a4161b7a212/image.png)

Happy with today's progress! Made the converter. Huge progress on the PCB. TMW will be the connection to the Raspberry Pi!

### Recording Links

- https://lookout.hackclub.com/api/media/1f55d780-5f31-488e-bcbf-edad80969dc1/video.mp4

## Entry 17
- ID: 6842
- Author: Stefanos
- Created At: 2026-05-12T21:17:28Z

### Content

### 12. May: Finished the Schematics of the PCB: charging mode etc!

I started by adding GND to the battery because I forgot it last time, and then I added a parallel connection for the Raspberry Pi and the servo motor. But I didn’t know how to connect the power to the Pi, so after searching I found 2 options:

1. over Micro-USB  
2. connect the power supply + to the 5V pin (pin 2 or 4) and GND to any GND pin on the Raspberry Pi, but pin 6 is the recommended one  

I decided to use the pins because I am building the PCB directly for the Pi pins and mounting it there. So after fixing the GND and power for the Raspberry Pi it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ4MzUsInB1ciI6ImJsb2JfaWQifX0=--57bd63f042b37b4384cdfa964456a0224a60ff4f/image.png)

And then I wanted to add the power for the servo and the connection to the Raspberry Pi, so I first created the GPIO pin connection to the Raspberry Pi.

After googling I found out that you should use GPIO18 because it supports PWM, which is needed for controlling servo motors smoothly. That’s why I quickly made the connection.

But then after starting the 5V connection I remembered that the chip can maximally produce 3A, AND THE RASPBERRY PI already needs around 2A under high load, and sometimes the servo can also need up to 1A during startup spikes. So it would be VERY close and I was afraid that my chip could melt, so I decided to add a capacitor for extra current buffering so that voltage drops and current spikes don’t melt the system.

After searching online I found out that radial electrolytic capacitors are the best for this because they can store a lot of energy in a very small space, which is PERFECT for my drone.

Then I also found out that the capacitor voltage rating should be at least double the system voltage for safety and reliability, so around 10–15V.

After adding the values into a calculator with an example of 1000µF it calculated:

(and sorry, during that time till 20:22 I had my English project open — didn’t work on it during recording though, just forgot to close it. Sorry!!)

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ4NDAsInB1ciI6ImJsb2JfaWQifX0=--c6e31b4ef650b9baf91dd545ceb42a51d814ceaf/image.png)

And then I got 0.1125 Joules, and after calculating how much current it could provide and dividing it by 1–5ms (because servos create very short but high startup current spikes during the first milliseconds before the motor fully spins), I got values from max 16A down to around 3.2A depending on the discharge time, WHICH IS PERFECT for me because now the servo will probably not melt my chip.

And after everything was clear I added that to the circuit.

After adding that it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ4NDgsInB1ciI6ImJsb2JfaWQifX0=--31ef21ab0e0afbb9851c1a16ec26cf7a5e60d83a/image.png)

Now only the power connection to the FC was missing. So I decided to power the FC directly from the battery (throu the PCB) because it has an inbuilt buck converter. That’s why I searched for an XT30 connector to connect the power cable.

And after building that it looked like that!! Awesome:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ4NTUsInB1ciI6ImJsb2JfaWQifX0=--fcc6cde2062116557aca23efb2bc6a5dbd5cdbd9/image.png)

Lastly for this session I wanted to finish the schematics, so I wanted to add the pogo pins so the batteries can also be charged.

Therefore I first thought of a principle so everything works properly:

I will have 2 different pogo pin types:
- 2 thick ones for the main power  
- 4 smaller ones for battery information (Cell 1, Cell 2, Cell 3, and GND)  

Then I should have a diode directly after the power pogo pin so that if I accidentally touch it my finger doesn’t get cooked etc.

Then I also wanted to use something that closes the circuit during charging so that the Raspberry Pi, servo, and FC aren’t powered while charging, because otherwise battery measurements and charging could become unstable.

So I started by first adding the pogo pins and then directly connecting the 4 status pins:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ5NDgsInB1ciI6ImJsb2JfaWQifX0=--031c63b30ee620dec36c3169d5e06fbc15dc1f70/image.png)

Then I wanted to add the circuit breaker system, and I found out that I would need a High-Side Switch circuit with a P-Channel MOSFET because:

It works by allowing power through when no charging voltage is on it. Sooo, the Raspberry Pi, servo, and FC get power. But once the pogo pins connect and charging starts, the MOSFET gate changes state and disconnects the system power from the battery.

After that I only had to find which exact model I should use.

Very important requirements for me were:
- 20–30A current handling  
- around 30V 
- 10–20mΩ 

About 20–30A because:
- the FC can take max ~15A  
- Raspberry Pi + servo can together take ~4A  
- and I wanted extra safety margin  

About 30V because:
- you should generally use about double the operating voltage  
- 11.1V ×2 + safety buffer  

And the resistance should be as low as possible so I don’t lose too much voltage and generate unnecessary heat.

With these criteria I found 2 chips:
- AO4407A  
- AOD4185  

The problem with the AO4407A was that it only supported around -12A, so it was too weak. That left the AOD4185, which actually had slightly overkill specs:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ5NTcsInB1ciI6ImJsb2JfaWQifX0=--64262d20f4ec1540cc0afd971bf454f83198407d/image.png)

But I decided to use the AOD4185 because I probably won’t run into any problems with it.

Then I added it into KiCad.

Then I wanted to wire everything up, but after seeing the datasheet I first didn’t understand anything:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ5NTgsInB1ciI6ImJsb2JfaWQifX0=--5be9f114e8fce74801bcafc02a7ad0e45ba61b8b/image.png)

But after a bit of time I finally understood how it worked.

I first had to delete the connection between VCC and J5 Pin 1, and then route the power through the MOSFET drain to VCC.

After that the plus from the pogo pins gets connected to pin 3 of the AOD4185.

There I also had to use a pull-down resistor so that when the drone is NOT connected to the pogo pins, the gate is connected to GND and the module stays activated, allowing power through normally.

Then after managing the power lock for the charging system so that charging works good:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ5NjAsInB1ciI6ImJsb2JfaWQifX0=--bb30e3c1fc397e57ce17aa105ff23b3cf7fbafb0/image.png)

I continued on the diode protection for the power pogo pins so that I don’t get shocked or burn my PCB.

I decided to use a Schottky diode because they have very low forward voltage drop and are fast, which makes them good for power protection.

After a bit of searching I decided to use the SK1045 because it can handle 10A, which is pretty good for the landing process.

But then I thought:
What if something metallic or finger ect.  touches the pogo pins during mid-flight while the motors are active and spikes of 30–40A appear?

SO I HAD THE IDEA TO USE A 100nF CAPACITOR as a filter for extremely short touches, and additionally use a 15V Zener diode that clamps voltage spikes and ESD events.

Because indoor environments can create a lot of static electricity (like carpets etc.), this should protect the MOSFET gate and the system.
So I started implementing my LOOOOOOONG thought into KiCad.

But during that I noticed that I forgot to connect the power correctly.

And while fixing it I realized that I mixed up the MOSFET pins: pin 3 was actually the input and I accidentally placed the diode like 10 times on the wrong side etc.

After that I also added the 15V Zener diode and the 100nF capacitor:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ5NjYsInB1ciI6ImJsb2JfaWQifX0=--df0fa99a913c422f48c380bb07a713902d3cc619/image.png)

And after that process it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ5NjcsInB1ciI6ImJsb2JfaWQifX0=--142a12c8dda3ea80b181c4a2a47276902697371c/image.png)

And after a bit of tidying it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ5NjgsInB1ciI6ImJsb2JfaWQifX0=--8dace3567e450d8dcfb9617336dc17c99f38edcd/image.png)

AND..... that was it for the session. It’s 11PM now and I gotta sleep.

BUT I’m VERY happy with the progress today. I’ll send it into Slack for checking again, and tomorrow will be routing/tracing and finishing the PCB for the drone!!!11

### Recording Links

- https://lookout.hackclub.com/api/media/92c6ca23-f5c4-4fb1-9210-15252b661946/video.mp4

## Entry 18
- ID: 6986
- Author: Stefanos
- Created At: 2026-05-13T20:39:35Z

### Content

### 13. May: Finished the schematics for my drone PCB!

Added a not_conn by pressing q (thx @anvar), after that it looked like this: 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTUyNjgsInB1ciI6ImJsb2JfaWQifX0=--ab40a410e9923f3ef7742b225da0d510b4c6531d/image.png)

And then I thought that it would be smart to add the battery percentage measurement also in the drone, so that the drone can automatically land if the battery is too low.

So that I can start that, I firstly had to think how I make sure that I don't have conflicts because the 4 pins from the battery have to also connect to the landing station.

I had the idea to connect the cells with the GPIO pins of the Raspberry Pi, but the problem was that the GPIO pins only can handle up to 3.3V and the battery will be max a pin at 11V, which is almost 4x more. 

So I can fix that problem, I would need a voltage divider so that I can get the voltage for every pin under 3.3V, and after that I would need an ADC chip that can translate the voltage into digital signals with 0s and 1s so that the GPIO pins can read that.
And after finding out how much voltage the pins can maximally have:

- Pin 1: GND
- Pin 2: Cell 1 (ca. 3.7V - 4.2V)
- Pin 3: Cell 2 (ca. 7.4V - 8.4V)
- Pin 4: Cell 3 / Total (ca. 11.1V - 12.6V)

After that I had to calculate how much resistance the resistors should have...
And then I found out that I would need 2 resistors per pin for the voltage reduction, and it would look like this (with the formula from the DigiKey calculator):

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTUyODIsInB1ciI6ImJsb2JfaWQifX0=--98e2ad1b32950f7e552f22f09ec8a8248be0176b/image.png)

And after calculating for everyone I got these values:

Pin 2: max 4.2V
- R1: 10kΩ
- R2: 33kΩ
- Output: 3.22V

Pin 3:
- R1: 10kΩ
- R2: 5.6kΩ
- Output: 3.01V

Pin 4: (Total)
- R1: 10kΩ
- R2: 3.3kΩ
- Output: 3.12V

Lastly I had to find the correct ADC and I decided on the ADS1115.
How it works:
1. Converting the voltage into digital numbers.
2. It has not like cheap ones only 8 or 10 bit, it's a 16-bit converter. That means it divided its measurement in ranges of 2^16 (65,536) tiny steps, so that it allows to see the smallest changes like 3.5 and 3.51.
3. It is built for I2C, so that I can connect all 3 pins to the chip. 

So that I firstly started by implementing the chip into KiCad.
Then I branched off and made another way from the 4 data cables which were going to the pogo pins:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTUyODYsInB1ciI6ImJsb2JfaWQifX0=--097b9b15292ec914daaa41f01a2f3383d465e13c/image.png)

And after labeling them I started implementing the resistors for C1:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTUyODksInB1ciI6ImJsb2JfaWQifX0=--a9ea021b759999882bdf20560bc64ae4cc7659e4/image.png)

And then continued with every other:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTUyOTAsInB1ciI6ImJsb2JfaWQifX0=--05ae80825c508efc141bba298e31e916b2bc91be/image.png)

After that I connected them to the ADS1115 chip: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTUyOTEsInB1ciI6ImJsb2JfaWQifX0=--42cd4984f5a4e99f4e64c05922735fb5058d9978/image.png)

After that I wanted to make the connection to the Raspberry Pi but I noticed that I already used the SCL and SDA pins on the Raspberry Pi. But luckily I found out that you can connect the I2C buses with the same pins as long as they don't have the same address.

So after checking again which address both have, I found out that the:
- ToF:  0x48
- Battery:  0x49 (if ADDR connected to VCC)

So everything was fine and after also connecting the SCL/SDA pins it looked like this: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTUzMDAsInB1ciI6ImJsb2JfaWQifX0=--ce2f9ba37e428961504022d60f6323819155307e/image.png)

And after also making the VDD connection with 3.3V with a 100nF capacitor that goes to GND, and after doing that I was finished:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTUzMDMsInB1ciI6ImJsb2JfaWQifX0=--25293630ff627e9d857a8b6e89cb5498e2cbe4a9/image.png)

And after all, my schematics looked like that:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTUzMDUsInB1ciI6ImJsb2JfaWQifX0=--fc254400ffd0e1ed100c6c179ebc568ecb181def/image.png)

Happy with progress! Finished the drone schematics. TMW will be the routing and happy with the progress!

### Recording Links

- https://lookout.hackclub.com/api/media/4970d584-1c17-4f44-832b-c7d77c9b153a/video.mp4

## Entry 19
- ID: 7166
- Author: Stefanos
- Created At: 2026-05-14T21:13:27Z

### Content

### 14. May: Fixing schematics problems/errors and placing the components on the PCB!

And after getting feedback again I actually had some issues which would cause that the drone wouldn't start or some parts wouldn't run etc (T-T)

1. MOSFET Q1 AOD4185:
- R10 has to be connected to the gate Q1 (pin 1)
- I would need another 100k Pull Down resistor that is directly from the gate to GND so that the MOSFET during flight is still turned on, whether the pogo pins are accidentally touched etc.

So I fixed that adding the resistor R10 between J7 pin 1 and Gate from Q1 and then I also added the R18 a 100k pull down resistor to the Q1 pin 1:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU0MTEsInB1ciI6ImJsb2JfaWQifX0=--d26b544803b7b17aae7d534ae7c1730bebca1cbc/image.png)

2. I also had the problem that I connected the reset with the GPIO, but the pull up resistor shouldn't be connected to GND, it should be connected to 3.3V.

and after checking it in the datasheet he was right:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU0MTIsInB1ciI6ImJsb2JfaWQifX0=--3243f5aa113fe093347b945598ad56da6b1fc4ec/image.png)

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU0MjAsInB1ciI6ImJsb2JfaWQifX0=--38a53ef9aa3794a1d423e60955fc8c4e67f82b77/image.png)

and after fixing that issue it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU0MjMsInB1ciI6ImJsb2JfaWQifX0=--c4913e7258cb264fedf589c6c9771a49a2db7916/image.png)

3. I accidentally put the reset pin at pin 17 at the Raspberry Pi Zero 2 W which is the 3.3V pin but not a GPIO pin, which is what I needed to restart the bus over the code. So I decided to move the reset pin to pin 15 (GPIO 22).

4. I accidentally added a resistor at the battery percentage although it should be a capacitor:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU0MzAsInB1ciI6ImJsb2JfaWQifX0=--ae86548c5e3cf1fc2d0bd7abce9939be141a3827/image.png)

So after changing the resistor to a capacitor and making it 100nF it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU0MzEsInB1ciI6ImJsb2JfaWQifX0=--6953a147356bfea1d73a0cc71da20713c71a2afd/image.png)

and the updated schematics looked pretty good now and I was confident to route it now (thou a bit scared.....)

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU0MzIsInB1ciI6ImJsb2JfaWQifX0=--940f25d3b47099008a8b8dc023212c5767defedf/image.png)

Sooo after a couple of deep breaths I continued on the routing, but I didn't even know how it works to open the routing thingy and how to route etc, so I stopped the timelapse to watch some videos to understand the process of it and then I would start the routing.

So after I found out that I opened the PCB editor then I pressed F8 to add all the components, so that I had to go back to the schematics editor and add a footprint to all parts that hadn't a footprint.

I did this, and after I opened the footprint assignments editor I saw that I had to add a footprint to 40 parts (T-T) that will take a LOOOONG time.

So I started with all the capacitors but that was tough to find the correct ones.

(I forgot to stop the lapse for 4 min I think sorry please DONT count it or so it's not fraud!! pls)

I used for the resistors and capacitors the size 0603 because you can hand solder it but is still small but not too small so that you can solder it easy. Only for the C1 and C4 I decided to use 0805 because these have to handle higher voltage and current, the larger size prevents them from overheating.

I decided to use for every part JST-GH (1.25mm) connectors because they are vibration stable and easy for debugging.

For the power cables I used the XT30 connectors because they can handle up to 30A but are lightweight thou.

For the pogo pins I decided to use copper pads with 2mm diameter for soldering

For the 2 power pads I decided to use also 2mm pads but in the design I'll make them double the size so that they can handle more power.

For the chips I used them from the SOIC & TSSOP packages the smd ones.

and after all it looked like this; after importing them like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU0NTUsInB1ciI6ImJsb2JfaWQifX0=--0634cccc8d05dccd641cdc75f2c912bc21596ed8/image.png)

and after that I had to draw the size and form of the PCB. I did that by making an outline of 2mm from the walls and then cut out the piece I would need.
but then I also had to draw the position of the FC but I wasn't sure where the front is.

and after drawing the PCB size, I also drew the position of the FC and the center of the mounting holes:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU0NzYsInB1ciI6ImJsb2JfaWQifX0=--c16ff1fed7c4fc2a0351399e15146ceca1d33c8b/image.png)

and I decided to make the holes for the screws so that they will hold the FC and the PCB, so that the screw can perfectly go through it, but then I saw that the length was wrong: 24.5, so I built the rectangle again with 0.5mm more on each side.

and after fixing that it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU0ODIsInB1ciI6ImJsb2JfaWQifX0=--c230a4ad26c20bd5f3d7aeb647a3fbe6059c714d/image.png)

and after removing the unnecessary lines, only the holes for the PCB were left.

but I wasn't sure if the 4 holes would hold the PCB.

But I decided not to make more holes but to make support pads that help the PCB not vibrate.

then I firstly placed the connector in the correct place so that I can start with the routing soon and tidy it up a bit.

I placed the J11 and J8 for the sensors in the front, for the down- and front-looking sensor, and I also added the servomotor connector to the front because it's at the front.

Next I also moved the J9 to the right side for the right sensor and the J10 to the left side.

Then I also added the J2, which is for the connection between the Pi and FC, to the left side because around there are also the pins from the FC to connect.

Lastly I also positioned it, but when I wanted to connect the XT30 cable, because exactly there where I wanted to add it, the capacitor of the FC was overhanging and was blocking the whole place for the 3 battery connectors.

1. Option would be to add the capacitor on my PCB.

2. Option would be to solder it so that it's not overhanging and is facing straight up.

And I decided to add the capacitor to my PCB so that it will not vibrate and accidentally break, and I think that this is the best, cleanest, and nicest solution, soooo I jumped back to the schematics and added it, and after adding it to the circuit it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU1NzgsInB1ciI6ImJsb2JfaWQifX0=--24a6385150bb26160d1ae4b6d0c219c4857d2df1/image.png)

and then I also updated the PCB:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU1ODIsInB1ciI6ImJsb2JfaWQifX0=--9c95548ddc0cc8ec027ca475f465b42c1c2762ba/image.png)

and after that I optimized the placement of the connectors so that they were perfect:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU1ODYsInB1ciI6ImJsb2JfaWQifX0=--608a0d98d883e43d67d6c4fed0841c305f1c43d0/image.png)

after that I started positioning the components, but for that I firstly had to pay attention to a lot of things while placing them.

but before I started I roughly brought all components to their places:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU1ODksInB1ciI6ImJsb2JfaWQifX0=--52b6e04e1b35fccf6e0995d441a7b228ebaa392f/image.png)

but while I was doing the Raspberry Pi power supply, the many texts made it impossible to read and connect them properly.

After Going to the settings and disable them It looked much cleaner

and after that my Raspberry Pi and servo motor power was finished:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2MTUsInB1ciI6ImJsb2JfaWQifX0=--3acc8b6d89bb5dcfae6702147eac0d7af239b5e0/image.png)

but then I read in the datasheet that the diode must be as close as possible to pin 1, so I switched the position with the L1:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2MTYsInB1ciI6ImJsb2JfaWQifX0=--ff0993bfb8182887851bf705b670b1d887a4eb49/image.png)

I also took some inspiration and tips from the datasheet  for optimal positioning. For that I'll connect the R9 in the 3rd layer with an extra power wire because now it's very hard to get to it, and also for the R4 connection I'll use the 4th layer to connect it to VCC/VIN, and after checking in 3D it looked pretty good:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2MjAsInB1ciI6ImJsb2JfaWQifX0=--1c31b0adf663f6edfccb7deecf49c9133cdbbc67/image.png)

So I continued with the battery percent:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2MjExInB1ciI6ImJsb2JfaWQifX0=--2b1a07146bf16e43f31ccfe66e22e0842f098d68/image.png)

and then I noticed that I forgot once to stop the timer and then when I wanted to stop the timer again I actually started it, so I lost like 30min of work T-T (in time).

but with the U3 I had the problem that the C2, C1, and C3 were always crossing with GND, which would make it much harder to connect them to the other pins, but lastly I found a very nice solution:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2MzksInB1ciI6ImJsb2JfaWQifX0=--1a732cc5c5e7b2199fb10aacebe321b0ede23a53/image.png)

After that I continued with the LiPo battery and pogo pins:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2NDAsInB1ciI6ImJsb2JfaWQifX0=--6d38c8af0234ce8d8f9e728544848d2f6d674cf6/image.png)

and actually this went pretty fast and looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2NDEsInB1ciI6ImJsb2JfaWQifX0=--069b1f7588a7041927c67787c9727bf0f8685768/image.png)

I also made the texts for the parts that I already placed nicer so that it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2NDMsInB1ciI6ImJsb2JfaWQifX0=--7592669e3b4656334091ff8280a8a5045ba7dad3/image.png)

and lastly I centered the U1, positioned the resistors and capacitor, and I was finished with positioning the components.

Here is the 3D model and the PCB parts:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2NDcsInB1ciI6ImJsb2JfaWQifX0=--edb8c56085f0f8ebe62b949f2a87af61e57d2abc/image.png)

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2NDgsInB1ciI6ImJsb2JfaWQifX0=--9d30cbb07aca51b3ebcc473d1ffb40a23c72225d/image.png)

Pretty happy with the progress, fixed the last schematic bugs, learned how to import the schematics into the PCB editor and place the components, and did that. Next will be routing and hopefully finishing the PCB!!

### Recording Links

- https://lookout.hackclub.com/api/media/d45459ca-fa8b-481c-a3fd-95bd56824789/video.mp4

## Entry 20
- ID: 7331
- Author: Stefanos
- Created At: 2026-05-15T21:44:32Z

### Content

### 15. May: Fixed last issue with schematics and started the routing!

I was placing the parts last time, but then I saw that the pogo pins were actually male pins 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU4ODAsInB1ciI6ImJsb2JfaWQifX0=--34393d637043a6a345057260f8fb04bdc856f05e/image.png)

but I wanted to have like copper plates or something like that to solder the things on it, and they should be on the other side.

But then I had a better idea: for the 4 data cables, I could use the JST-GH adapter again, but for the power, I would use soldering pads with a diameter of 3mm.

So I changed the J12 to a JST-GH with 4x1 pins

But then while searching for the soldering pads, I had the idea that I could also just use XT30 connectors for the voltage horizontally, which I then also did, so that I could very easily remove the PCB Raspberry Pi, FC from the drone and debug, which is PERRFECT.

And after saving, opening the PCB, and loading the 3D view it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU4OTAsInB1ciI6ImJsb2JfaWQifX0=--d03a068bd0603e8d59579899682f8e2017a24cea/image.png)

Now I only had to figure out how to place them on the other side, and after finding out that you have to press F to flip, it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU4OTEsInB1ciI6ImJsb2JfaWQifX0=--20c635726be3bd9e513b39b91625eec62fc23096/image.png)

But then I quickly had a tough problem, the J7 pogo pins control and the J17 place was hard to find the perfect place.
But then I had a good idea, I could rotate some parts to 45 degrees and my PCB would have much more space and the cable could be much, much better: so after a bit of trying, changing the position of the capacitor C8, and rotating the U3 block and the U2 block, it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU5MDMsInB1ciI6ImJsb2JfaWQifX0=--aea820b2ee4f5c4347b9ac6e19cec3e1ddb6547e/image.png)

And then I also got some feedback on my circuit from someone who knows A LOOOOOT about electronics, and he said that it looks really good, but I had one critical thing: The servo motor:
The 1000nF capacitor is good but not enough and risky to shut down my Raspberry Pi, etc. And because the way to the servo is about 10 cm long, it would be even riskier, so he said that I should additionally use a 100uF before the C5 capacitor and then a 100nF capacitor, and close before the 5V pin from where the part gets the voltage, to also set a ferrite bead (this model Murata BLM21SN601SN1L) because it can handle up to 8.5 A and a resistance from 600 at 100MHz, which should be perfect for the servo noise. So I switched back to the schematics and added those things, and after I inserted it into the schematics, it looked like this:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU5NDksInB1ciI6ImJsb2JfaWQifX0=--73321cfa0889639bb3f85c7ed285b634bd78745d/image.png)

And after giving it the corresponding footprint, I saved and went back to the PCB design to place them. So I quickly changed it so it looked like that.

But then I understood that I placed the 1000uF C5 wrong, it should be as close as possible to the input voltage point
so it looked like that after fixing:

And after finding the perfect place and fixing the order of the components, it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU5NTcsInB1ciI6ImJsb2JfaWQifX0=--a4c517dc9bd400eb9ff5442375d0ae44bd0b7655/image.png)

And after all my PCB placing was finished!!!!! And now the routing begun.

Then I first gave the 4 layers different names: F.Cu: TOP-SIGNALS, In1.Cu: GND-PLANE, In2.Cu: POWER-PLANE and B.Cu: DOWN-SIGNALS

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU5NjYsInB1ciI6ImJsb2JfaWQifX0=--e6c638053214925a7f6a0df5ef0d82689eaef3fb/image.png)

Then I made Design rules:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU5NjgsInB1ciI6ImJsb2JfaWQifX0=--3b83d4d11c9a861734a7223f36dadc10bc409119/image.png)

And after also making the assignments, I started with the connection for the battery, and after placing the first things, I quickly noticed that I did something wrong:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU5OTgsInB1ciI6ImJsb2JfaWQifX0=--657c76ed2fa746fc0facbc9a47b5677f1dccd611/image.png)

The nets at the resistor were too big so that it was at risk of a short circuit:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU5OTksInB1ciI6ImJsb2JfaWQifX0=--38c91a3cc17302d1ff50c9f7845723394bef3532/image.png)

And lastly, I added Copper Pours and made it even cleaner through it:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYwMDYsInB1ciI6ImJsb2JfaWQifX0=--63ccb3224e1fff62a00e7008992e1f77437202ed/image.png)

And after connecting the other parts from this, it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYwMTYsInB1ciI6ImJsb2JfaWQifX0=--16f6f23d3b2ad315554c6f7b53d279889fa2eb4d/image.png)

Lastly in that part of the PCB, I connected the GND with the GND plate 

And after selecting the board I pressed B and filled the net and directly all other GND parts connected and it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYwMTcsInB1ciI6ImJsb2JfaWQifX0=--f1d5173b338ca35e819f34f66fd01ae13e410c4c/image.png)

After finishing the most important part, I continued on the battery status pins:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYwMTksInB1ciI6ImJsb2JfaWQifX0=--2bf47b08ca303db994a4ab9088a0872d85672495/image.png)

Therefore I used the default tracks 0.2mm for the signals lines and for 3.3V and GND 0.3mm, and also for Power, but for the capacitor, I used 0.3mm because there is more power, and after designing that, it looked like this:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYwMjMsInB1ciI6ImJsb2JfaWQifX0=--f56c5df0f5a6932a2319d85650ea0ca9e5b71e9e/image.png)

During that process, I also placed VIAS, so that the GND can go to the GND plate, but the problem was that the VIAS didn't connect to the GND:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYwMjUsInB1ciI6ImJsb2JfaWQifX0=--b37009c71055bf3f4090715eaeb11b2878b5b702/image.png)

But I tried for about 30 min to find a solution and I didn't find one. Soo I'm gonna sleep now and this is how the PCB looks today:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYwMjgsInB1ciI6ImJsb2JfaWQifX0=--f6265d816e6ded97fc9054147c1d1d34664b8def/image.png)

Happy with the progress today, fixed the last issues with the schematics and started the routing of the components!

### Recording Links

- https://lookout.hackclub.com/api/media/a658e64d-1b82-4241-87b3-47b247f468f2/video.mp4

## Entry 21
- ID: 7680
- Author: Stefanos
- Created At: 2026-05-17T20:27:52Z

### Content

### 16-17 May: Fixing last issues in the drone schematics!

I wanted to fix the via connections to the GND plane now, and after searching online a bit, I found out that you have to open the GND plane properties and change the pad connection from thermal reliefs to solid so that it also connects if it is near a chip, etc.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYxOTUsInB1ciI6ImJsb2JfaWQifX0=--b5e60b61a872e7efa6fc5a4220bf5cfdd38fb60d/image.png)

But unfortunately, that didn't fix my problem. However, after taking a second look, I saw that the clearance zone was very high at 0.5mm, and I changed it to 0.2mm because I read that this is standard.

But that also didn't do anything, even after re-rendering with B.

I just didn't understand why it didn't work, why??? T-T

But then I saw that it actually worked and was connected! Yes, it was fine the whole time, I just didn't know that it looked like that. I thought it should have those little legs.

But never mind. I continued connecting the pogo pins, data cable, and battery with the J3 battery status pins. Because the connector to the pogo pins was on the bottom layer, I had to make vias to the bottom and connect it with the status pogo pin connector. Then I saw that I had forgotten to connect the GND pin with the GND plane through a via, so I quickly changed it.

I also decided to add the vias for the connection with J15 on the bottom pogo connector. I paid attention to placing them at the correct height so that the routing would be easier later.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYyMDEsInB1ciI6ImJsb2JfaWQifX0=--724613605fe50ccd7ad6e61d390f51ded6638ed3/image.png)

And after connecting the 4 vias with the connector, it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYyMDIsInB1ciI6ImJsb2JfaWQifX0=--79525cda2dbd4be9df81a3b3caee7329396aba7a/image.png)

Lastly, I only had to connect the GND with the GND plane, so it ended up looking like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYyMDQsInB1ciI6ImJsb2JfaWQifX0=--71f768d0cd995af94a34fa1fe6bdd95c612be865/image.png)

Next, I continued on this part, which was also the most important and the hardest because the components have to be as close as possible to each other. FOR THIS ONE, I HAVE TO FOLLOW THE exact description from the datasheet.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYyMDcsInB1ciI6ImJsb2JfaWQifX0=--3268e36b2c151c8936b1c26afa107ab6bed85579/image.png)

I firstly started by making the huge connection between VCC and the VCC input of the buck converter.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYyMDksInB1ciI6ImJsb2JfaWQifX0=--a9477843760a236cc61f1263857584a58237d33f/image.png)

I made the VCC connection into the buck converter and the drone directly to the XT30 over the C8 capacitor so that I was finished with that step.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYyMTMsInB1ciI6ImJsb2JfaWQifX0=--4b4a2d83e740a3453130794dc33a1672435e5ae6/image.png)

AND I NOTICED A HUUUUUUUUUGGGGGGGGGGEEEE mistake that cost me 3-4 hours of work!
Here comes the ultra-long description why:

So I had to delete D1 because it has a small resistance that would cause a voltage drop of -0.5V. I thought I could change it software-wise, but this wouldn't work because the values from the cells would be wrong and the risk would be too high that the battery would explode. SO I needed something like a diode, but with almost no resistance.

And then I stopped for the day because I was at my limits. Almost the whole work I did on placing and routing was for nothing, and I was very afraid that there would be many more errors, etc., and that I would destroy my drone. After asking in Slack, nobody could really help me.

But then, I got very clear feedback that my PCB would not turn on and would catch fire (not so good).

First, I had a problem in my charging/power circuit which I wanted to solve, but then I saw what kind of bullshit I made. J12 pin 5 was completely useless and Q3 too, SO I decided to remove them. Because they wouldn't do anything special, after removing them it looked like this:

And after thinking logically about it, it was perfect and 10x easier and correct now, here it is:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY2MTQsInB1ciI6ImJsb2JfaWQifX0=--3e7033454c41bda8a2d88155c97aa2872708a680/image.png)

During flight: J5 pin 1 can go normally through Q1 because the input is at the Source, and Drain is VCC. The other part's pin 1 allows it to go through because it is connected through GND, so that works perfectly. Q2 blocks itself, so that during flight, if you touch the pogo pins, the battery doesn't get cooked. This is the perfect system! After that, I wanted to be completely sure, so I decided to simulate it in KiCad.

Therefore, I had to find the SPICE file for the AOD4185. After finding a PDF that had 108 PAGES (!!!), I found the correct part and created a new text file so that I could save that section. Then I had to double-click on the MOSFETs, add the TXT files to them, and also change the pin layout because it was different in the TXT file. After that, I added virtual voltage sources. But after running the simulatio... ERROR, and over and over I tried for sooooo lnog to fix that but it didn´t work, tired to export it to other simulator, but they weren't that good and I didn´t knew what to do, but then I managed to run one. But it came out, that my system for charging/battery-switch didn´t fork, SO I tried finding the solution, but I kept failing...

After that, I took a walk outside and thought about whether I could even build this drone, etc., and fell into a rabbit hole... But then I thought the thing that is holding me back the most right now is the electronics for the landing station. So I decided to build the landing station, but NOT to make the drone charge through the landing station automatically. You will just have a button or switch built into the drone to turn it on and off and then charge the battery manually. This saves me a lot of time to finish this project and also raises my chances to attend the in-person event in Shenzhen! (Who knows, maybe I'll do the automatic charging in V2 of the project). But I am happy with my decision. And I set a personal deadline for myself: 1 WEEK! It's tough because I have to finish the PCB, make the poster, write the code, and do the 3D CAD of the landing station, but that was the ONLY solution for me to attend the in-person event. So I switched right back and deleted the parts for the landing station electronics.

Excluding J7, J12, and their electronics. After that, it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY2ODUsInB1ciI6ImJsb2JfaWQifX0=--e5e72f424ac686c3bf4e5969d863d92b588be99a/image.png)

But then I had to think of a switch to turn the drone on and off for charging, but also for saving energy, etc.

I wanted to add a switch like this on the side of the drone:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY2ODgsInB1ciI6ImJsb2JfaWQifX0=--4c0c6bb1943684c626193d24b92891831d73bcb6/image.png)

But I had to search up how to add it, etc.

SO after searching online, I found an idea on how to do this. Because if I would put the switch in series, it would melt and the whole circuit would not work. For switching it off, I decided to use a P-Channel MOSFET.

And after connecting the Source with pin 1 of the battery and Drain with VCC, it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY3MTgsInB1ciI6ImJsb2JfaWQifX0=--b401716e30145785751668dd8ccf27166bb3bd58/image.png)

And after finishing it, it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY3MzMsInB1ciI6ImJsb2JfaWQifX0=--dd81ca3b93348a5ac24c25a8f4b387e321ffe88d/image.png)

Next, I wanted to check again if I calculated it right, so that the output will be max 3.3V here:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY3MzQsInB1ciI6ImJsb2JfaWQifX0=--9988786b2ab0c8f6c5b71d2e53a8f694be868e04/image.png)

But I remembered that I did that in an older journal, so I checked it again and it was correct. So this part is fine!

Then I wanted to check the Raspberry Pi power supply because I got feedback here that L1 was too small, but the rest should be fine:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY3MzUsInB1ciI6ImJsb2JfaWQifX0=--1256c7cc837e8c1fecabfc4c36b4233e5c11dd76/image.png)

But then I saw that I actually used 2 GND flags because I thought it needed 2 separate GND nets. But now I know that it doesn't, so I changed everyone to normal GND.

So that it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY3MzgsInB1ciI6ImJsb2JfaWQifX0=--72ad0659026ae603904cb69a759e297fbdd89462/image.png)

Then I went to the footprints and updated L1 to a bigger model so that it can handle more than 3A.

So after a bit of searching, I decided to take this one: L_7.3x7.3mm_H4.5mm

It is big enough, but not too big so that it will block other parts on the PCB, and it can handle up to 4A, so it was perfect! Lastly, I updated the footprint and it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY3NTUsInB1ciI6ImJsb2JfaWQifX0=--dcc8b6c9545ae1f3317b24398b220b51ec54aacf/image.png)

Then I noticed a mistake: the sequence of those pieces was wrong.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY3NTYsInB1ciI6ImJsb2JfaWQifX0=--605090bb5ac8dc6659a4707282f6ffce4493b4ec/image.png)

So I quickly changed the order from C2 C1 C3 to C1 C2 C3.

And now the schematics were perfect! I only needed to fill in the rest of the footprints and then I could finally continue working on the routing of the PCB!!!

The only things that I had to change were J7 to just a JST-GH.

Then for Q1, I'll use the TO-252-2. Why use this?
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY3NTcsInB1ciI6ImJsb2JfaWQifX0=--1da4dfbab016fd90b58fa74e1720a50625bd275a/image.png)

Then, for J7 I decided to take the JST-GH 01x02 pin like the others, and for the resistor, I chose 1608 (0603) like all the others. And then I was finished with the schematics—hopefully for the WHOLE PROJECT!!!!!

The last 2 days were really interesting. I learned a lot about electronics and how hard it can sometimes be to find the correct thing and try to fix errors. Although I'm very happy that I finished the schematics and will route the PCB tomorrow!!

### Recording Links

- https://lookout.hackclub.com/api/media/cd0ff3d3-00ed-430e-8e9b-5a7cdec6df52/video.mp4

## Entry 22
- ID: 7852
- Author: Stefanos
- Created At: 2026-05-18T20:38:55Z

### Content

### 18. May: Fixing the routing and starting again with it!

After switching back to the routing, I firstly had to remove the old routing, remove the old components that I didn't need anymore, and add the new ones.
I firstly looked to see if I could do that somehow automatically,

and after going to Edit and then to Global Deletions, I selected tracks and vias and deleted them.

After that, I pressed F8 to load the new pieces and then deleted the old ones manually. After that, I tried placing Q1 as near as possible to the J5 power XT-cable, but then the problem was that the pin 2 Vcc block was always going against the capacitor C1, which made it impossible. But after flipping J5, I got much more space and then I placed the R10 resistor there. The only problem then was that I didn't know where to place J7, which was for the on/off switch, and because I had much space on that side, I decided to move the J5 XT30 to the top and bring the new J7 into the middle, so after all it looked like that:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTcwMTQsInB1ciI6ImJsb2JfaWQifX0=--7a6591312b058d75256f7256d7783db581d3955b/image.png)


Then I started routing again:
Firstly, I connected the + pin of the battery over pin 3 with the resistor and then the other end of the resistor. This line has to be massive, because the whole power of the battery goes through there. Next, I connected pin 1 of Q1 with the other leg of the resistor to the J7 pin 1 again. This one should be big, but not too big, because the max 12.6V for the MOSFET will be there. Lastly, I connected the GND.

So after doing all of that, it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTcwMTYsInB1ciI6ImJsb2JfaWQifX0=--11dc8847a6c5f43ddc61a1bff70740cfe043ec88/image.png)


But then I decided to make the GND lane even bigger, so that it flows much better and doesn't heat up that much:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTcwMTgsInB1ciI6ImJsb2JfaWQifX0=--b7fb2be87b1fd64b4d05a94c4c2d9c3720a6fe7e/image.png)


After that, I continued on making the battery percent measurement, but first I thought of moving U3 etc. more closely to the connector:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTcwMTksInB1ciI6ImJsb2JfaWQifX0=--9c2a6fe7c1ea02f63ef271662791c5e1ad7549e5/image.png)


I decided to position it like that because it's the shortest way for SCL and SDA, but also the shortest way to C1, C2, and C3, while also being far away enough to be safe from interference, noise, etc.

And after connecting all parts to the chip and the resistor, it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTcwMjAsInB1ciI6ImJsb2JfaWQifX0=--42fb72affe32e34031f93a1263550fc6ae3fdae3/image.png)


But then I thought that I maybe should move the 3.3V track that is under the U3 chip somewhere else, so that the chip doesn't get noise, etc. After a bit of thinking, I decided to do it with vias and move it to the 3rd layer, the power layer.

And after doing it, it worked perfectly and looked like that:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTcwMjEsInB1ciI6ImJsb2JfaWQifX0=--6e77f14e0b2c53d6330364fdcfa0bb9fd26639b8/image.png)


But then I noticed another small problem: the via for 3.3V was blocking the SDA in the future, so I switched it and made it on the other side.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTcwMjIsInB1ciI6ImJsb2JfaWQifX0=--426792b0b1f8f9474bc165170a97902f09212774/image.png)


Happy that I got everything working now, it'll be much faster, and I'm happy with the progress.


### Recording Links

- https://lookout.hackclub.com/api/media/f20cf719-18f9-4824-844e-f80dd63dc93c/video.mp4

## Entry 23
- ID: 8029
- Author: Stefanos
- Created At: 2026-05-19T20:02:00Z

### Content

### 19. May: Finished the battery percentage and started the sensor I2C connection!

I started by connecting the C1, C2, and C3 pins from the connector with the I2C chip.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1MDgsInB1ciI6ImJsb2JfaWQifX0=--3e4ed5c001d8b8557a0cced273c0323883b23e39/image.png)

But that wasn't the best solution because it would be under J3, which is not ideal. It would waste pretty much space and is also much longer, so I decided to do it with vias on the 4th layer.

And after firstly drawing the vias to the right height, I could easily draw the connections. 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1MTksInB1ciI6ImJsb2JfaWQifX0=--c4d33ecc5b3a453fef9124bfc8400903404f0d1b/image.png)

And lastly, I connected the GND pin from J3:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1MjAsInB1ciI6ImJsb2JfaWQifX0=--7af0cc187f1453752ff17acc0d588adef688a764/image.png)

And then I continued routing U1 with the 4 ToF sensors.

Then I wanted to connect them, but I encountered a small issue: the connectors and their pins weren't in the perfect position. Because, for example, J10 had more upper pins, but optimally it would have the pins of J11.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1MjEsInB1ciI6ImJsb2JfaWQifX0=--bf3dda6185fc675701460eb76df74ae0b5f42b11/image.png)

So I decided to give J9 the 0 pins because they are the highest ones, J8 the 1 pins, J11 the 2 pins, and lastly J10 the 3 pins. After I updated the schematics, it looked like this: 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1MjIsInB1ciI6ImJsb2JfaWQifX0=--2d1a4e4e3986da1115d33fe6c8a143bd64881295/image.png)

And then I started routing the J10 SDA_3 and SCL_3 pins.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1MjMsInB1ciI6ImJsb2JfaWQifX0=--e62f8147baf810cb091afe8f1025585dd7d5808d/image.png)

I decided to firstly do all data connections and then do the 3.3V and GND. After that, I continued with J11 and the SCL_2 and SDA_2 pins, but there I had 2 problems. 
There was a capacitor that could cause interference (noise), etc., and the Raspberry Pi Zero 2 W pins were there. 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1MjQsInB1ciI6ImJsb2JfaWQifX0=--f03aa08e1362eb3c2a5f0de3afc8e745290dab94/image.png)

And because of the interference, the noise, and the fear of soldering a bit of the pins, I decided not to route the pins through the pinout, but through vias on the 4th layer.

But the C9 capacitor was still a bit in the way, so I decided to move it to the other side. 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1MjYsInB1ciI6ImJsb2JfaWQifX0=--c3e22beeed39e2c8422bffc93e0233a8f8bfb79e/image.png)

And then I saw that the lines had to switch positions, so I did the same as with the battery percentage I2C. But the twist would happen at the I2C chip so that it spends the least possible time on the first layer. Afterwards, it looked like this: 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1MzAsInB1ciI6ImJsb2JfaWQifX0=--8c66ee0baeb17214171b570784cb990537002b98/image.png)

And then I continued on J8, where I used the exact same principle.

But then I decided to put them on the same height so that they don't steal space from the other pins.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1MzYsInB1ciI6ImJsb2JfaWQifX0=--1f1240fe239aee3e6a78e11872696c499f9dddd1/image.png)

And after that and routing it again, it looked like this: 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1MzcsInB1ciI6ImJsb2JfaWQifX0=--3ba5f3129be8bfa13250d0f15ef3c1e1642fd6c3/image.png)

And after doing that also for J8, it looked like this: 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1MzgsInB1ciI6ImJsb2JfaWQifX0=--f5e125d147312c8adb516e42a3f81017c9866943/image.png)

And then I placed the J9 connection.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1NDEsInB1ciI6ImJsb2JfaWQifX0=--06a1d313cd6d526f8462bf27865f8cc13d244cf4/image.png)

But then I saw a mistake: the lines were blocking R1. 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1NDIsInB1ciI6ImJsb2JfaWQifX0=--f7719e707bfaae68761ac4f92c0027b2db583300/image.png)

So I deleted the old ones and moved them further to the left. After  adding the traces, it looked like this: 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1NDQsInB1ciI6ImJsb2JfaWQifX0=--525a4c8d987f39477511cf4f180eb42257699eee/image.png)

Lastly, for that session, I made the GND and 3.3V connections to every sensor. I started with the GND pin because I would just need a via:

And then it looked like this, for example, in that part: 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1NDYsInB1ciI6ImJsb2JfaWQifX0=--6e9b9a6ee9d6f91e4df33319ebb7446a1d1ae564/image.png)

And then I had to connect the 3.3V to the sensors through vias.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1NDcsInB1ciI6ImJsb2JfaWQifX0=--4d0c3ba904522ef66cc8058ca33d60b4eb4cb9ee/image.png)

And then I did the same to all the other 3 sensors.

And then, after all, it looked like this: 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc1NDgsInB1ciI6ImJsb2JfaWQifX0=--4e761029f894e251c0496dc29b320e7807806d4f/image.png)

I didn't have much time today (I have a math exam on Friday T-T), but I managed to finish the battery percentage and connect the sensors with the I2C.

### Recording Links

- https://lookout.hackclub.com/api/media/59dba2a7-2f81-4cfe-b29b-54de82a00de7/video.mp4

## Entry 24
- ID: 8210
- Author: Stefanos
- Created At: 2026-05-20T20:08:02Z

### Content

### May 20th: Routing the 3.3V power supply and starting the 12.6V to 5V buck converter!

**ATTENTION:** For some reason, Lookout bugged out on me and kept turning my main monitor off and on sometimes. So, for about 30 mins you do not see the progress, but I wrote what I did in that time in the journal. It's NO FRAUD, PLEASE DON'T count it as such or something, I don't wanna get in trouble...

In this session, I want to route the U1 chip.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc3OTQsInB1ciI6ImJsb2JfaWQifX0=--6234371a85ad45c89ec92fe73a2a3c0e4b61beaa/image.png)

Therefore, I had to find (optimize) the position of the components to get the optimal connections.

I actually didn't need much time to optimize and I basically only moved the components (R1, R2, R3) further up so that the other pins have more space and the voltage lines have a bit more clearance from the data lines.

After that, I started by connecting the SDA/SCL connections. But after starting, I thought of  that I had to pay attention to the second SCL/SDA line that goes from U3 (the battery percent).

Firstly, I created the vias for the pins at the U1 chip and the pull-up resistors.

And then I also added the vias at the battery percent sensor.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc4MjIsInB1ciI6ImJsb2JfaWQifX0=--ce7544ad80aa091befbf2532dc85bb516944f131/image.png)

And then I connected all 4 pins with the Raspberry Pi.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc4MjUsInB1ciI6ImJsb2JfaWQifX0=--f63ebbf7aaa78c6bc82e5b68880068aaebf5588d/image.png)

I firstly made the GND connections, and since there were plenty of GND pins, I decided to connect them with vias.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc4MjcsInB1ciI6ImJsb2JfaWQifX0=--fcfc0690ee48b84c27643887a3474bbe6f0e2d34/image.png)

Then I added the last GND vias because I had forgotten that, and I also changed the thickness of the vias from 0.5mm to 0.4mm because that was the width of the pads for soldering.

After that, I made the 3.3V vias and connected them to the 3rd layer (power plane).
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc4MzAsInB1ciI6ImJsb2JfaWQifX0=--23ab7e80d6fb8eb98d18d28ffc5cea525f65ae3f/image.png)

Lastly, I had to connect the reset pin with the Raspberry Pi, which I also did through the 4th layer (2nd signal layer) because the other tracks were blocking the way.

But then I found an issue with the connection because there was again no way through.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc4MzEsInB1ciI6ImJsb2JfaWQifX0=--368d03502ebae696ae5add7a60c7685d2b4a65d7/image.png)

And after bringing the lines further down, it looked like that. And after connecting the line:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc4NzMsInB1ciI6ImJsb2JfaWQifX0=--6d553fbf7de980d0197a17779c102647799033c2/image.png)

After connecting all with a 1mm track and the small track with 0.5mm, it looked like that:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc5MjAsInB1ciI6ImJsb2JfaWQifX0=--1a37358dd6b89f9d6cf40920ec483f33d1031a76/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc5MjEsInB1ciI6ImJsb2JfaWQifX0=--fd9d74e64caa48144bbbf443ba25de2620aea4df/image.png)

(And here I don't know why the app just recorded only one screen for a couple of minutes, sorry)
But then I was afraid that one pin couldn't power that many things. Also, another problem came up: the other power lines had almost no way around.

So I decided to use vias and bring them to the GND plane, but the vias were too small, so I decided to make them bigger: 1.0mm diameter and 0.5mm hole.

And after drawing and trying a bit with sizes and positions, and paying attention that it doesn't go parallel or so to data tracks, it looked like that:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc5NDExInB1ciI6ImJsb2JfaWQifX0=--92a60f2d5ed25a77d3ea5f2d1f64886cdeb533c6/image.png)

And then I moved on to making the 12.6V to 5V thing. But firstly, I had to find the best position, and I looked in the datasheet to see how to do it best:

And after all the tuning, it looked like that:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc5NDQsInB1ciI6ImJsb2JfaWQifX0=--e7c449adac72a199f440917ef88d27ef362f9462/image.png)

But after all of the routing, I mostly followed the design from the schematics and optimized it to mine:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc5NjIsInB1ciI6ImJsb2JfaWQifX0=--18b3694a0a5ed989c102c444c31ffba914529974/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc5NjMsInB1ciI6ImJsb2JfaWQifX0=--4c1ff81dc995f2134ec63b38bcc9f9ef7266ead3/image.png)

Tomorrow I'll hopefully finish the PCB, and then by the end of the weekend I'm finished with the project. Overall happy today, and till tmw!

### Recording Links

- https://lookout.hackclub.com/api/media/d76554fa-a0ee-4ab7-93b9-97fc9dac90a4/video.mp4

## Entry 25
- ID: 8359
- Author: Stefanos
- Created At: 2026-05-21T20:06:08Z

### Content

### 21. May: FINISHED THE PCB!!!!

I firstly drew the big 5V connection on the Powerplane 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyMTgsInB1ciI6ImJsb2JfaWQifX0=--4dd4702a4aded74b8e2b4ed11442ada7c01c8358/image.png)

and updated the vias at the VCC connection so that they are bigger, and then I continued on making the GND connection.

I started by connecting the top part's 3 connections together and then connected that with the down GND connection. And then I saw that in the datasheet they showed that they made a huge GND plate with many vias, and also under the MP part for cooling, optimal flow, and temperature. So after making a hugeee plate and adding the vias (which by the way were very hard because all had to have the same distance but they were awkwardly rotated, but after a bit of trying I got that)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyMjYsInB1ciI6ImJsb2JfaWQifX0=--29b99e5a9bba4b4e3afca056fc1f1f4b3f8abd40/image.png)
but then I saw that I had some 90-degree angles which wasn't that good. So I quickly removed them by adding a diagonal trace..

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyMjcsInB1ciI6ImJsb2JfaWQifX0=--d7579ca57de02c01e0782a7a22594c9318dca5ea/image.png)

But I saw that I forgot to connect the other GND net with the vias to the GND plate, and also add the GND from the battery connection, but then I saw that there should actually be more vias (4, so I added them).
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyMzUsInB1ciI6ImJsb2JfaWQifX0=--1348f48a3c5042e85791ebabd2a22169a7098283/image.png)

and after implementing it looked like that 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyMzYsInB1ciI6ImJsb2JfaWQifX0=--1e041f451a42158ac1ead2c47737315abd1009d2/image.png)

Then I continued on connecting the 1st capacitor that is for the servo with the 5V and then also to the FB8.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyNjAsInB1ciI6ImJsb2JfaWQifX0=--7be5d961644dab4895299618cfb4e77afa43c655/image.png)

After that, I improved the position of the other 2 capacitors that the servo would need, and made them so that they had the shortest way to the 5V buck converter. And after also connecting those components it looked like that:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyNjExInB1ciI6ImJsb2JfaWQifX0=--0e692e8c4b8ad2da68dacb0f314e8acf5b95ed22/image.png)

I also decided to make the vias for the power bigger: diameter 1.6mm and hole 1mm.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyNjIsInB1ciI6ImJsb2JfaWQifX0=--d859e0ef1d6f6a4038c3210b7fa9fee0421032ae/image.png)

Next, I started with the connection from the 5V power supply to the servo, but I had to pay attention so that the Raspberry Pi power supply wouldn't go all the way up and go to both the FC data connection and sensor, and get false data through noise.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyNjQsInB1ciI6ImJsb2JfaWQifX0=--d854437bb0e3b044da26064cbe6afc9cc4cae9d2/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyNjUsInB1ciI6ImJsb2JfaWQifX0=--c300a674834535059344e6c648c4411a1a593717/image.png)

But there was still a problem: the two blue lines (data) were perfectly parallel to the 5V line, which is terrible. So I decided to put them further down.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyNjksInB1ciI6ImJsb2JfaWQifX0=--57d4aa6f75c55798b41bfdea007df0960b036374/image.png)

And now I could start, but I forgot that the pins from the Raspberry Pi were blocking a part, so I actually had to go around it.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyNzAsInB1ciI6ImJsb2JfaWQifX0=--7b19aa61bae01d2c769d9e1a870d459d0bc314e5/image.png)

But I noticed I could save some space if I wouldn't turn all to the other side of the 2 capacitors.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyNzMsInB1ciI6ImJsb2JfaWQifX0=--bc0fa510fca16f5636204f9c45cbc09e3e795b9b/image.png)
And after turning the components and connecting them again, it looked like that above.

After I recovered it, it looked like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyNzQsInB1ciI6ImJsb2JfaWQifX0=--dbc4522f0b391bbde561191251509eb1b44d94ff/image.png)

After that, I connected the servo GPIO pin with the servo.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyNzUsInB1ciI6ImJsb2JfaWQifX0=--68c114fc402aa44d9fea41251082e28b87f8c055/image.png)

But I thought that if there would be another pin that works with the servo and is further down, that this would be much better. So I searched for a new one, but there weren't really other pins that were PWM-capable, so I didn't change that.

And then I only had to connect smaller things like the TX RX.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyNzYsInB1ciI6ImJsb2JfaWQifX0=--d91818d6c8c5d774a9046d82a49ec3f3af57384b/image.png)

And then, very important, the power to the buck converter and the FC.

And then it looked like that. I tried to make the tracks as wide as possible so that it doesn't heat up.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyODQsInB1ciI6ImJsb2JfaWQifX0=--2e704351375d7423b53ae3a2da21fa2439239593/image.png)

Lastly, I connected the last missing GND connections and checked everything again.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyODgsInB1ciI6ImJsb2JfaWQifX0=--54b6d7082c54bd7a36616ae6690031544a34f3ef/image.png)

And then I wanted to add GND planes to every layer and to every spot that is free for better absorption and better cooling.

I found out that you can do it the exact same way as for the GND layer, and it worked perfectly! I applied it to the other 3 layers.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyOTQsInB1ciI6ImJsb2JfaWQifX0=--fd1809c10f81c305d3554ec4c49d8e88e6293940/image.png)

Now I only positioned the codes/numbers of the components nicely so I can read them clearly.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgyOTUsInB1ciI6ImJsb2JfaWQifX0=--25c677b9c67a36f240502df457e486b5fb5ec8d7/image.png)

And then I added small detailed pictures like the fan from Hack Club and Fallout, but that didn't work that well and I'm doing that tomorrow.

Overall happy, GOT BASICALLY THE PCB DONE!!!!

### Recording Links

- https://lookout.hackclub.com/api/media/a0720a00-95b1-4759-aac4-6754cc47eb09/video.mp4

## Entry 26
- ID: 8621
- Author: Stefanos
- Created At: 2026-05-23T09:24:17Z

### Content

### 22. May: Finding name and finishing the PCB!

After I got back from school, I started directly and actually found a really cool name for my project: Odonata.

I came up with that because it's the Latin word for dragonfly. They have 4 wings, can fly in every direction, and are very precise pursuers. I really like the vibe because it sounds a bit Japanese or Chinese and a bit mysterious. So, I went right ahead and created the GitHub repo!

For the description, the first version was: 
> A small, fully autonomous drone that can fly precise flights indoors and be commanded from all over the world!

After a bit of small optimization, it was: 
> A fully autonomous drone for precise indoor navigation and worldwide remote control.

And after adding tags, it looked like this:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg1NDEsInB1ciI6ImJsb2JfaWQifX0=--b50090fcdb6205f0877e1cb782739596f656af60/image.png)

Lastly, I wanted to find a cool font for the name so that I could add it to the PCB, but also onto the drone itself.

I decided on this font, which is named: Bungee ![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg1NDIsInB1ciI6ImJsb2JfaWQifX0=--51b7ad453840c38bb7a6b2a87f3e990b6014067d/image.png)

What I wanted to write on my PCB was the project name, my name, the date, the Fallout text/logo, the Hack Club flag, and also the version number.

So, I started with the flag, which I got from hackclub.com/brand/. To add that, I had to open the image converter in KiCad and upload it.

After watching this video (https://www.youtube.com/watch?v=00Gn0FWlMzU), it worked, and I had a HUGE HC flag on my PCB!  (actually to big)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg1NDksInB1ciI6ImJsb2JfaWQifX0=--1a7a243acf315f59bafffc0309471a409cbfe316/image.png)

I wanted the flag and most of the text on the back, but I also wanted the name, so I had to measure how much space I have, and for the most parts I had max 20mm width. But I started with the text:
After playing around a bit, I found 3 fonts that I liked (I couldn't use the other one I had searched for previously), and I decided on the first one.  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg1NTYsInB1ciI6ImJsb2JfaWQifX0=--75eef09b07fcdd7c164a02412787b182747f8ee6/image.png)

After placing it, it looked like this:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg1NTgsInB1ciI6ImJsb2JfaWQifX0=--059732ab522a27f8d1c39e6caa1c87612a63078a/image.png)  


Then, on the other side at the bottom, I also placed the GitHub link and my name.

And then I wanted to add Fallout and soup :) For the FALLOUT text, I found out that I needed the HellsBells font, so I got that.  (found that out from the website)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg1OTIsInB1ciI6ImJsb2JfaWQifX0=--78bb8137acf7cec5f7e8c655832bbb76f836c25a/image.png)

Then I noticed THAT AGAIN THE LOOKOUT APP ONLY RECORDED ONE SCREEN ALTHOUGH I SELECTED TWO! So I probably lost like 20 minutes of recording. (during that time I convertet the images and, had some Issues with negative and sizes so it took quite a bit of time, but worked at the end)

I also wanted to add this sticker, where orpheus skates a PCB, because it's very cool.

After adding them, it looked like this. But soup was too big, and the sticker and Fallout should be negative so only the small lines would be seen. So, I quickly changed that.

After all that, it looked like this:  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg2MzcsInB1ciI6ImJsb2JfaWQifX0=--3976c4e821707ae0f19e73300ce97d58f359cdc8/image.png)  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg4NzAsInB1ciI6ImJsb2JfaWQifX0=--038552a9918b48bbe21deae30d3003dbf01e2002/image.png)




Then I wanted to save my PCB and check if everything was right.

When I ran the Design Rule Checker (DRC), I GOT SHOCKED (a bit exaggerated...), 8 errors and 36 warnings!

One error was that the GND and VCC were connected through vias.  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg2NTAsInB1ciI6ImJsb2JfaWQifX0=--ba7b8d62882a34309254e6588cfb2dd29b58cef2/image.png)

So I just moved the track further up... and... 4 ERRORS away!  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg2NTIsInB1ciI6ImJsb2JfaWQifX0=--d3271cf345faa98508e201068afa47debd2f2177/image.png)

Another error was that the distance was too close to the pins.  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg2NTMsInB1ciI6ImJsb2JfaWQifX0=--b0474e0b69deb2b5f27013ab7a9583e7181f00fb/image.png)  
So I changed its position.

Then I got "Thermal relief connection to zone incomplete", and I didn't understand what the issue was. But after a bit of research, I learned it's because when you are soldering, the heat soaks into the large copper pads, making it harder to solder. It's actually not an electrical issue, and mostly there should be two small spokes, but there wasn't any space for that. So I just ignored/deleted that marker.

The next problem was the same GND thing, there wasn't enough space, so I moved the TX pin further down.  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg2NTQsInB1ciI6ImJsb2JfaWQifX0=--8724b23136267e222608920ac10813ddbad8a46c/image.png)  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg2NTUsInB1ciI6ImJsb2JfaWQifX0=--16a07bb450f19d6ca06d20a2c35118233b2d4b79/image.png)

The next problem was like the one before the last one, so I just skipped it.  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg2NTYsInB1ciI6ImJsb2JfaWQifX0=--3242a82d1b2de732d5249569df8c596faac6f24f/image.png)  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg2NTcsInB1ciI6ImJsb2JfaWQifX0=--5f06258c09c46d8b41c5fc2b441476b3dd5cb214/image.png)

And then the next problem was that there was a track with no connection.  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg2NTksInB1ciI6ImJsb2JfaWQifX0=--a091e01da031111394c6d5f1b976e11beb96114b/image.png)

So I just deleted that, and then 0 errors and now only warnings!!!

Actually, all the warnings were no problem, and I was basically almost finished.

After generating the Gerber files and putting them in a ZIP, it looked like this. And 5 pieces would only cost 6 Dollars!  
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg2NzEsInB1ciI6ImJsb2JfaWQifX0=--086e793a908eb1c5867f9a0176fb407b86fd3f09/image.png)

Lastly, I wanted to export the PCB as a 3D model to import it into Fusion for my drone. I exported it as a STEP file and uploaded it into Autodesk Fusion so that I can later assemble everything nicely in Blender, but also make the holes and standoffs to hold the PCB. But because the upload took sooooo long, I stopped the Lookout recording and took a shower. See ya soon...

And it´s morning... I actually got sick yesterday and went to sleep, so this session ends here now!






### Recording Links

- https://lookout.hackclub.com/api/media/adbe344f-0b08-492b-9815-f656c3b5bcfe/video.mp4

## Entry 27
- ID: 9079
- Author: Stefanos
- Created At: 2026-05-25T10:12:43Z

### Content

### 23-24 May: Fixing PCB, CAD and lastly starting and finishing the Landing station!

After uploading the PCB into Fusion, it looked like that:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg4NzgsInB1ciI6ImJsb2JfaWQifX0=--f97d79ac1349c8bc0d85f8a0fffbd19f1ae7dac7/image.png)

and after placing it in the drone, it looked like that: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg4OTksInB1ciI6ImJsb2JfaWQifX0=--30e705c44ab1a12a6c27e7e13818155ae4b4e86d/image.png)

and now I started creating the columns, so that I can screw the PCB with the fx on the drone.

After measuring the height, I started placing them (height was 8.82mm) +4mm , because of the thickness of the platfrorm

but firstly I had to check how big the hole should be

and I decided that I should add an additional 2mm for more stability, and also so that the heat insert fits perfectly, and after adding the holes which I copied from the arms and lastly rounded the bottom, it looked like that: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5MDUsInB1ciI6ImJsb2JfaWQifX0=--68d6a0d7172254b575600e0411b4f2cc52811109/image.png)

and after adding the PCB on it again, it looked like that:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5MDYsInB1ciI6ImJsb2JfaWQifX0=--86fa7646a6959471a1108899206c3a1c2a37c325/image.png)

and then I wanted to add the text to the drone, so I firstly searched up how to do that. You have to make a new sketch and then there is a tool called "Text" where you can write sth on the sketch

Firstly I wrote the name on it: ODONATA
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5MDcsInB1ciI6ImJsb2JfaWQifX0=--7c17fbed610556f12157c4cd89f4afab6f878df3/image.png)

and then the version plus date: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5MTEsInB1ciI6ImJsb2JfaWQifX0=--00b193b0b15e55fa6194eeda16f96ff9358c5f92/image.png)

then I started making the 3D model a bit cooler and made small like notches on the sides: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5MTYsInB1ciI6ImJsb2JfaWQifX0=--28f7615134a0e26ba5b735f418db9863048fd097/image.png)

I tried other things like /// >>> or ||| but that didn't look nice and I just left it as it was, but now...... THE DRONE ITSELF IS FINISHED!!!
Here is the finished drone:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5MjUsInB1ciI6ImJsb2JfaWQifX0=--3733485b6c91b58de36bb1662c6b40386b9dc2cf/image.png)

and then I started with the landing station. Like I said before, it will be like that and will have its own AprilTag attached in the front.

I firstly drew the lines and made an outline of 1cm, so that if the drone has an offset of 10mm it will position itself, and now I also made a small outline of 0.5mm, so that the drone can perfectly fit.

And then I deleted the old lines and kept the others, and so I got that: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5NDYsInB1ciI6ImJsb2JfaWQifX0=--8d4a138c51372ae13efbc0ca4c9f4710fbd4b9a7/image.png)

but after that I saw that I forgot to add the holes for the front, back, and the arms. So I went back and changed that.

And after adding them in the sketch, it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5NTEsInB1ciI6ImJsb2JfaWQifX0=--0b2553942e1ff9132af160ba704125cff44372c7/image.png)

now I only had to make the 10mm offset, so it works out with the 10mm error.

And then I had to stop because I had a headache, and after measuring my temperature I had a very high fever, so I lay down. And now, one day later, I'm better and continuing! During that time, I remembered that I forgot to add the on/off switch for the drone into the CAD, and I decided to place it on the back because it's the easiest to click there; on the sides, the propellers make it more dangerous.

And I decided to use this switch: https://www.digikey.de/de/products/detail/e-switch/RA1113112R/3778055?gclsrc=aw.ds&gad_source=1&gad_campaignid=20496382285&gclid=Cj0KCQjww8rQBhDjARIsAE43KPMbfgeEBc8-5HGrJN0BMzVz1RTfrfVK5zAIDxv98wixdx1Dpi16iw4aAjvNEALw_wcB because it can handle up to like 120V and 10A, which IS PERFECT!! It looks like the classic switch (cool): 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk0ODQsInB1ciI6ImJsb2JfaWQifX0=--65348ac97a1578c1c79bd7e6cd0a27ebebf683f3/image.png)

and then I found the dimensions of the cutout and I directly applied them into the CAD:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk0ODVsInB1ciI6ImJsb2JfaWQifX0=--e79e0777c1d56f9474d25b72cae2f4e4c4928221/image.png)

and after cutting it out, it looked like that, but the cover holder thing was also sticking out, SO I decided to also cut it.

And I wanted to see if the battery and the switch would fit into it, and during that, I saw that the JST-GH that I added to the PCB was different from the one on the battery, so I had to update the footprint: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk0ODksInB1ciI6ImJsb2JfaWQifX0=--9457b9768d945ba6f131e5ad499cdb58c6c19208/image.png)

and after searching online, I found out that I would need this one: `Connector_JST:JST_XH_B4B-XH-A_1x04_P2.50mm_Vertical`

and after updating, I had to fix some issues with that: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1MDIsInB1ciI6ImJsb2JfaWQifX0=--1310c1cd47597c07106d00f82a59050292317284/image.png)

and after finding the optimal position and rewiring, it looked like this (and in 3D, I was a bit shocked btw that this connector is THAT BIG):

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1MDgsInB1ciI6ImJsb2JfaWQifX0=--36ccc45896d998bba2653a41e01e724ccdb2b422/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1MDksInB1ciI6ImJsb2JfaWQifX0=--a874b3b00811867e8165bc7bff7d0f246cd44fd8/image.png)

but then I was very afraid that the battery wouldn't fit perfectly, so I designed the battery to test it, and..... the battery didn't fit, whYyYY? 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1MTMsInB1ciI6ImJsb2JfaWQifX0=--1394636689bea848e350d8f6e6e49db9552f3435/image.png)

and after trying and thinking for like 20 min what to so, I saw that the only solution would be to extrude the back by 15mm. So after adding a construction plane and moving it to the point, I split the back of the drone, moved it back, and made the back of the drone larger. And after positioning the battery in there, it was almost perfect (I'm just afraid how the center of gravity will be).

 ![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1MjQsInB1ciI6ImJsb2JfaWQifX0=--a8629fd038fa354b7250628fcc9e1ae3088e6d06/image.png)

I just had to cut a bit of the cover holding part and it would be fine, SO I did it.

I cut the part that was unnecessary and I rounded the cut corners, and it looked like that: 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1MjgsInB1ciI6ImJsb2JfaWQifX0=--b2e6cf429d2c208ba140cffea46d0bf55bd76d84/image.png)

so after that, this part was finished:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1MjksInB1ciI6ImJsb2JfaWQifX0=--1c6f4f37cb0ac5f68b1479283a80fae65a6142ea/image.png)

But I still had to position the on/off switch. At first, I didn't want to position it on the cover, but I didn't have space anywhere else, so I had to do it. And after finding the perfect spot for the on/off button on the top, it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1NjksInB1ciI6ImJsb2JfaWQifX0=--9f38e891e52861f8127b6a2e038e02b3fe8b128f/image.png)

It is the perfect position because it needs about 2cm to the bottom, and there is nothing for about 2.5cm, and it's directly under the pins which is connected to it.

and the drone is finished!!!!

and now we continue on the landing station again, but when I wanted to open it, it was lost.... I probably forgot to save, sooooo I had to start from the beginning T-T

I firstly started by making a new sketch and projecting the important lines: 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1NzUsInB1ciI6ImJsb2JfaWQifX0=--601ebbb41bdcc723030a41a555f6a72147662c8a/image.png)

and after making an offset of 10mm (so that the drone centers itself): 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1OTAsInB1ciI6ImJsb2JfaWQifX0=--0da2b35a3d0f32d98573e585c3b050a8e1065036/image.png)

I then started extruding for 50mm, so that after landing the camera can still see the AprilTag and can stabilize itself etc. After that, I made the hole in the middle where the drone will land on: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1OTEsInB1ciI6ImJsb2JfaWQifX0=--1499357b078fd2f0cb77533b411ec13cedfd4987/image.png)

after that, I cut out where the parts will stick out, so the arms and the front and back body.

So I firstly removed the holes and the text from the platform, so that I can extrude and cut the things out of the landing station:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1OTYsInB1ciI6ImJsb2JfaWQifX0=--cd330fe8da8d1c67f6b26a677e208b330b7e9f77/image.png)

and so I cut the front and back object into the landing station: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1OTcsInB1ciI6ImJsb2JfaWQifX0=--10528e11a56758a1f6593f17f34a88ec2a85bca6/image.png)

Now I had to cut the arms, but therefore I firstly had to measure the angle of the arms, and after measuring I found out that it was 3.6 degrees: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk2MDEsInB1ciI6ImJsb2JfaWQifX0=--877c85ec0a57881bd09801aa210734731ba61187/image.png)

But firstly I selected the arms and cut the holes:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk2MDIsInB1ciI6ImJsb2JfaWQifX0=--278f7a90c87ff79d424cb1aaddc7a685aec2eddf/image.png)

and after that, I rounded the corners.

1. I rounded the corners of the arms with a radius of 2mm. I used that because it's small enough so that the drone is still in a good position, but also good for the printer so that it doesn't have to like stop and go in the other direction.

And then I continued on those corners: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk2MDQsInB1ciI6ImJsb2JfaWQifX0=--c24a3f73d4906d12a210753cc4da883e9b6124f5/image.png)

I decided to use 4mm here so that it looked like a half circle and so cleaner: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk2MDUsInB1ciI6ImJsb2JfaWQifX0=--7dcf4bd20f66c28b078151a9d1aafe783b670356/image.png)

and now I had to make an offset of 0.2mm so that the drone isn't stuck:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk2MDYsInB1ciI6ImJsb2JfaWQifX0=--076dd46db7ad569e343aaa5be62a9018d64f4a4a/image.png)

and now I added the angle for the drone arm, but I first had to search how you do that because I didn't know that.

And I tried with many tools like Loft, chamfer, and draft. At first, I didn't really know how they all worked so I had to find that out, and all of them had their problems and it didn't end up how I wanted it. I was thinking of other solutions like maybe cutting it with planes or making like a sketch and then extruding that part with cut, but luckily after checking Draft, it worked perfectly! And after adding 45 degrees, it was perfect and I only had to adjust the height of the platform where the drone will sit:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk2ODksInB1ciI6ImJsb2JfaWQifX0=--638af43e06db446ebd2216a1b591e0458307cb70/image.png)

and then I wanted to make that landing station a bit nicer looking, so I added the project name: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk3MTcsInB1ciI6ImJsb2JfaWQifX0=--da81c3a38139952198db4c1f11fdab8f806a11f1/image.png)

then also added a small like barrier by making an outline: 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk3MTgsInB1ciI6ImJsb2JfaWQifX0=--a1114866de2f19a9b408704af63166496a20962e/image.png)

and I had the idea to also add Bumpons so that it stays at its place and also cushions the drone a little bit, SO I right away made the holes for it in the CAD model.

I tried making them as close as possible to the edges of the landing station with a diameter of 13mm:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk3MzgsInB1ciI6ImJsb2JfaWQifX0=--9c1fdb24e0d4df5b5d2cccac1726a0b79e7570fd/image.png)

and after that, I extruded them with cut mode for 1.2mm:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk3NDAsInB1ciI6ImJsb2JfaWQifX0=--4f625be8ac1813f4b351564dfeb59d87a5155319/image.png)

to make it prettier, I also added some little like strips or like blocks here: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk3NDMsInB1ciI6ImJsb2JfaWQifX0=--02b6339231dfc56c957189fd40418518a12ecfd9/image.png)

and also added some text at the bottom:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk3NDUsInB1ciI6ImJsb2JfaWQifX0=--6c88802202933bddb8f6b6a741633ea2fc497c02/image.png)
 
lastly (for good looks, I also added an outline to the center tiles): 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk3NDgsInB1ciI6ImJsb2JfaWQifX0=--edbb9b29e02d63f9f2c06214a8d2193d39785278/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk3NTEsInB1ciI6ImJsb2JfaWQifX0=--040766dc55d7022e950078ff69a14a6ac6cbfc6c/image.png)
Looks sooooooo cool!!

and now I only had to add the AprilTag attachment code thing, and for that I had to firstly find out where the center of the camera is.

I started by projecting the camera thing and finding the center. Then I calculated that I would need 5mm so that the connection would be strong enough, and then I drew the rectangle—and the AprilTag can be this large.

And then I had the idea to make it so that you can slide in a piece of paper so that you don't have to glue it etc., SO I had to make like a cover with walls, and that's what the sketch looked like:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk3NjIsInB1ciI6ImJsb2JfaWQifX0=--25490806d1ccae99632790baa8d9f3c4ecd8feea/image.png)

and after extruding the parts, it looked like that: 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk3NjUsInB1ciI6ImJsb2JfaWQifX0=--e27dc8c1d54aa0eb698d451639cc32a5fca3b34a/image.png)

For the connecting mechanism, I thought of something like that. I added 2 of them for more stability, but also so that it cannot turn to the left and right, and then these teeth so that it doesn't come out.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk3NjksInB1ciI6ImJsb2JfaWQifX0=--9ed5dd1c68f885489ffcf8cf4f41f33ebc943383/image.png)

and after rounding, it looked like that: 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk3NzAsInB1ciI6ImJsb2JfaWQifX0=--a964480b9fe846ec49657aa8202b87323e703399/image.png)

and additionally I then added an offset of 0.25mm so that it perfectly fits:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk3NzEsInB1ciI6ImJsb2JfaWQifX0=--419182bbf21a40149e2d23289a01ed05a73b3cca/image.png)

and then I extruded it (cut) into the station by 5mm.

And directly afterward, I added the original piece to the AprilTag holder and rounded the connection by 1mm: 

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk4MDYsInB1ciI6ImJsb2JfaWQifX0=--6ef18007f3a7f9b1fb78a19d76cdc66a02fc81c5/image.png)

After that, I rounded the corners of the holder itself and I was finished with the CAD for that PROJECT!

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk4MDcsInB1ciI6ImJsb2JfaWQifX0=--3bd2a8391b5863744720d60e50218a13514237fa/image.png)

Happy with the progress today (last day), fixed the PCB + drone and started and ended the landing station. Sorry that this session got that long, I just didn't have the energy to fix and write the journal while I was sick...

### Recording Links

- https://lookout.hackclub.com/api/media/18ada570-57e6-4fd8-b9e5-8464013dad85/video.mp4

## Entry 28
- ID: 9321
- Author: Stefanos
- Created At: 2026-05-26T10:07:56Z

### Content

### 25. May: Starting coding and making Takoff!!!

And now it's CODING TIME !!!

Firstly, I cloned my GitHub project and then directly created a folder called `firmware`, where all the code will go. Then I split it into 2 folders: 1. `drone` and the other one `server`. In the `drone` folder will be the code for the drone, and in the `server` folder will be the code for connecting the drone with the server, the website, the control, and the server. I directly created a README in the `firmware` folder to clarify this, and after writing the README, I started with the drone:

First, I just copied the code from the YouTube video tutorial to have a base to start and understand MAVLink better. I got the code from this: https://www.youtube.com/watch?v=riWIg6Yx4KI

And after creating a venv and installing pymavlink, it was without errors.

But understanding how this works and optimizing it for mine was TOUGH and extremely hard.
But then I found that guide which made it a bit easier: https://ardupilot.org/dev/docs/raspberry-pi-via-mavlink.html

And I didn't get anything reading the GitHub code for that tool. Searching online for other guides, nothing helped or worked, and after watching the video again I understood how it worked (but not completely).

> 
> 1. make ssh connection with the drone
> 2. install mav proxy
> 3. setup fc wiht mission planner, to enable the UR ports
> 4.  set the boud rate to 115200 +set the protocol to mavlink 2
> 5. make the connection between the pi and fc: 
>     1. ssh connection to the pi
>     2  cd .local/bin
>     3.  python3 mavproxy.py -- master=/dev/serial0 -- baudrate 115200 -- aircraft MyCopter       <-- install maxproxy 


The only problem now is that at the end of the video, he showed the code once, and in the doc file, the codes were different. I thought the code in the docs was up to date, but the code in the video looked like the right one.

But then I got the code:
So before all of that, you first have to run all the commands at the top.

And then you basically connect with `master = mavutil.mavlink_connection('/dev/serial0', baud=115200)` with 115,200 bits per second communication (have to later check if my FC can handle it) and this port: `'/dev/serial0'`.

Then you activate the motors with  
> master.arducopter_arm()

and then run the command:
> master.mav.command_long_send(
>     1, 0,
>     mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST, 0,
>     1, 0, 20, 2, 0, 0, 0
> )

And here is where it gets a bit confusing, because there are like 10 different numbers. 

But we will break it up a little bit with nice comments:
> master.mav.command_long_send(
>     1, # system id of the fc
>     0, # autopilot mode of the fc
>     mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST, 
>     0, # confirmation
>     1, # motor number 1
>     0, # throttle value in percentage 
>     20, # throttle value in percentage
>     2, # time in seconds of the test
>     0, # -
>     0, # -
>     0  # -
> )


And now, after understanding the code, I wanted it to be able to control all motors independently. Because I want to firstly make a web app where you can control the drone manually, so you see the sensor data, you can control the servo, see the camera feed, and can control the motors, and also the AprilTag tracking, but it doesn't fly autonomously, because that requires a lot of trial and error and would be too much pain. So I want you to be able to control each motor independently, the throttle and the time of it, but I forgot to record all of that !!!!! 1 and a half hours of work for nothing T-T (ok, not for nothing, but nevermind).

But for that, I will organize the `drone` folder a bit better. I'll make one file called `motor` for the motors, one `camera` for the cam, and one called `servo` for the servo, and one for the ToF sensors called `tof_sensors`, and the last one `main`, where everything is put together and sent to the server.

In the `main` I left the connection builder and the imports, but during the search I found that you can also, for the optimal flight, wait until you get the first heartbeat with the command `wait_heartbeat()`. So I created a function in `motor.py` called `motor` where you can say which motor, how much throttle, and for how long. Additionally, I want to add a function that is for the takeoff because it should be very easy, because it is also just one command called. But I found out that you actually need GPS for the takeoff and I don't have GPS, but I have the ToF sensors and I can use them instead in a custom function, so I will do these first. 

Firstly I checked which I2C I had, and after looking at the schematics I saw that it was the 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjAyMDMsInB1ciI6ImJsb2JfaWQifX0=--6c7fb2917697e5bc5bbecae647438d5ca3a57141/image.png)
TCA9548A.

In the code I firstly initialized the I2C and the TCA. I made it by firstly importing the `busio` and `adafruit_tca9548a` library, and then with these two commands:
> """ initialize the i2c bus """
> i2c = busio.I2C(board.SCL, board.SDA)
> 
> """initialize the tca9548a multiplexer and set the adress to 0x70"""
> tca = adafruit_tca9548a.TCA9548A(i2c, address=0x70)

Then I added the channels that I used and go through them, measuring the distance of all of them after each other with a for loop. To do this, I firstly created a list where all the addresses are, and in a while loop, measured the distances from all sensors one after the other and then returned the distances as a list every 4 measurements, so that every session and this happens every 100ms. So measurements happen about 10 times per second.

The only problem now would be that if I start the function, it would just run all the time but stop the rest of the code. And to avoid that, I need to somehow make it so that it can run in the background of the code but give new data 10 times a second. And to find out how to do this, I firstly searched up how to do this exactly.
And while doing that, I saw that I should do a class because the setup and initializing was currently also in the same function. So I kinda changed the system a bit:

I created a setup function where all the initializing happens and moved the list `tof_sensors` into the init function, but I still had to make it work in the background. After a quick search on the internet, I found a nice library called threading that lets you, like I need it, run stuff in the background, and therefore I had to create also a start function to start the threading.

But after I had implemented the start function with:

```
def start(self):
        # start the thread for the distance measurement loop
        thread = threading.Thread(target=self.measure_distances)
        thread.start()
```

I still had one problem: I still had to take the `measure_distance` function, which wouldn't work because it would have to be perfectly aligned in time to work out. So I had to make it so that it doesn't return the distance. It has to save the distance in a list, and then I have to make another function to get the distance which just returns the list. And after doing that, I was finished with the sensors. Then I remembered that I should make a requirements.txt file, and after creating it I thought, "Nah, I'll do this when I'm finished with coding." And then I remembered that I should do also a stop function for the sensors and measuring, so stopping the task from the threading. For that, I had to make a new self variable named running to make it possible to make it stop running. And nOw the sensors are really finished. And I right away started with the take off....

Therefore, firstly I had to deactivate GPS, because it doesn't use GPS, with `master.set_mode('GUIDED_NOGPS')`.
And next I implemented a small 1 sec wait to ensure the mode is changed. Then I armed the drone -> activated the motor.
After that, the target altitude is changed from meters to millimeters, and the climbing speed is turned from positive to negative because positive speed in MAVLink is positive down, and the drone would push itself into the bottom.

And after that the ✨✨REAL TAKE-OFF✨✨ (I extra searched the sparkling emojis up...) comes, it's basically a while True loop with that MAVLink command:

```
master.mav.set_position_target_local_ned_send(
            0, # time_boot_ms
            master.target_system, master.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,
            0b0000110111000111, # type_mask (only vertical velocity is enabled)
            0, 0, 0, # x, y, z positions (not used)
            0, 0, climb_speed, # x, y, z velocity in m/s
            0, 0, 0, # x, y, z acceleration (not used)
            0, 0 # yaw, yaw_rate (not used)
        )
```

And the drone goes up until it reaches a position or higher of 95 percent of the target altitude, and it checks 10 times a second. And if it reaches the height, it goes over to ALT_HOLD, which means hold the altitude and just stay still. And after one second of waiting, the takeoff is finished.


Happy with today progress, but coding journals take SOOOOOO much longer, but nvm. Tomorrow I´ll add the camera feed and april tak the rest of the flight and servo motor!!!

### Recording Links

- https://lookout.hackclub.com/api/media/050301aa-a39c-486c-b63f-1865177f6c66/video.mp4

## Entry 29
- ID: 9622
- Author: Stefanos
- Created At: 2026-05-27T10:13:45Z

### Content

### 26. May: Coding the Apriltag tracking, servo and the battery status

Today I firstly wanted to make the camera and the april tag because for the next step in the flight I would need them, because for the movement I need to orient on the april tag.


1. I created a new file named camera.py, and then I saw in the AliExpress store that they explained how to use it and how to set it up, etc.

And because I also wanted to measure the distance from the april tag directly, I wanted to make both in parallel, and I found this awesome guide for the apriltags, from which I want to use some parts: https://pyimagesearch.com/2020/11/02/apriltag-with-python/

But then I got some issues with my venv, and actually the problem was that I forgot to add a # into my comment in the requirements.txt file.

After installing all the libraries again, I also made:
```
pip freeze > requirements.txt
```

the requirements.txt:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjA3MDksInB1ciI6ImJsb2JfaWQifX0=--55d8b93420bc8aa52a3f40a227139f37aaedd0e4/image.png)


and after making a commit it was perfect.

And I decided to first make only the april tag detection with my camera, and when it works, I’ll implement the resberry pi cam. For that I need to print out the april tag, but first I have to check how big it is allowed to be.

And after I found code in Python, it worked perfectly, and the april tag was completely found.


![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjA3MjIsInB1ciI6ImJsb2JfaWQifX0=--9dc47341465f4d26be2c083fadafeb227c37359b/image.png)


But I didn’t want to steal the code from the person, so I deleted most of it and started coding it myself.

So after reading a lot of other code, the documentation, and guides, I found out that you need argparse, and with the ArgumentParser and add_argument(), you can set arguments for the detection, like the width and height of the image, the family of the tag, so which tag should be searched, the nthreads, so how many threads should be used for the detection, and the quad_decimate. This is the factor by which the image is scaled, so it can get better results with higher values, but it takes longer.

I first coded it like this, but I got errors and it didn’t work:

```
import argparse
import cv2 as cv
from pupil_apriltags import Detector

# defining the arguments of the parser
ap = argparse.ArgumentParser()
ap.add_argument(
    "--width", type=int, default=640, help="the width of the video stream",
    "--height", type=int, default=480, help="the height of the video stream",
    "--family", type=str, default="tagCostum48h12", help="the family of the april tag to detect",
    "--nthreads", type=int, default=3, help="the number of threads to use for the detection (cpu cores)", # the resberry pi zero 2 W has 4 cores -> use 3 for the detection
    "--quad_decimate", type=float, default=1.5, help="decimate input image by this factor (lower means faster but less accurate detection)"
)

# pars the arguments
args = ap.parse_args()
```

And I decided to use these values because, after research, these were the best values for a micro computer like the resberry pi zero/w/2w.

But you have to actually make ap.add for every argument itself.

And after fixing that, the text was this:

```

import argparse
import cv2 as cv
from pupil_apriltags import Detector

# defining the arguments of the parser
ap = argparse.ArgumentParser()
ap.add_argument("--width", type=int, default=640, help="the width of the video stream")
ap.add_argument("--height", type=int, default=480, help="the height of the video stream")
ap.add_argument("--families", type=str, default="tagCostum48h12", help="the family of the april tag to detect")
ap.add_argument("--nthreads", type=int, default=3, help="the number of threads to use for the detection (cpu cores)") # resberry pi zero 2 W has 4 cores, so using 3 of them for detection
ap.add_argument("--quad_decimate", type=float, default=1.5, help="decimate input image by this factor")

# pars the arguments
args = ap.parse_args()

```

Then I set up the camera, and this part was easy because I used cv2 often in previous projects. I set the camera firstly to 1 (the second cam, because I have multiple cameras), and then set the camera height with the argparser argument parser.

```
# setup the camera
cap = cv.VideoCapture(1)
cap.set(cv.CAP_PROP_FRAME_WIDTH, args.width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, args.height)
```

Then I set up the detector with the corresponding arg families, nthreads, and quad_decimate.

```
# setup the april tag detector
at_detector = Detector(
    families=args.families, 
    nthreads=args.nthreads, 
    quad_decimate=args.quad_decimate
)
```

And then I continued with the real detection with a while loop.
It first reads the frame, converts the image into gray for optimal detection, and then detects the tags and prints their position.

```
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
```

But during testing it was really hard to see through the camera, so I decided to add an option that a window pops up to see the stream.

But then I understood why I got those weird coordinates, and when I was holding the apriltag in the middle of the camera it displayed something like 200 and 300 for x/y, but that didn’t make sense. So then I understood that 0, 0 was in the left bottom corner.
And currently I only had the x and y coordinates, but I also need the angle, so that the drone knows in which direction it has to yaw, and also for fun the distance.

Then I wanted to make the yaw angle, so that the drone knows how to rotate so it lands correctly, and therefore you can convert the rotation from matrix to euler.

And now, where the system works, I deleted all the stuff that I didn’t need, like the roll and pitch, but I didn’t need the estimated x and y meters.

And after that I had to make, like in the tof sensor, a class with threading, because it has to run in the background. So I created the class camera, moved most settings into the init function, made a start and stop function, made a get data function, and a running variable to start and stop the process. And now I’ll make it so I can use the resberry pi camera, and actually I only had to change the cam from 1 to 0 for the default, and the cam was finished!!!

Next I continued on the servo motor, which should be much easier.

I firstly used the normal servo from the library gpiozero, but I quickly realized, after reading the documentation, that you could only give it the normal servo max, middle or min. But with AngularServo you could give an angle, which is much better and is what I will do. Then I made the code into 2 functions. The first one calibrates the servo, which moves the servo in the setup at the beginning before takeoff to angle 0 and waits one second. Then, at the move_servo function, the servo is moved when the angle that is given is in the safe area, and if not, the max or min value is used.

```
from gpiozero import AngularServo
import time

# the gpio pin for the servo
gpio_pin = 18 

# safe angle range for the servo
min_angle = -90
max_angle = 90

# define the servo
servo = AngularServo(gpio_pin, min_angle=min_angle, max_angle=max_angle)

def calibrate_servo():
    # calibrate the servo
    servo.angle = 0
    time.sleep(1)

def move_servo(angle):
    # confirm and potentially adjust the angle to be within the safe zone
    safe_angle = max(min_angle, min(max_angle, angle)) # ensure the angle is within the safe range

    # move the servo to desired angle
    servo.angle = safe_angle
```

And next I’ll do the battery_percentage.

Therefore I firstly created a new file called battery_status.py, then I added the adafruit_ads1x1115 library and initialized the i2c with the SCL and SDA pins and defined my ads.

Then I defined that pin AIN2 is the input from Cell 3, which is the voltage of the whole battery, so that I can later estimate the percentage. But because in the schematics I added a resistor to bring the voltage from max 12.6V down to under 3.3V, because the i2c only can handle up to 3.3V, after redoing the math.

Happy today with the progress, almost finished the backend!


### Recording Links

- https://lookout.hackclub.com/api/media/c5c3f37b-91ae-4aab-aa08-bbdf54183f9c/video.mp4

## Entry 30
- ID: 9861
- Author: Stefanos
- Created At: 2026-05-28T08:20:54Z

### Content

### 27. May: Finishing the drone code and starting with the server!

And after yesterday, after mostly finishing the battery status, I had to make it also threaded, because it should run in the background. So I firstly created a class named `Battery`, then I added all the defined parameters and variables with `self`, and then added the function `battery_status` with a `while self.running` loop like all the others before. Then I also made a current battery status variable, so that in `get_battery_percentage` you just return this one. I also made that the battery percentage only updates every 2 seconds because it is not that important to get information like 10 times per second.

Then I also made a function to start the thread and to stop it, and after the battery code was finished I wanted to write the description of the scripts in the firmware README and explain how it works etc. But for that I first wanted to read the submission docs for the design submit, so that I include everything. But after starting the README I thought that it would be smarter to make it after I am finished with also the main and the server.

So I continued by making in `Motor` the function so that the drone, after it took off, can move around like to the front, left, right etc.

I made 4 (3 real) parameters:

```python
def move_drone(master, direction="front", speed=0.5, distance=1.0):
    """
    :param direction: the direction in which the drone should move, can be "front", "back", "left" or "right"
    :param speed: the speed at which the drone should move in m/s
    :param distance: the distance the drone should move in meters
    """
```

and applied this style with the commands and params to all functions in this file and then also to the others.

After that, like in the takeoff function, I set the mode to no GPS so that it can be controlled manually. Then I coded that it checks whether the direction is front, back, left or right and sets the velocity x and y firstly for all to `0.0`, but then to the corresponding speed that was defined before and also the corresponding sensor is given.

Only if the user tells the drone to go back it returns, because the drone doesn’t have a sensor on the back. It gives a message and warning that the drone firstly has to yaw to make it.

But because the sensor can only measure for about 2 to 3 meters I had to implement an alternative way to measure where and when to stop the drone. Then I had the idea that I can predict the time that the drone takes and then make a timer. I calculate it simply by dividing the distance by the speed and then I get the predicted time and start the timer.

Then I make a `while True` loop for the real movement. Now I measure the elapsed time and the current distance. Then I check if the distance is reached, but if the sensor is not measuring correctly and gives output error codes like `8190`, `8191` or `0`, it checks the time and if it’s reached it breaks the loop. And if the current distance is equal or bigger than the distance it also breaks.

Then I added the local target for the drone and added that only horizontal velocity is possible and added `vx` and `vy`. After waiting per loop 100ms to ensure 10Hz, after the while loop it checks if it’s too close so that it goes a bit back so that it doesn’t collide with that, and after that it changes into altitude hold mode.

```python
def move_drone(master, direction="front", speed=0.5, distance=1.0, stopping_distance=0.5):
    """
    :param direction: the direction in which the drone should move, can be "front", "back", "left" or "right"
    :param speed: the speed at which the drone should move in m/s
    :param distance: the distance the drone should move in meters
    :param tof_sensors: the list of the tof sensors, which are used to measure the distance to the obstacles in the corresponding direction, and they are in the order of the channels (0, 1, 2, 3)
    :param stopping_distance: the distance at which the drone should stop in meters
    """

    # initialize the velocity values for the x and y direction
    vy, vx = 0.0, 0.0

    # activate the no_gps mode, to be able to control the drone without gps
    master.set_mode('GUIDED_NOGPS')
    time.sleep(1) # wait a bit to ensure the mode is changed

    if direction == "front":
        vy = speed
        sensor_index = 1
    elif direction == "back":
        vy = -speed
        sensor_index = None # we don't have a sensor facing backwards, so we can't measure the distance to obstacles in that direction, the drone has to yaw firstly and then it will move
        return
    elif direction == "left":
        vx = -speed
        sensor_index = 3
    elif direction == "right":
        vx = speed
        sensor_index = 0
    else:
        print("Invalid direction, please choose from 'front', 'back', 'left' or 'right'")
        return

    # calculate the time needed to move to the target distance with the given speed and time
    time_needed = distance / speed

    # start the timer to control the movement for the calculated time
    start_time = time.time()

    # here happens the real movement logic
    while True:
        elapsed_time = time.time() - start_time
        current_distance = tof_sensor.get_distances()[sensor_index]

        # if the sensor sends an error value, because the distance is too far, we rely on the time to control the movement
        if current_distance == 8190 or current_distance == 8191 or current_distance == 0:
            print("Distance measurement error, moving for the calculated time")

            # if the elapsed time is greater than or equal to the calculated time, we can stop the movement
            if elapsed_time >= time_needed:
                print(f"Reached target distance of {distance} meters")
                break

        # if the sensor sends valid distances, we use the distance control
        else:
            # if the current distance is less than or equal to the stopping distance, we stop the movement to avoid collision
            if current_distance <= distance*1000 or current_distance <= stopping_distance*1000:
                print(f"Reached stopping distance of {stopping_distance} meters, stopping to avoid collision")
                break

        # here happens the movement command
        master.mav.set_position_target_local_ned_send(
            0,
            master.target_system, master.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,
            0b0000111111000111,
            0, 0, 0,
            vx if 'vx' in locals() else 0, vy if 'vy' in locals() else 0, 0,
            0, 0, 0,
            0, 0
        )

        time.sleep(0.1)

    # if the drone is too close to an object, move backwards for a half second
    if current_distance <= stopping_distance*1000:
        print("Too close to an object, moving backwards for 0.5 seconds to avoid collision")
        master.mav.set_position_target_local_ned_send(
            0,
            master.target_system, master.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,
            0b0000111111000111,
            0, 0, 0,
            -vx if 'vx' in locals() else 0, -vy if 'vy' in locals() else 0, 0,
            0, 0, 0,
            0, 0
        )
        time.sleep(0.5)

    # now the drone has to hover in that position
    print("Entering hover mode")
    master.set_mode('ALT_HOLD')
    time.sleep(1)
```

Next, I continued with the yaw drone function. As input you put in the angle and the duration. From that I had to calculate the radians because MAVLink doesn’t take the angle directly. Then after using the `0b010111100111` mask, which only activates the yaw, I gave as input the yaw rate and lastly switched back into altitude hold mode.

```python
def yaw_drone(master, yaw_rate=90, duration=2):
    """
    Yaw the drone in a specific direction with a specific yaw rate for a specific time.

    :param yaw_rate: positive values for right and negative values for left in degrees
    :param duration: the time for which to yaw the drone in seconds
    """

    # activate the no_gps mode, to be able to control the drone without gps
    master.set_mode('GUIDED_NOGPS')
    time.sleep(1)

    # calculate the yaw rate in radians per second
    yaw_rate_rad_s = yaw_rate * (math.pi / 180)

    start_time = time.time()

    # here happens the real yawing logic
    while time.time() - start_time < duration:
        master.mav.set_position_target_local_ned_send(
            0,
            master.target_system, master.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,
            0b010111100111,
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
            0,
            yaw_rate_rad_s
        )
        time.sleep(0.1)

    print("Entering hover mode")
    master.set_mode('ALT_HOLD')
    time.sleep(1)
```

And lastly I wanted to make the `land_drone` function.

I firstly changed the guided mode to no GPS and made some basic settings.

Then I made the `while True` loop and created 3 phases. The first phase was for the yaw alignment and it works by making small moves and comparing it with the tolerance which is measured previously.

After trying out how much tolerance is possible I found out that 5 degrees are possible.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjE0NDMsInB1ciI6ImJsb2JfaWQifX0=--956c36d81481697aed710fa0914e78aadb9101ed/image.png)

And if it was aligned then the next phase started. The second phase aligns the x/y coordinates by also making small moves and a total tolerance of 10 pixels.

Lastly it was the landing phase, phase 3. There it goes slowly down with `0.25m/s` and goes to `10cm` over the ground measured by the ToF sensor and then the drone goes into LAND mode, which basically lets the drone down, but when it touches the ground it stops and disarms

```python

def land_drone(master, landing_speed=0.25):
    """
    Land the drone by using the distance to the ground from the downward facing sensor and the distance to the april tag from the camera, which is also facing downwards, to control the landing process.

    :param landing_speed: the landing speed in m/s
    """  
    # changing to GUIDED_NOGPS mode, to be able to control the drone without gps
    master.set_mode('GUIDED_NOGPS')
    time.sleep(1) # wait a bit to ensure the mode is changed

    # convert the landing speed to negative, because the mavlink takes negative values for climbing up and positive values for climbing down
    landing_speed = abs(landing_speed)

    x_centre = 320 # 640/2, because the camera resolution is 640x480
    y_centre = 240 # 480/2, becasue the camera resolution is 640x480

    yaw_tolerance = 5/2 # in degrees
    pixel_tolerance = 20/2 # in pixel

    phase = 1 # phase 1: align yaw, phase 2: align x and y, phase 3: landing

    while True:
        data = cam.get_data()

        x_pixel, y_pixel, z_meter, yaw = data
        vx, vy, vz, yaw_rate = 0.0, 0.0, 0.0, 0.0

        if not data or len(data) != 4:
            print("Tag data not valid or tag not detected, hovering in current position!")
            
            # hover in the current position
            master.mav.set_position_target_local_ned_send(
                0, master.target_system, master.target_component,
                mavutil.mavlink.MAV_FRAME_LOCAL_NED,
                0b010111000111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            )

            time.sleep(0.1)
            continue

        if phase == 1:
            if not abs(yaw) < yaw_tolerance:
                yaw_rate = yaw * 0.1

                yaw_rad = math.radians(yaw_rate)
                yaw_rate = yaw_rad

                yaw_rate = max(-0.5, min(0.5, yaw_rate))

            else:
                print("Yaw aligned, switching to phase 2")
                phase = 2

        elif phase == 2:
            error_x = x_pixel - x_centre
            error_y = y_pixel - y_centre

            if abs(error_x) > pixel_tolerance:
                vy = (error_x / 320) * 0.3
                vy = max(-0.25, min(0.25, vy))

            if abs(error_y) > pixel_tolerance:
                vx = -(error_y / 240) * 0.3
                vx = max(-0.25, min(0.25, vx))

            if abs(error_x) <= pixel_tolerance and abs(error_y) <= pixel_tolerance:
                print("X and Y aligned, switching to phase 3")
                phase = 3

        elif phase == 3:
            vz = abs(landing_speed)

            ground_distance = tof_sensor.get_distances()[2] / 1000 # convert to meters

            if ground_distance <= 0.1:
                print("Landed successfully!")
                break
        
        # using mask 0b010111000111, to aktivate vx, vy, vz and yaw_rate control and deactivate all other controls
        master.mav.set_position_target_local_ned_send(
            0, master.target_system, master.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,
            0b010111000111, 
            0, 0, 0,        # position
            vx, vy, vz,     # velocity 
            0, 0, 0,        # acceleration
            0, yaw_rate     # yaw-rate, yaw
        )

        time.sleep(0.1) # for the next command after 100ms becasue we have to keep 10Hz control of the drone

    master.set_mode('LAND')
    time.sleep(1) # wait a bit to ensure the mode is changed

```

And next I wanted to combine everything in the main and program a small flight where the drone takes off, yaws, goes one meter to the drone, turns, yaws, centers and lands. And exactly that I did.

```python

def flight_loop():
    # start the drone and get the connection to the flight controller and arm
    master = turn_on_drone()
    motor.arm_drone(master)
    
    # take off to 1 meter altitude
    motor.takeoff_drone(master, target_altitude=1.0)

    # fly forward for 1 meter and then back
    for _ in range(2):
        # rotate the drone by 180 degrees
        motor.yaw_drone(master, yaw_rate=180, duration=2)

        # fly forward for 1 meter
        motor.move_drone(master, direction="front", speed=0.5, distance=1.0, stopping_distance=0.20)

    # land the drone
    motor.land_drone(master, landing_speed=0.25)

    # shutdown the drone and disconnect from the flight controller
    shutdown_drone(master)
```

Then in the `main.py` file I added the other things like move servo, get ToF distances, get battery status or test motors etc.

Next I had to make the server and the website to connect the server with the commands.

Firstly I created the `main.py` file where I added just the code to display an HTML file in the frontend folder, with just “Hello World” on it.

Firstly I wanted to use Flask because I know it very well, but it’s a bit slow, and FastAPI, which I have never used before, would be worth it, so I read a bit of the docs to get into it.

Then I built the basic HTML structure.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjE1OTQsInB1ciI6ImJsb2JfaWQifX0=--17d41a2694669dafb1ca7dc8b8231c938d82151c/image.png)

Because I want to finish the project tomorrow and don’t want to spend 10 hours on the design, I let Claude make a nice CSS look for my drone and after that I will do the frontend/backend connection myself. I used Antigravity because I anyway wanted to try it out.

After writing a prompt that basically said to make a CSS/JS minimalistic design for the HTML structure that I designed myself, it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjE2MTIsInB1ciI6ImJsb2JfaWQifX0=--11cc96e503ec6a44e1956aeae581094809baf2a4/image.png)

I pretty liked it, I just wanted that everything had to be visible without scrolling and there were some bugs, like the servo showed 90 degrees although it was at 0 degrees, but that should be fast to fix.

And after fixing that it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjE2MjQsInB1ciI6ImJsb2JfaWQifX0=--516df00319680de01441ff435b69ab0f48129765/image.png)

And now I have to make the connection with the backend over an API. So I started by making the `server/main.py`. Therefore I wanted to make the direct API from the Raspberry Pi to the drone. So I made the direct connection to the Pi, but it got late and I’ll continue in the morning and hopefully finish the design tomorrow!


### Recording Links

- https://lookout.hackclub.com/api/media/bff8c5a2-1af6-42c6-a57f-a04d9bafd6cd/video.mp4

## Entry 31
- ID: 9891
- Author: Stefanos
- Created At: 2026-05-28T12:18:43Z

### Content

### 28. May: Finishing the Firmware!

I decided to not use UDP because I don’t need such a fast connection and it’s too risky to lose packages, so I decided to use requests and a REST API for the following things:

I started with the telemetry API where the drone sends the data that is then just displayed, like the battery percentage and the 4 distances from the ToF sensors, which are divided by 10 so that they get converted from mm to cm.

Then I added the command requests for starting the flight, stopping the drone, testing the motors, and moving the servo.

```python
# -- API commands ---

@app.post("/api/drone/start")
def start_drone():
    try:
        response = requests.post(f"{pi_url}/drone/start", timeout=1)
        return response.json()
    except Exception as e:
        print(f"Error occurred while starting the drone: {e}")
        return {"status": "error", "message": "Failed to start the drone and to reach the raspberry pi"}
    
@app.post("/api/drone/stop")
def stop_drone():
    try:
        response = requests.post(f"{pi_url}/drone/stop", timeout=1)
        return response.json()
    except Exception as e:
        print(f"Error occurred while stopping the drone: {e}")
        return {"status": "error", "message": "Failed to stop the drone and to reach the raspberry pi"}
    
@app.post("/api/flight/start")
def start_flight():
    try:
        response = requests.post(f"{pi_url}/flight/start", timeout=1)
        return response.json()
    except Exception as e:
        print(f"Error occurred while starting the flight: {e}")
        return {"status": "error", "message": "Failed to start the flight and to reach the raspberry pi"}
    
@app.post("/api/servo/move")
def move_servo(command: ServoCommand):
    try:
        response = requests.post(f"{pi_url}/servo/move", json={"angle": command.angle}, timeout=1)
        return {"status": "success", "message": f"Servo moved to {command.angle} degrees"}
    except Exception as e:
        print(f"Error occurred while moving the servo: {e}")
        return {"status": "error", "message": "Failed to move the servo and to reach the raspberry pi"}
    
@app.post("/api/motor/test")
def test_motor(command: MotorTestCommand):
    try:
        response = requests.post(f"{pi_url}/motor/test", json=command.dict(), timeout=1)
        return {"status": "success", "message": f"Motor {command.motor_number} tested with throttle {command.throttle} for {command.duration} seconds"}
    except Exception as e:
        print(f"Error occurred while testing the motor: {e}")
        return {"status": "error", "message": "Failed to test the motor and to reach the raspberry pi"}
```

And then I started implementing the API endpoints in the main file of the drone. Therefore, I firstly started a FastAPI server to send and access the API, and then I simply created POST and GET endpoints and returned the output of the corresponding functions that were already in the main.py file of the drone.

I thought that the whole flight should run in a background task because it could take up to 1 minute and would completely stop the API POST and GET flow with the cockpit. So after searching online, I found out that FastAPI has a tool called BackgroundTasks, which lets users run tasks in the background, and that is exactly what I used:

```python
@app.post("/api/flight/start")
def api_start_flight():
    try:
        # add a bg task to ensure the api loop keeps running while the flight loop is executed in the background
        fastapi.background_tasks.add_task(flight_loop)
        return {"status": "Flight started successfully"}
    except Exception as e:
        print(f"Error occurred while starting the flight: {e}")
        return {"status": "Failed to start flight"}
    
```

And now I only had to connect the server with the HTML website.

Therefore, I firstly looked online how to do that, and it’s actually pretty simple. You just have to write in the JS file which object, text, button, slider, etc. you want to use and what data it should show based on the API or which data it should send.

So I started with the connected symbol at the top to check if the drone is connected with the server.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjE5MzYsInB1ciI6ImJsb2JfaWQifX0=--1f25562b50229684f65fece2e7ab1247175f353c/image.png)

And after adding all the other stuff that I listed previously, I was finished with the coding part. But then I had the idea that you could input the IP of the drone in the cockpit so that it would be easier to access and more user friendly. So I quickly added a new button and again connected it with the backend to change the pi_ip variable.

I also then decided to automatically check which IPs are connected with the network, and then it looked like that after letting Claude improve the style a bit.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjE5NTMsInB1ciI6ImJsb2JfaWQifX0=--6940301c303503820254e1f517dda8a3c22a5433/image.png)

Happy that I’m finished with coding and basically with the project. I now only have to make the zine, upload everything to GitHub, and write the README.


### Recording Links

- https://lookout.hackclub.com/api/media/cda1665e-2cec-4157-9d76-59990af87547/video.mp4

## Entry 32
- ID: 10088
- Author: Stefanos
- Created At: 2026-05-29T09:02:40Z

### Content

### 28. Starting with the CAD organisation and making the render

Now I wanted to perfectly organize my GitHub repo and therefore I created, besides the firmware folder, also a PCB folder and a CAD folder. But I also wanted to check out approved and good projects to see how they did that, and after checking out other projects I decided to also make an image folder for all images.

But first I wanted to export all PCB files:

So I added the .kicad_pcb, .kicad_pro, .kicad_sch and gerbers.zip with the drill and gerber files.

Then I wanted to make the CAD files and that was a PAIN!

I firstly had to add all parts into one file and also the parts that I’ll buy, and the problem was that for some parts like the FC or battery I didn’t find any models, that’s why I had to add them myself. And after adding all, downloading, extracting them etc. it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjIwNTYsInB1ciI6ImJsb2JfaWQifX0=--900c2729c02053537dc75d7a5878138109d47b70/image.png)

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjIwNTcsInB1ciI6ImJsb2JfaWQifX0=--bf6a06457112adc7785ef13db91e7ea2a3589bac/image.png)

But I had some problems. The prop guards were a bit too high.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjIwNTgsInB1ciI6ImJsb2JfaWQifX0=--e33ffc04b0dc745b2a535f8169cfe30036592b8c/image.png)

And the ToF sensor holder had the stilts too far apart:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjIwNTksInB1ciI6ImJsb2JfaWQifX0=--3d01760fb8afa1caeeda38b43769f8245bced4e8/image.png)

Also I had the problem that the stilts were touching the camera cable from the Raspberry Pi, so I had to move that one further up.

So I started with the 2 ToF problems, but I quickly realized that for one of them I also had to move the hole.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjIwNjIsInB1ciI6ImJsb2JfaWQifX0=--b99c0d4beb3257c37169557643f294ff76e0ba4a/image.png)

So after fixing it, it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjIwNjUsInB1ciI6ImJsb2JfaWQifX0=--19d271199cf84c0962dc3e751771ceb448d68c20/image.png)

And after fixing the 2 errors it looked like that:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjIwODcsInB1ciI6ImJsb2JfaWQifX0=--9116a8bcb3a55a7442014c3248744c3be86fbab8/image.png)

And after moving the prop guards more down they were perfect.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjIwOTksInB1ciI6ImJsb2JfaWQifX0=--ea9901fd888a04321abf8fd20d1513be17a0dfbd/image.png)

I wanted one more thing, because I was afraid that there would be too much heat at the PCB etc. I decided to make small cuts at the bottom of the case so that air can go through and the parts don’t get that hot. I only had to pay attention that the stilts had a good connection and weren’t floating in the air.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjIyMjgsInB1ciI6ImJsb2JfaWQifX0=--bb8ef847ae750825ca80abe604d1a68545c1615d/image.png)

Then I thought I would need some airflow regulation, so I added some cuts at the front on both sides so that the air powered by the propellers can go through it.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjIyMjksInB1ciI6ImJsb2JfaWQifX0=--1b3b5206b6d9077f72055f62a987253f0bcab992/image.png)

And lastly I thought that the battery can get really hot too, so I also added cuts there.

And finally I was finished with the assembled file and then I checked again which files were needed for the submission.

So the single parts as STEP, a fully assembled file and an .f3d file.

But then the render took my attention and I focused on that first.

After positioning everything I also added the landing station for better demonstrating it in the zine poster.

I decided to use the colors purple/blue and light green inspired by Neon Genesis Evangelion. I decided to make the small parts like the guard protectors, the camera holder and the cover green and use blue/purple as the base color. I also decided to make some faces of the landing station green to bring a bit more color and action into it.

I also decided to make the AprilTag holder green, and after checking which background looks the best I decided to use a classic background with 2 lights. I also wanted to use shadows and reflections with almost no roughness for a cool picture and after trying multiple poses I decided on this one:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI3NjMsInB1ciI6ImJsb2JfaWQifX0=--f70d745968bf4f7c1a92c459bccfaeb2ba9f4e8f/image.png)

And my vision for the zine poster was this:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI3NjQsInB1ciI6ImJsb2JfaWQifX0=--fc7bb7ea0442b62d2b8ca5be039dabb5adaea1a0/image.png)

But I SAW THAT I FORGOT TO ADD the camera in the render and after finally finding one I also had to design a case, and I decided to make a slide in case.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI3NjUsInB1ciI6ImJsb2JfaWQifX0=--461ae80ec00be1de133eff00ac57d62594c62aef/image.png)

And after trying a lot with the settings and the resolution it looked like that after also adding the camera:

![All-together\_2026-May-29\_08-23-26AM-000\_CustomizedView5026933682\_jpg.jpg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI3NjksInB1ciI6ImJsb2JfaWQifX0=--a9504300c9fc6036a4c5708470af221a8fbfc1f2/All-together_2026-May-29_08-23-26AM-000_CustomizedView5026933682_jpg.jpg)

Happy with the progress, just got at the end a bit away from the main way, but also finished the render!


### Recording Links

- https://lookout.hackclub.com/api/media/9f46398a-7192-45db-bab8-814c90d1d2d0/video.mp4
