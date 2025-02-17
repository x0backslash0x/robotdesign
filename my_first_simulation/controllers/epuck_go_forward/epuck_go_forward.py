"""epuck_go_forward controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# set parameters
TIME_STEP = 64
MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()

# Add robot motors
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

# Set target position of the motors
#leftMotor.setPosition(20.0)
#rightMotor.setPosition(20.0)
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
#rightMotor.setPosition(float('-inf')) deze zou moeten resulteren in oneindig achteruit rijden maar het wordt niet aangenomen.

leftMotor.setVelocity(0.1 * MAX_SPEED)
rightMotor.setVelocity(0.1 * MAX_SPEED)

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIME_STEP) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
