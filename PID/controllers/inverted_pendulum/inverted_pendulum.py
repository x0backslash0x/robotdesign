"""Sample Webots controller for the inverted pendulum benchmark."""
from controller import Robot
import math #used for angle [RAD] calculations
import matplotlib.pyplot as plt #used to create a plot
import datetime as dt #used to create the plot time based x-axis

#region PID controller class



#endregion

def defRobot(robot):
    #region --Get the time step of the current world
    varTimestep = int(robot.getBasicTimeStep())
    #endregion

    #region --Initialize pendulum angle sensor

    #endregion

    #region --Initialize the motors and retrieve the max. speed

    varMaxSpeed = min(devRiMotor.getMaxVelocity(), devLeMotor.getMaxVelocity())
    #endregion

    # region --Initialize PID controller

    #endregion

    #region -- Initialize plot lists
    lstAngleValues = []
    lstTimeValues = []
    lstSpeedValues = []
    #endregion

    # Main loop: perform a simulation step until the simulation is over.
    while robot.step(varTimestep) != -1:
        #region --Readout the angle sensor

        #endregion

        #region --Stop the robot when the pendulum falls.
        if math.fabs(varSensAngle_RAD) > math.pi * 0.5:
            devLeMotor.setVelocity(0.0)
            devRiMotor.setVelocity(0.0)
            break
        #endregion

        #region --PID control

        #endregion

        #region --Set the robot varSpeed (left wheel, right wheel).

        #endregion

        #region --Store the angle, speed and time values into the lists

        lstTimeValues.append(dt.datetime.now())

        #endregion

    #region --Plot diagram when pendulum falls
    # X= Time values
    # Y= Angle values
    # The number of measuring points between X and Y must be equal


    #endregion

#region --Main loop
if __name__ == "__main__":
    myRobot = Robot()
    defRobot(myRobot)
#endregion