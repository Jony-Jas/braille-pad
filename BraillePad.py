from gpiozero import Servo
from time import sleep

# Define servo objects for each servo
s1 = Servo(2)
s2 = Servo(3)
s3 = Servo(4)
s4 = Servo(5)
s5 = Servo(6)
s6 = Servo(7)

def rotate(servo, angle):
    # Convert the angle from 0-90 to -1 to 1 (gpiozero servo range)
    servo.value = (angle / 90.0) * 2 - 1

# Main setup
for servo in [s1, s2, s3, s4, s5, s6]:
    servo.min()
    sleep(1)

for servo in [s1, s2, s3, s4, s5, s6]:
    servo.max()
    sleep(1)

# Loop
while True:
    positions = [(1, 1), (0, 1), (0, 0)]

    pin = 2
    for pos in positions:
        rotate(s1, pos[0] * 90)
        pin += 1
        rotate(s2, pos[1] * 90)
        pin += 1

    sleep(2)
