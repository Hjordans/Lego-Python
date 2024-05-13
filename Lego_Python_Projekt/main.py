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
# These are the forward and backward settings.
def moveDistanceInMMforward(distance):
 moveDistanceIn(distance)
 fullStop()

def moveDistanceInMMbackward(distance):
    moveDistanceIn(-1*distance)
    fullStop()

def moveDistanceIn(distance):
    robot.straight(distance)

# This stops the Robot.
def fullStop():
    robot.stop()
    motor_left.brake()
    motor_right.brake()

# Here are the speed settings.
def setting(speed):
    robot.settings(speed)

# The angles settings for turning.
def turnAngleLeft(angle):
    turnAngle(-1*angle)
    gyroCorrection()

def turnAngleRight(angle):
    turnAngle(angle)
    gyroCorrection()

def turnAngle(angle):
    robot.turn(angle)

def gyroCorrection(turnAngleLeft, turnAngleRight):
    if turnAngleLeft() > 0:
        gyroCorrection - turnAngleLeft()
        gyroReset()
    else:
        gyroCorrection - turnAngleRight()
        gyroReset()

def gyroReset():
    gyro.reset_angle(0)

# Here is the programm.
setting(150)
moveDistanceInMMforward(500)
turnAngleRight(180)
moveDistanceInMMforward(500)


print(gyro.angle())
print(robot.distance())
