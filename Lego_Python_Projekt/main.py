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

# Write your program here.
gyro.reset_angle(0)
while robot.distance() <= 1000:
    correction = (0 -gyro.angle()) * 2
    robot.drive(200, correction)
robot.stop()
motor_left.brake()
motor_right.brake()
