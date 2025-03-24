"""Elisa_bumper controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from math import atan2

#=============================================================
#Global vars
#=============================================================
varMaxSpeed = 6.28
varTimeStep = 32

#=============================================================
#Function:Robot Control
#=============================================================
def defRobotControl(robot):
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  motor = robot.getDevice('motorname')
    #  ds = robot.getDevice('dsname')
    #  ds.enable(timestep)
    
    #Enable left motor
    devMotLe = robot.getDevice('left wheel motor')
    devMotLe.setPosition(float('inf'))
    devMotLe.setVelocity(0.0)
    
    #Enable right motor
    devMotRi = robot.getDevice('right wheel motor')
    devMotRi.setPosition(float('inf'))
    devMotRi.setVelocity(0.0)
    
    #Enable bumper sensor
    devBumper = robot.getDevice('touch sensor')
    devBumper.enable(varTimeStep)

    #Enable compass
    devCompass = robot.getDevice('compass')
    devCompass.enable(varTimeStep)

    #Enable arrow
    devNeedle = robot.getDevice('arrow')
    
    
    #Reset velocity of both wheels
    varSpeedLe = 0.0
    varSpeedRi = 0.0
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(varTimeStep) != -1:
        #Move forward
        varSpeedLe = varMaxSpeed * 0.25
        varSpeedRi = varMaxSpeed * 0.25
     
        # Read the bumper sensors
        print(devBumper.getValue())
        if devBumper.getValue() == 1.0:
            varSpeedLe = -varMaxSpeed*0.25
            print("Turning left")
            print(devBumper.getValue())

        # Read the compass
        varNorth = devCompass.getValues()
        # Read the arrow
        varAngle = atan2(varNorth[1], varNorth[0])
        devNeedle.setPosition(varAngle)
    
        # Control the motors
        devMotLe.setVelocity(varSpeedLe)
        devMotRi.setVelocity(varSpeedRi)
        
#=============================================================
#POU:Main
#=============================================================
if __name__ == "__main__":
    
    #Create the Elisa robot instance
    myRobot = Robot()
    defRobotControl(myRobot)
    
