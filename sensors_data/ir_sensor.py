import RPi.GPIO as GPIO

# Use Pins as per GPIO board 
GPIO.setmode(GPIO.BOARD)

# Take input from GPIO pin 3
GPIO.setup(3, GPIO.IN)

def get_ir_value():
    val = GPIO.input(3)  # Get sensor value
    return {"ir_value": val} # return sensor value


