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
