from os import path
import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pymavlink import mavutil

import requests

app = FastAPI(title="Drone Control Cockpit")


# define the frontend
if path.exists("frontend"):
    app.mount("/static", StaticFiles(directory="frontend"), name="static")

templates = Jinja2Templates(directory="frontend")


# defining the API adresses of the drone
pi_ip = ""
pi_url = f"http://{pi_ip}:5000/api"

class ServoCommand(BaseModel):
    angle: int

class MotorTestCommand(BaseModel):
    motor_number: int
    throttle: float
    duration: float

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request, "index.html")

# -- API telemetry ---
def get_telemetry():
    try:
        response = requests.get(f"{pi_url}/telemetry", timeout=1)
        data = response.json()

        # tof data
        pi_tof = data.get("tof", [0, 0, 0, 0])

        # 
        return {
            "battery": data.get("battery", 0),
            "tof": {
                "right": pi_tof[0] / 10, # convert from mm to cm
                "front": pi_tof[1] / 10,
                "bottom": pi_tof[2] / 10,
                "left": pi_tof[3] / 10
            }
        }
    except Exception as e:
        print(f"Error occurred while fetching telemetry: {e}")
        return {
            "battery": 0,
            "tof": {
                "right": 0,
                "front": 0,
                "bottom": 0,
                "left": 0
            }
        }

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