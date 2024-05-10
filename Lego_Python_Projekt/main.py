#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = EV3Brick()
motor_left = Motor(Port.B)
motor_right = Motor(Port.C)
color = ColorSensor(Port.S3)
gyro = GyroSensor(Port.S2)
# The wheel diameter is 54 mm and the axle track is 132 mm.
robot = DriveBase(motor_left, motor_right, wheel_diameter = 54, axle_track = 132)

# This are the definitions.
def moveDistanceInMMforward(distance):
 robot.straight(distance)

def moveDistanceInMMbackward(distance):
    moveDistanceIn(-1*distance)

def moveDistanceIn(distance):
    robot.straight(distance)

def setting ():
    robot.settings(250)

def fullStop():
    robot.stop()
    motor_left.brake()
    motor_right.brake()

def turnAngleLeft(angle):
    turnAngle(-1*angle)

def turnAngleRight(angle):
    turnAngle(angle)

def turnAngle(angle):
    robot.turn(angle)

# Here is the programm.
setting()
moveDistanceInMMforward(500)
turnAngleRight(180)
moveDistanceInMMforward(500)


print(gyro.angle())
print(robot.distance())
