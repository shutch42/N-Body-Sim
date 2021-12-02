from body import Body
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import copy

def Sequential_N_Body(bodies, simLength, dt):
    t = [0]
    bodies_per_t = [copy.deepcopy(bodies)]
    G = 6.674e-11
    r = 0
    Fx = 0
    Fy = 0
    Fz = 0
    ax = 0
    ay = 0
    az = 0

    iterations = int(simLength/dt)

    for i in range(iterations):
        for j in range(len(bodies)):
            for k in range(len(bodies)):
                #make sure not to calculate the force of a body on itself
                if(j != k):
                    x1 = bodies[j].x
                    x2 = bodies[k].x
                    y1 = bodies[j].y
                    y2 = bodies[k].y
                    z1 = bodies[j].z
                    z2 = bodies[k].z
                    m1 = bodies[j].mass
                    m2 = bodies[k].mass
                    r = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
                    F = (G*m1*m2)/(r**2)
                    #Using spherical coordinates
                    theta = math.atan2((y2-y1), (x2-x1))
                    phi = math.atan2(math.sqrt((x2-x1)**2 + (y2-y1)**2), (z2-z1))

                    Fx = F*math.sin(phi)*math.cos(theta)
                    Fy = F*math.sin(phi)*math.sin(theta)
                    Fz = F*math.cos(phi)

                    ax = Fx/m1
                    ay = Fy/m1
                    az = Fz/m1

                    bodies[j].vx = bodies[j].vx + ax*dt
                    bodies[j].vy = bodies[j].vy + ay*dt
                    bodies[j].vz = bodies[j].vz + ay*dt
                    bodies[j].x = bodies[j].x + bodies[j].vx*dt
                    bodies[j].y = bodies[j].y + bodies[j].vy*dt
                    bodies[j].z = bodies[j].z + bodies[j].vz*dt
        
        #how to kill all of the RAM in your computer
        bodies_per_t.append(copy.deepcopy(bodies))
        t.append(i*dt)

    return bodies_per_t, t

def findMinMax(data):
    xmin = data[0][0].x
    xmax = data[0][0].x
    ymin = data[0][0].y
    ymax = data[0][0].y
    zmin = data[0][0].z
    zmax = data[0][0].z

    for i in range(len(data)):
        for j in range(len(data[i])):
            if(data[i][j].x < xmin):
                xmin = data[i][j].x
            if(data[i][j].x > xmax):
                xmax = data[i][j].x
            if(data[i][j].y < ymin):
                ymin = data[i][j].y
            if(data[i][j].y > ymax):
                ymax = data[i][j].y
            if(data[i][j].z < zmin):
                zmin = data[i][j].z
            if(data[i][j].z > zmax):
                zmax = data[i][j].z
#            print(data[i][j].get_info())
#    print(xmin, xmax)
#    print(ymin, ymax)
#    print(zmin, zmax)
    return xmin, xmax, ymin, ymax, zmin, zmax

def cubeSim():
    b1 = Body(mass = 1e8, x = 0, y = 0, z = 0, vx = 0, vy = 0, vz = 0)
    b2 = Body(mass = 1e8, x = 0, y = 0, z = 100, vx = 0, vy = 0, vz = 0)
    b3 = Body(mass = 1e8, x = 100, y = 0, z = 0, vx = 0, vy = 0, vz = 0)
    b4 = Body(mass = 1e8, x = 100, y = 0, z = 100, vx = 0, vy = 0, vz = 0)
    b5 = Body(mass = 1e8, x = 0, y = 100, z = 0, vx = 0, vy = 0, vz = 0)
    b6 = Body(mass = 1e8, x = 0, y = 100, z = 100, vx = 0, vy = 0, vz = 0)
    b7 = Body(mass = 1e8, x = 100, y = 100, z = 0, vx = 0, vy = 0, vz = 0)
    b8 = Body(mass = 1e8, x = 100, y = 100, z = 100, vx = 0, vy = 0, vz = 0)

    bodies = [b1, b2, b3, b4, b5, b6, b7, b8]
    print("initialized bodies for sim")
    print("running n-body sim")
    simData, t = Sequential_N_Body(bodies = bodies, simLength = 5000, dt = 25)
    print("sim complete, making animation (this may take a while)")
    xmin = -500
    ymin = -500
    zmin = -500
    xmax = 500
    ymax = 500
    zmax = 500
    animate(xmin, xmax, ymin, ymax, zmin, zmax, simData)
    print("All done!")
#    xmin, xmax, ymin, ymax, zmin, zmax = findMinMax(data = simData);
#print(animation.writers.list())

def lottaMassesSim():
    bodies = []
    for i in range(0,101,25):
        for j in range(0,101,25):
            for k in range(0,101,25):
                b = Body(mass = 1e6, x = i, y = j, z = k, vx = 0, vy = 0, vz = 0)
                bodies.append(copy.deepcopy(b))

    print("initialized 64 bodies for sim")
    print("running n-body sim")
    simData, t = Sequential_N_Body(bodies = bodies, simLength = 2000, dt = 10)
    xmin = 0
    ymin = 0
    zmin = 0
    xmax = 100
    ymax = 100
    zmax = 100
    print("creating animation (this will take a while)")
    animate(xmin, xmax, ymin, ymax, zmin, zmax, simData)
    print("All done!")


def update(i, ax, xmin, xmax, ymin, ymax, zmin, zmax, simData):
    ax.cla()
    ax.set_xlim3d([xmin, xmax])
    ax.set_xlabel('x')
    ax.set_ylim3d([ymin, ymax])
    ax.set_ylabel('y')
    ax.set_zlim3d([zmin, zmax])
    ax.set_zlabel('z')
    for j in range(len(simData[i])):
        ax.scatter(simData[i][j].x, simData[i][j].y, simData[i][j].z)

def animate(xmin, xmax, ymin, ymax, zmin, zmax, data):
    Writer = animation.writers['pillow']
    writer = Writer(fps = 15)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')

    line_ani = animation.FuncAnimation(fig, update, 200, fargs=(ax, xmin, xmax, ymin, ymax, zmin, zmax, data))
    line_ani.save("sequential.gif", writer = writer)
    plt.show()

lottaMassesSim();