from matplotlib import pyplot as plt
import numpy as np
import math

gravityAcceleration = -9.81                                                                         # g [in m/s^2]

def velocityComponents(velocity: float, angle: float) -> list:
    '''
    Return the x-component and y-component of velocity in the form of a 'python list'
    
    Parameters: 
    - Velocity Magnitude (float)
    - Angle between the velocity vector and local horizontal (float)
    '''
    x_velocity, y_velocity = [velocity*math.cos(math.radians(angle)), velocity*math.sin(math.radians(angle))]
    return [x_velocity, y_velocity]

def draglessProjectile(initialConditions: list) -> list:
    '''
    Returns the projectile flight time, maximum attained height, and total range covered
    '''
    initialHeight, initialVelocity, incidentAngle = initialConditions
    x_initialVelocity, y_initialVelocity = velocityComponents(initialVelocity, incidentAngle)       # u*cos(theta), u*sin(theta)

    flight_time = (y_initialVelocity + math.sqrt((y_initialVelocity**2) + 2 * (-gravityAcceleration) * initialHeight))/(-gravityAcceleration)
    max_height = initialHeight + (y_initialVelocity**2)/(2*-gravityAcceleration)
    total_range = x_initialVelocity*(y_initialVelocity+math.sqrt((y_initialVelocity**2) + 2 * (-gravityAcceleration) * initialHeight))/(-gravityAcceleration)

    return [flight_time, max_height, total_range]

def trajectoryPlotter(initialConditions) -> None:
    initialHeight, initialVelocity, incidentAngle = initialConditions
    flightTime, maxHeight, totalRange = draglessProjectile(initialConditions)
    x_initialVelocity, y_initialVelocity = velocityComponents(initialVelocity, incidentAngle)

    def x_position(time):    
        u = x_initialVelocity
        a = 0   
        return (u*time)+(a*(time**2)/2)
    
    def y_position(time):    
        u = y_initialVelocity
        a = gravityAcceleration
        return initialHeight + (u*time)+(a*(time**2)/2)

    time_step = 0.01                                                                                    # motion time per iteration
    time = np.linspace(0, flightTime, int(1/time_step))
    x, y = [], []
    
    for t in time: 
        plt.clf()
        
        x.append(x_position(t))
        y.append(y_position(t))
        
        plt.plot(x, y)
        
        plt.title("Flight Trajectory in zero-drag conditions")
        plt.legend([f"Time of Flight: {round(t, 2)} seconds"], loc="upper right")
        
        plt.xlabel('Range (in metres)')
        plt.ylabel('Height (in metres)')

        plt.grid()
        
        plt.ylim(bottom = 0, top = (maxHeight*1.1))
        plt.xlim(left = 0, right = (totalRange*1.1))
        
        plt.pause(time_step)
    plt.show()

def displayParameters(initialConditions: list) -> None:
    flightTime, maxHeight, totalRange = draglessProjectile(initialConditions)
    print("\nFlight Parameters")
    print(f"- Total Flight Time\t: {round(flightTime,2)} seconds")
    print(f"- Maximum Height\t: {round(maxHeight, 2)} metres")
    print(f"- Total Range\t\t: {round(totalRange, 2)} metres")

if __name__ == '__main__':        
    print("Solution Setup")
    initialHeight = float(input("- Initial Height (in metres)\t: "))                                    # y_0 [in m]
    initialVelocity = float(input("- Initial Velocity (in m/s)\t: "))                                   # u [in m/s]
    incidentAngle = float(input("- Incident Angle (in degrees)\t: "))                                   # theta [in radians]
    
    initialConditions = [initialHeight, initialVelocity, incidentAngle]
    
    displayParameters(initialConditions)
    trajectoryPlotter(initialConditions)


