from os import path
import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pymavlink import mavutil

app = FastAPI()

if path.exists("frontend"):
    app.mount("/static", StaticFiles(directory="frontend"), name="static")

templates = Jinja2Templates(directory="frontend")

pi_ip = "11.22.33.44" # replace with the actual ip address of the pi
pi_url = f"http://{pi_ip}:5000/api"

master = None

def get_laptop_drone_connection():
    global master
    if master is None:
        master = mavutil.mavlink_connection("udpin:0.0.0.0:14550")
    return master

class ServoCommand(BaseModel):
    angle: int

class MotorTestCommand(BaseModel):
    motor_number: int
    throttle: float
    duration: float

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/api/get_data")
def get_data():
    # set battery status
    battery_percentage = 0
    battery_connection = False

    drone = get_laptop_drone_connection()
    msg = drone.recv_match(type='SYS_STATUS', blocking=False)
    if msg is not None:
        battery_percentage = msg.battery_remaining
        battery_connection = True

