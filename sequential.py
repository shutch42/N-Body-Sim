from body import Body
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import copy

def Sequential_N_Body(bodies, simLength, dt):
    t = [0]
    bodies_per_t = [bodies]
    G = 6.674e-11
    r = 0
    Fx = 0
    Fy = 0
    Fz = 0
    ax = 0
    ay = 0
    az = 0

    iterations = int(simLength/dt)
    print(iterations)

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
                    theta = math.atan((y2-y1)/(x2-x1))
                    phi = math.atan(math.sqrt((x2-x1)**2 +(y2-y1)**2)/(z2-z1))

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

b1 = Body(mass = 1, x = 0, y = 0, z = 0, vx = 0, vy = 0, vz = 0)
b2 = Body(mass = 2, x = 5, y = 2, z = 4, vx = 0, vy = 0, vz = 0)

bodies = [b1, b2]

simData, t = Sequential_N_Body(bodies = bodies, simLength = 1000, dt = 1)

x1 = []
y1 = []
z1 = []
x2 = []
y2 = []
z2 = []

for i in range(len(simData)):
    x1.append(simData[i][0].x)
    y1.append(simData[i][0].y)
    z1.append(simData[i][0].z)
    x2.append(simData[i][1].x)
    y2.append(simData[i][1].y)
    z2.append(simData[i][1].z)
    for j in range(len(simData[0])):
        print(simData[i][j].get_info())

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(xs = x1, ys = y1, zs = z1)
ax.scatter(xs = x2, ys = y2, zs = z2)
plt.show()