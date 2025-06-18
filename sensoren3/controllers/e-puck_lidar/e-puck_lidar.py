"""e-puck_lidar controller."""

from controller import Robot
import statistics
import random

# create the Robot instance.
def run_robot(robot):
    timestep = 32
    varMaxSpeed = 6.28 
    varLeftSpeed = varMaxSpeed
    varRightSpeed = varMaxSpeed
    
    #Enable the motors, set their Position on infinity and their velocity on zero
    leftMotor = robot.getDevice('left wheel motor')
    rightMotor = robot.getDevice('right wheel motor')
    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))
    leftMotor.setVelocity(0.0)
    rightMotor.setVelocity(0.0)

    # Enable the Lidar and clear it's list with measured values
    lidar = robot.getDevice('lidar')
    lidar.enable(timestep)
    listLidarSections = []
        
    # Enable the use of the Lidar Point Cloud
    lidar.enablePointCloud()
    
    #Turn around
    varTurnAround = False
    varCounter = 0

    while robot.step(timestep) != -1:
        varLeftSpeed = varMaxSpeed
        varRightSpeed = varMaxSpeed
        listLidarSections.clear()
        
        # Dump every value of the lidar in a list
        img = lidar.getRangeImage()
        if not varTurnAround:
            # for i=0 to 16 do
            for i in range(16):
                    # Calculate 16 mean values and append each of them to a list
                    # mean(LidarSections[0:15]), mean(LidarSections[16:31]), ...)
                    listLidarSections.append(statistics.mean(img[i*32:((i+1)*32)-1]))
            
            # For each of the 8 mean lidar values at the left, turn right if they detect something if their values are lower then 0.3
            # by increasing right speed, for each ray
            for x in listLidarSections[0:8]:
                if(x < 0.3):
                    varRightSpeed -= 0.78
                    
            # For each of the last 8 mean lidar values at the right, turn left if they detect something if their values are lower then 0.3     
            # by increasing left speed, for each ray
            for x in listLidarSections[8:16]:
                if(x < 0.3):
                    varLeftSpeed -= 0.78
                                   
            if(varRightSpeed <= 0.1 and varLeftSpeed <= 0.1):
                varTurnAround = True
                varCounter = random.randint(12, 20)

        else:
            varLeftSpeed = -varMaxSpeed
            varRightSpeed = varMaxSpeed
            varCounter -= 1
            
            if(varCounter == 0):
                varTurnAround = False

        #Print current velocities to the console 
        if varLeftSpeed < -varMaxSpeed:
            varLeftSpeed = -varMaxSpeed    
            
        if varRightSpeed < -varMaxSpeed:
            varRightSpeed = -varMaxSpeed
                                   
        print(varLeftSpeed)
        print(varRightSpeed)
        
        #Set velocity of motors
        leftMotor.setVelocity(varLeftSpeed)
        rightMotor.setVelocity(varRightSpeed)
    
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)
