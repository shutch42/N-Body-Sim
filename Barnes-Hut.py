from body import Body
from octTree import octTree
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import copy

thetaComp = 0.5
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

        length = math.sqrt((xmax - xmin)**2 + (ymax - ymin)**2 + (zmax - zmin)**2)
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
        timeStep(bodies, dt)
        t.append(i*dt)
        bodies_per_t.append(copy.deepcopy(bodies))
    return bodies_per_t, t

b1 = Body(mass = 1e8, x = 0, y = 0, z = 0, vx = 0, vy = 0, vz = 0)
b2 = Body(mass = 1e8, x = 0, y = 0, z = 100, vx = 0, vy = 0, vz = 0)
b3 = Body(mass = 1e8, x = 100, y = 0, z = 0, vx = 0, vy = 0, vz = 0)
b4 = Body(mass = 1e8, x = 100, y = 0, z = 100, vx = 0, vy = 0, vz = 0)
b5 = Body(mass = 1e8, x = 0, y = 100, z = 0, vx = 0, vy = 0, vz = 0)
b6 = Body(mass = 1e8, x = 0, y = 100, z = 100, vx = 0, vy = 0, vz = 0)
b7 = Body(mass = 1e8, x = 100, y = 100, z = 0, vx = 0, vy = 0, vz = 0)
b8 = Body(mass = 1e8, x = 100, y = 100, z = 100, vx = 0, vy = 0, vz = 0)
bodies = [b1, b2, b3, b4, b5, b6, b7, b8]

simData, t = BH_N_Body(bodies, 5000, dt = 25)

