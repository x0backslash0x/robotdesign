"""e-puck_lidar controller."""

from controller import Robot

def run_robot(robot): 
    # Define general vars
    timestep = 32
    varMaxSpeed = 6.28
    
    # Enable the Lidar
    lidar = robot.getDevice('lidar')
    lidar.enable(timestep)
    
    # Enable the use of the Lidar Point Cloud
    lidar.enablePointCloud()
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # Read the sensors:
        # Dump every value of the lidar in a list
        img = lidar.getRangeImage()
        #Print only the values of the 5 first rays to the console
        print("{}" .format(img[0:5]))
    
        # Only necessary when the while loop does not contain any code
        pass

# Main loop:
if __name__ == "__main__":

    #create the robot instance
    my_robot = Robot()
    run_robot(my_robot)
