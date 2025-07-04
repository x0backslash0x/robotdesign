"""Elisa_bumper controller."""

from controller import Robot

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

    #Enable battery sensor
    robot.batterySensorEnable(varTimeStep)
    
    #Reset velocity of both wheels
    varSpeedLe = 0.0
    varSpeedRi = 0.0

    # - perform simulation steps until Webots is stopping the controller
    while robot.step(varTimeStep) != -1:
        #Move forward
        varSpeedLe = varMaxSpeed
        varSpeedRi = varMaxSpeed

        #Read the battery state
        print(robot.batterySensorGetValue())
     
        if devBumper.getValue() == 1.0:
            varSpeedLe = -varMaxSpeed
            print("Turning left")
            print(devBumper.getValue())
    
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
