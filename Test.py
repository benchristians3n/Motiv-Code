import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# Motor driver pins
IN1 = 17
IN2 = 19
ENA = 21  # For PWM speed control (optional)

# Set GPIO pins as output
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

# Set PWM frequency for motor speed control (optional)
pwm = GPIO.PWM(ENA, 1000)  # 1000 Hz frequency
pwm.start(0)  # Start PWM with 0% duty cycle (off)

# Function to move motor forward
def move_forward(speed=100):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(speed)  # Set motor speed

# Function to move motor backward
def move_backward(speed=100):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm.ChangeDutyCycle(speed)  # Set motor speed

# Function to stop motor
def stop_motor():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)  # Stop motor by setting duty cycle to 0

# Test the motor control
try:
    print("Moving forward...")
    move_forward(speed=75)  # Move forward at 75% speed
    time.sleep(5)  # Move forward for 5 seconds
    
    print("Moving backward...")
    move_backward(speed=75)  # Move backward at 75% speed
    time.sleep(5)  # Move backward for 5 seconds
    
    print("Stopping motor...")
    stop_motor()  # Stop motor

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
