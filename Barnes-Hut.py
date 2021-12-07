from body import Body
from octTree import octTree
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import copy

thetaComp = .5
G = 6.674e-11

def findLengthAndCenter(data):
        xmin = data[0].x
        xmax = data[0].x
        ymin = data[0].y
        ymax = data[0].y
        zmin = data[0].z
        zmax = data[0].z

        for i in range(len(data)):
            if(data[i].x < xmin):
                xmin = data[i].x
            if(data[i].x > xmax):
                xmax = data[i].x
            if(data[i].y < ymin):
                ymin = data[i].y
            if(data[i].y > ymax):
                ymax = data[i].y
            if(data[i].z < zmin):
                zmin = data[i].z
            if(data[i].z > zmax):
                zmax = data[i].z

        length = max(xmax-xmin, ymax-ymin, zmax-zmin)*1.0001 #This is dumb, but it prevents bodies from getting caught on corners of the octTree
        centerX = (xmax - xmin)/2
        centerY = (ymax - ymin)/2
        centerZ = (zmax - zmin)/2
        return length, centerX, centerY, centerZ

def setTree(bodies):
    length, x, y, z = findLengthAndCenter(bodies)
    tree = octTree(length, x, y, z)
    for i in range(len(bodies)):
        tree.addBody(bodies[i])
    return tree

def calcForce(body, tree, dt):
    dist = math.sqrt((tree.xCenterMass - body.x)**2 + (tree.yCenterMass - body.y)**2 + (tree.zCenterMass - body.z)**2)
    if(tree.hasChildren == False or tree.length/dist < thetaComp):
        if(tree.mass != 0 and dist > 0):
            force = body.mass*tree.mass*G/dist**2
            theta = math.atan2((tree.yCenterMass - body.y),(tree.xCenterMass - body.x))
            phi = math.atan2(math.sqrt((tree.xCenterMass-body.x)**2 + (tree.yCenterMass-body.y)**2), tree.zCenterMass - body.z)
            Fx = force*math.sin(phi)*math.cos(theta)
            Fy = force*math.sin(phi)*math.sin(theta)
            Fz = force*math.cos(phi)
            ax = Fx/body.mass
            ay = Fy/body.mass
            az = Fy/body.mass
            body.vx = body.vx + ax*dt
            body.vy = body.vy + ay*dt
            body.vz = body.vz + az*dt
            body.x = body.x + body.vx*dt
            body.y = body.y + body.vy*dt
            body.z = body.z + body.vz*dt
    else:
        calcForce(body, tree.q1, dt)
        calcForce(body, tree.q2, dt)
        calcForce(body, tree.q3, dt)
        calcForce(body, tree.q4, dt)
        calcForce(body, tree.q5, dt)
        calcForce(body, tree.q6, dt)
        calcForce(body, tree.q7, dt)
        calcForce(body, tree.q8, dt)

def timeStep(bodies, dt):
    tree = setTree(bodies)
    for i in range(len(bodies)):
        calcForce(bodies[i], tree, dt)

def BH_N_Body(bodies, simLength, dt):
    t = [0]
    bodies_per_t = [copy.deepcopy(bodies)]
    iterations = int(simLength/dt)
    for i in range(iterations):
        print(i)
        timeStep(bodies, dt)
        t.append(i*dt)
        bodies_per_t.append(copy.deepcopy(bodies))
    return bodies_per_t, t

def update(i, ax, xmin, xmax, ymin, ymax, zmin, zmax, simData):
    ax.cla()
    ax.set_xlim3d([xmin, xmax])
    ax.set_xlabel('x')
    ax.set_ylim3d([ymin, ymax])
    ax.set_ylabel('y')
    ax.set_zlim3d([zmin, zmax])
    ax.set_zlabel('z')
    for j in range(len(simData[i])):
        ax.scatter(simData[i][j].x, simData[i][j].y, simData[i][j].z, c='black', s = 5)

def animate(xmin, xmax, ymin, ymax, zmin, zmax, data):
    Writer = animation.writers['pillow']
    writer = Writer(fps = 15)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')

    line_ani = animation.FuncAnimation(fig, update, 200, fargs=(ax, xmin, xmax, ymin, ymax, zmin, zmax, data))
    line_ani.save("sequential.gif", writer = writer)
    plt.show()

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

bodies = []
for i in range(0,101,25):
    for j in range(0,101,25):
        for k in range(0,101,25):
            b = Body(mass = 1e6, x = i, y = j, z = k, vx = 0, vy = 0, vz = 0)
            bodies.append(copy.deepcopy(b))

print("initialized 125 bodies for sim")
print("running n-body sim")
simData, t = BH_N_Body(bodies = bodies, simLength = 2000, dt = 10)
print("creating animation (this will take a while)")
xmin, xmax, ymin, ymax, zmin, zmax = findMinMax(simData)
animate(xmin, xmax, ymin, ymax, zmin, zmax, simData)
print("All done!")