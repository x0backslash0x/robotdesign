"""my_controller_wall_follower controller."""
from controller import Robot

def run_robot(robot):  
    # Get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28
    
    # Enable motors
    leftMotor = robot.getDevice('left wheel motor')
    rightMotor = robot.getDevice('right wheel motor')
    
    leftMotor.setPosition(float('inf'))
    leftMotor.setVelocity(0.0)
    
    rightMotor.setPosition(float('inf'))
    rightMotor.setVelocity(0.0)

    # Enable proximity sensors
    prox_sensors = []
    for ind in range(8):
        sensor_name = 'ps' + str(ind)
        prox_sensors.append(robot.getDistanceSensor(sensor_name))
        prox_sensors[ind].enable(timestep)
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # Read the sensors:
        for ind in range(8):
            print("ind: {}, val: {}".format(ind, prox_sensors[ind].getValue()))
        # Enter here functions to read sensor data, like:
        #  val = ds.getValue()
    
        # Process sensor data here.
        leftWall = prox_sensors[5].getValue() > 80
        leftCorner = prox_sensors[6].getValue() > 80
        frontWall = prox_sensors[7].getValue() > 80
    
        left_speed = max_speed
        right_speed = max_speed
        
        if frontWall:
            print("Turn right")
            left_speed = max_speed
            right_speed = -max_speed
            
        else:
            if leftWall:
                print ("Drive forward")
                left_speed = max_speed
                right_speed = max_speed  
                   
            else:
                print("Turn left")
                left_speed = max_speed/8
                right_speed = max_speed          
                             
        # Enter here functions to send actuator commands, like:
        leftMotor.setVelocity(left_speed)
        rightMotor.setVelocity(right_speed)
       
if __name__ == "__main__":

    #create the robot instance
    my_robot = Robot()
    run_robot(my_robot)
