"""agv_controller controller."""

from controller import Robot

TIME_STEP = 64
robot = Robot()

motor_left = robot.getDevice('motor_left')
motor_right = robot.getDevice('motor_right')
motor_left.setPosition(float('inf'))
motor_right.setPosition(float('inf'))
motor_left.setVelocity(0.0)
motor_right.setVelocity(0.0)


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIME_STEP) != -1:
    leftSpeed = 1.0
    rightSpeed = 1.0

    motor_left.setVelocity(leftSpeed)
    motor_right.setVelocity(rightSpeed)
