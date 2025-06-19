"""Sample Webots controller for the inverted pendulum benchmark."""
from controller import Robot
import math #used for angle [RAD] calculations
import matplotlib.pyplot as plt #used to create a plot
import datetime as dt #used to create the plot time based x-axis

#region initialize variables
varNameRiMotor = 'right wheel motor'
varNameLeMotor = 'left wheel motor'
varNamePendulum = 'pendulum sensor'
varMotorRotatePosition = float('inf') # spins the motor infinitely
varVelocityStopped = 0.0
#endregion

#region PID controller class
class PID_Controller:
    def __init__(self, iKp, iKi, iKd, iSP, iLMN_HLM, iLMN_LLM):
        self.Kp = iKp  # proportional term / 0.0 = switched off
        self.Ki = iKi  # integral term / 0.0 = switched off
        self.Kd = iKd  # derivate term / 0.0 = switched off
        self.SP = iSP  # setpoint
        self.prev_ER = 0  # error from previous scan
        self.integral = 0
        self.derivative = 0
        self.LMN_HLM = iLMN_HLM  # LMN high Limit
        self.LMN_LLM = iLMN_LLM  # LMN low limit

    def compute(self, iPV, iTimestep):
        # Calculate error
        ER = self.SP - iPV

        # Proportional term
        P_out = self.Kp * ER

        # Integral term
        self.integral += ER * iTimestep
        I_out = self.Ki * self.integral

        # Derivative term
        self.derivative = (ER - self.prev_ER) / iTimestep
        D_out = self.Kd * self.derivative

        # Compute total output
        oLMN = P_out + I_out + D_out

        # Correct LMN if not in range of high and low limits
        if oLMN > self.LMN_HLM:
            oLMN = self.LMN_HLM
        elif oLMN < self.LMN_LLM:
            oLMN = self.LMN_LLM

        # Update previous error
        self.prev_ER = ER

        return oLMN
#endregion

def defRobot(robot):
    #region --Get the time step of the current world
    varTimestep = int(robot.getBasicTimeStep())
    #endregion

    #region --Initialize pendulum angle sensor
    sensPendulum = robot.getDevice(varNamePendulum)
    sensPendulum.enable(varTimestep)
    #endregion

    #region --Initialize the motors and retrieve the max. speed
    devRiMotor = robot.getDevice(varNameRiMotor)
    devRiMotor.setPosition(varMotorRotatePosition)
    devRiMotor.setVelocity(varVelocityStopped)

    devLeMotor = robot.getDevice(varNameLeMotor)
    devLeMotor.setPosition(varMotorRotatePosition)
    devLeMotor.setVelocity(varVelocityStopped)
    varMaxSpeed = min(devRiMotor.getMaxVelocity(), devLeMotor.getMaxVelocity())
    #endregion

    # region --Initialize PID controller
    devPIDController = PID_Controller(28.0, 10.0, 0.0, 0.0, varMaxSpeed, -varMaxSpeed)
    #endregion

    #region -- Initialize plot lists
    lstAngleValues = []
    lstTimeValues = []
    lstSpeedValues = []
    #endregion

    # Main loop: perform a simulation step until the simulation is over.
    while robot.step(varTimestep) != -1:
        #region --Readout the angle sensor
        varSensAngle_RAD = sensPendulum.getValue()
        varSensAngle_RADAbs = math.fabs(varSensAngle_RAD)
        print(f"Pendulum angle: {varSensAngle_RAD}")
        print(f"Pendulum angle (abs): {varSensAngle_RADAbs}")
        #endregion

        #region --Stop the robot when the pendulum falls.
        #if math.fabs(varSensAngle_RAD) > math.pi * 0.5:
        if varSensAngle_RADAbs > math.pi * 0.5:  # 1.57
            devLeMotor.setVelocity(0.0)
            devRiMotor.setVelocity(0.0)
            break
        #endregion

        #region --PID control
        varSpeed = devPIDController.compute(varSensAngle_RAD, varTimestep)
        print(f"speed: {varSpeed}")
        #endregion

        #region --Set the robot varSpeed (left wheel, right wheel).
        #varSpeed = varMaxSpeed * 0.5
        devRiMotor.setVelocity(varSpeed)
        devLeMotor.setVelocity(varSpeed)
        #endregion

        #region --Store the angle, speed and time values into the lists

        #lstTimeValues.append(dt.datetime.now())

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