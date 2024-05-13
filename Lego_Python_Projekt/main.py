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
# Resets the Gyro Sensor.
def gyroReset():
    gyro.reset_angle(0)
    while True:
        if gyro.angle() == 0:
            break
    while True:
        if gyro.speed() == 0:
            break

# Drive forward or backward.
def gyroStraight(distance, speed):
    target = gyro.angle()
    gain = 0
    robot.reset()

    while robot.distance() < distance:
        correction = target - gyro.angle()
        turn_power = correction * gain

        robot.drive(speed, turn_power)
    robot.stop()
    motor_left.brake()
    motor_right.brake()

# Turn right or left.
def gyroTurn(degrees):
    gyroReset()

    robot.turn(degrees)
    robot.stop()

# Here is the programm.
gyroStraight(500, 100)
gyroTurn(90)
gyroStraight(500, 100)
gyroTurn(90)
gyroStraight(500, 100)
gyroTurn(90)
gyroStraight(500, 100)
gyroTurn(90)

