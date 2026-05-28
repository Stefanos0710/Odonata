
"""
1. make ssh connection with the drone
2. install mav proxy
3. setup fc wiht mission planner, to enable the UR ports
4.  set the boud rate to 115200 +set the protocol to mavlink 2
5. make the connection between the pi and fc: 
    1. ssh connection to the pi
    2  cd .local/bin
    3.  python3 mavproxy.py -- master=/dev/serial0 -- baudrate 115200 -- aircraft MyCopter       <-- install maxproxy 
"""
# drone imports
from pymavlink import mavutil
from firmware.drone import motor, servo, camera, battery_status, tof_sensor
import time

# server imports
import fastapi
import uvicorn
from fastapi import FastAPI, BackgroundTasks, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
import uuid

try:
    from aiortc import RTCPeerConnection, RTCSessionDescription
    from firmware.drone.camera import CameraTrack
except ImportError:
    RTCPeerConnection = None
    RTCSessionDescription = None
    CameraTrack = None

# RTCPeerConnection handling
pcs = set()

# Initialize camera
cam = camera.Camera()
cam.setup()
cam.start()

# -- Functions to interact with the drone ---

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

def get_battery_status():
    return battery_status.get_battery_percentage()

def move_servo(angle):
    # move the servo to the desired angle
    servo.move_servo(angle)

def get_tof_distances():
    return tof_sensor.get_distances()

def test_motors(master, motor_number, throttle_value, time_seconds):
    motor.test_motor(master, motor_number, throttle_value, time_seconds)

def turn_on_drone():
    # build the connection to the flight controller
    master = mavutil.mavlink_connection('/dev/serial0', baud=115200)  

    # wait until the first heartbeat is received
    master.wait_heartbeat()
    print("Successfully connected to the flight controller")

    # here comes the logic of the drone

    return master

def shutdown_drone(master):
    """Shut down the drone"""
    # disconnet the motors
    master.arducopter_disarm()

    print("finished!")

    # disconnect the connection to the flight controller
    master.close()


# -- API endpoints ---

app = FastAPI()

class ServoCommand(BaseModel):
    angle: int

class MotorTestCommand(BaseModel):
    motor_number: int
    throttle: float
    duration: float

@app.get("/api/telemetry")
def api_get_telemetry():
    battery = 0
    try:
        battery = get_battery_status()
        tof = get_tof_distances()
    except Exception as e:
        print(f"Error occurred while fetching telemetry: {e}")
        return {
            "battery": battery,
            "tof": {
                "right": 0,
                "front": 0,
                "bottom": 0,
                "left": 0
            }
        }
    
    return {
            "battery": battery, 
            "tof": {
                "right": tof["right"],
                "front": tof["front"],
                "bottom": tof["bottom"],
                "left": tof["left"]
            }
        }

@app.post("/api/drone/start")
def api_start_drone():
    try:
        master = turn_on_drone()
        motor.arm_drone(master)
        return {"status": "Drone started successfully"}
    except Exception as e:
        print(f"Error occurred while starting the drone: {e}")
        return {"status": "Failed to start drone"}
    
@app.post("/api/drone/stop")
def api_stop_drone():
    try:
        master = turn_on_drone()
        shutdown_drone(master)
        return {"status": "Drone stopped successfully"}
    except Exception as e:
        print(f"Error occurred while stopping the drone: {e}")
        return {"status": "Failed to stop drone"}
    
@app.post("/api/flight/start")
def api_start_flight():
    try:
        # add a bg task to ensure the api loop keeps running while the flight loop is executed in the background
        fastapi.background_tasks.add_task(flight_loop)
        return {"status": "Flight started successfully"}
    except Exception as e:
        print(f"Error occurred while starting the flight: {e}")
        return {"status": "Failed to start flight"}
    
@app.post("/api/servo/move")
def api_move_servo(command: ServoCommand):
    try:
        move_servo(command.angle)
        return {"status": f"Servo moved to angle {command.angle} successfully"}
    except Exception as e:
        print(f"Error occurred while moving the servo: {e}")
        return {"status": "Failed to move servo"}
    
@app.post("/api/motor/test")
def api_test_motor(command: MotorTestCommand):
    try:
        master = turn_on_drone()
        test_motors(master, command.motor_number, command.throttle, command.duration)
        shutdown_drone(master)
        return {"status": "success"}
    except Exception as e:
        print(f"Error occurred while testing the motor: {e}")
        return {"status": "Failed to test motor"}

class WebRTCOffer(BaseModel):
    sdp: str
    type: str

@app.post("/api/webrtc/offer")
async def webrtc_offer(offer: WebRTCOffer):
    if RTCPeerConnection is None:
        return JSONResponse(content={"error": "aiortc is not installed"}, status_code=500)
    
    pc = RTCPeerConnection()
    pcs.add(pc)

    @pc.on("connectionstatechange")
    async def on_connectionstatechange():
        print(f"Connection state is {pc.connectionState}")
        if pc.connectionState == "failed" or pc.connectionState == "closed":
            await pc.close()
            pcs.discard(pc)

    # Add the camera video track
    video_track = CameraTrack(cam)
    pc.addTrack(video_track)

    desc = RTCSessionDescription(sdp=offer.sdp, type=offer.type)
    await pc.setRemoteDescription(desc)
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return JSONResponse(
        content={"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}
    )

@app.on_event("shutdown")
async def on_shutdown():
    # close all peer connections
    coros = [pc.close() for pc in pcs]
    import asyncio
    await asyncio.gather(*coros)
    cam.stop()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)