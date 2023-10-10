from gpiozero import AngularServo
from time import sleep

# Define servo objects for each servo
s1 = AngularServo(2,min_pulse_width=0.0006,max_pulse_width=0.0023)
s2 = AngularServo(3,min_pulse_width=0.0006,max_pulse_width=0.0023)
s3 = AngularServo(4,min_pulse_width=0.0006,max_pulse_width=0.0023)
s4 = AngularServo(5,min_pulse_width=0.0006,max_pulse_width=0.0023)
s5 = AngularServo(6,min_pulse_width=0.0006,max_pulse_width=0.0023)
s6 = AngularServo(7,min_pulse_width=0.0006,max_pulse_width=0.0023)

s1.angle = -90
s2.angle = 0
s3.angle = 0
s4.angle = -90
s5.angle = -90
s6.angle = -90
sleep(3)
s1.angle = 0
s2.angle = 90
s3.angle = 90
s4.angle = 0
s5.angle = 0
s6.angle = 0
sleep(3)


def rotate(pin, angle):
    print(pin, angle)

    if pin == 2:
        if(angle == 1):
            s1.angle = -90
        else:
            s1.angle = 0
    elif pin == 3:
        if(angle == 1):
            s2.angle = 0
        else:
            s2.angle = 90
    elif pin == 4:
        if(angle == 1):
            s3.angle = 0
        else:
            s3.angle = 90
    elif pin == 5:
        if(angle == 1):
            s4.angle = -90
        else:
            s4.angle = 0
    elif pin == 6:
        if(angle == 1):
            s5.angle = -90
        else:
            s5.angle = 0
    elif pin == 7:
        if(angle == 1):
            s6.angle = -90
        else:
            s6.angle = 0
    else:
        return
        
def run(brailleCode):
    while True:
        positions = brailleCode
        
        for i in range(len(positions)):
            pin = 2
            for pos in positions[i]:
                rotate(pin, int(pos[0]))
                pin += 1
                rotate(pin, int(pos[1]))
                pin += 1
            sleep(5)
        break;
            
