import datetime
from pymongo import MongoClient
import RPi.GPIO as GPIO
import time

mongo_client = MongoClient('mongodb://localhost:27017')
db = mongo_client.raspi
col = db.ir


GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.IN)

while True:
    val = GPIO.input(3)
    res = col.insert({"time": datetime.datetime.utcnow(), "value": val})
    print("Result", res)
    if val == 1:
     print("Object Detected")
    else:
     print("No Object")
    time.sleep(.5)
