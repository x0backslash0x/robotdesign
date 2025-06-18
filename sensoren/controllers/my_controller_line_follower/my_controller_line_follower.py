"""my_controller_line_follower controller."""

from controller import Robot
# varMax_speed = 6.28
varMax_speed = 6.28 * 0.5

def run_robot(robot): 

# get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())

    # Enable motors
    oLeftMotor = robot.getDevice('left wheel motor')
    oRightMotor = robot.getDevice('right wheel motor')
    
    oLeftMotor.setPosition(float('inf'))
    oLeftMotor.setVelocity(0.0)
    
    oRightMotor.setPosition(float('inf'))
    oRightMotor.setVelocity(0.0)
    
    # Enable IR sensors
    iLeftIR = robot.getDevice('IR_Left')
    iLeftIR.enable(timestep)
    iRightIR = robot.getDevice('IR_Right')
    iRightIR.enable(timestep)

    IRsensBlack = 1000

    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        mLeftSpeed = varMax_speed
        mRightSpeed = varMax_speed 
        
        # Read the IR sensors:
        mLeftIR_Value = iLeftIR.getValue()
        mRightIR_Value = iRightIR.getValue()
        print("left: {} right: {}".format(mLeftIR_Value, mRightIR_Value))

        detectRight = mRightIR_Value == IRsensBlack
        detectLeft = mLeftIR_Value == IRsensBlack

        if detectRight:
            print("Turn right")
            mRightSpeed =- varMax_speed
            mLeftSpeed = varMax_speed

        else:
            if detectLeft:
                print("Turn left")
                mRightSpeed = varMax_speed
                mLeftSpeed = -varMax_speed

            elif not detectRight and not detectLeft:
                print("Drive forward")
                mRightSpeed = varMax_speed
                mLeftSpeed = varMax_speed

        # Enter here functions to send actuator commands, like:
        oLeftMotor.setVelocity(mLeftSpeed)
        oRightMotor.setVelocity(mRightSpeed)
               
if __name__ == "__main__":

    #create the robot instance
    my_robot = Robot()
    run_robot(my_robot)
