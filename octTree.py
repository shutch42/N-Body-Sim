import math
from body import Body

class octTree:
    def __init__(self, length, x, y, z):
        self.length = length
        self.mass = 0
        self.xCenterMass = 0
        self.yCenterMass = 0
        self.zCenterMass = 0
        self.xOrigin = x
        self.yOrigin = y
        self.zOrigin = z
        self.bodies = []
        self.hasChildren = False
        self.q1 = None # +x,+y,+z
        self.q2 = None # -x,+y,+z
        self.q3 = None # -x,-y,+z
        self.q4 = None # +x,-y,+z
        self.q5 = None # +x,+y,-z
        self.q6 = None # -x,+y,-z
        self.q7 = None # -x,-y,-z
        self.q8 = None # +x,-y,-z
    
    def addBody(self, body):
        if(self.mass == 0):
            self.bodies.append(body)
            self.mass = body.mass
            self.xCenterMass = body.x
            self.yCenterMass = body.y
            self.zCenterMass = body.z
        else:
            #add body to node, set new mass and center of mass for node
            self.bodies.append(body)
            totalMass = self.mass + body.mass
            self.xCenterMass = (self.mass*self.xCenterMass + body.mass*body.x)/totalMass
            self.yCenterMass = (self.mass*self.yCenterMass + body.mass*body.y)/totalMass
            self.zCenterMass = (self.mass*self.zCenterMass + body.mass*body.z)/totalMass
            self.mass = totalMass
            #if node has children, add body to proper quadrant
            if(self.hasChildren == True):
                x = body.x
                y = body.y
                z = body.z
                if(x > self.xOrigin and y > self.yOrigin and z > self.zOrigin):
                    self.q1.addBody(body)
                elif(x < self.xOrigin and y > self.yOrigin and z > self.zOrigin):
                    self.q2.addBody(body)
                elif(x < self.xOrigin and y < self.yOrigin and z > self.zOrigin):
                    self.q3.addBody(body)
                elif(x > self.xOrigin and y < self.yOrigin and z > self.zOrigin):
                    self.q4.addBody(body)
                elif(x > self.xOrigin and y > self.yOrigin and z < self.zOrigin):
                    self.q5.addBody(body)
                elif(x < self.xOrigin and y > self.yOrigin and z < self.zOrigin):
                    self.q6.addBody(body)
                elif(x < self.xOrigin and y < self.yOrigin and z < self.zOrigin):
                    self.q7.addBody(body)
                else:
                    self.q8.addBody(body)
            else:
                #create child nodes, add in all bodies from current node
                self.q1 = octTree(length = self.length/2, x = self.xOrigin + self.length/2, y = self.yOrigin + self.length/2, z = self.zOrigin + self.length/2)
                self.q2 = octTree(length = self.length/2, x = self.xOrigin - self.length/2, y = self.yOrigin + self.length/2, z = self.zOrigin + self.length/2)
                self.q3 = octTree(length = self.length/2, x = self.xOrigin - self.length/2, y = self.yOrigin - self.length/2, z = self.zOrigin + self.length/2)
                self.q4 = octTree(length = self.length/2, x = self.xOrigin + self.length/2, y = self.yOrigin - self.length/2, z = self.zOrigin + self.length/2)
                self.q5 = octTree(length = self.length/2, x = self.xOrigin + self.length/2, y = self.yOrigin + self.length/2, z = self.zOrigin - self.length/2)
                self.q6 = octTree(length = self.length/2, x = self.xOrigin - self.length/2, y = self.yOrigin + self.length/2, z = self.zOrigin - self.length/2)
                self.q7 = octTree(length = self.length/2, x = self.xOrigin - self.length/2, y = self.yOrigin - self.length/2, z = self.zOrigin - self.length/2)
                self.q8 = octTree(length = self.length/2, x = self.xOrigin + self.length/2, y = self.yOrigin - self.length/2, z = self.zOrigin - self.length/2)
                self.hasChildren = True
                for i in range(len(self.bodies)):
                    x = self.bodies[i].x
                    y = self.bodies[i].y
                    z = self.bodies[i].z
                    if(x > self.xOrigin and y > self.yOrigin and z > self.zOrigin):
                        self.q1.addBody(self.bodies[i])
                    elif(x < self.xOrigin and y > self.yOrigin and z > self.zOrigin):
                        self.q2.addBody(self.bodies[i])
                    elif(x < self.xOrigin and y < self.yOrigin and z > self.zOrigin):
                        self.q3.addBody(self.bodies[i])
                    elif(x > self.xOrigin and y < self.yOrigin and z > self.zOrigin):
                        self.q4.addBody(self.bodies[i])
                    elif(x > self.xOrigin and y > self.yOrigin and z < self.zOrigin):
                        self.q5.addBody(self.bodies[i])
                    elif(x < self.xOrigin and y > self.yOrigin and z < self.zOrigin):
                        self.q6.addBody(self.bodies[i])
                    elif(x < self.xOrigin and y < self.yOrigin and z < self.zOrigin):
                        self.q7.addBody(self.bodies[i])
                    elif(x > self.xOrigin and y < self.yOrigin and y < self.zOrigin):
                        self.q8.addBody(self.bodies[i])

         
    def dispTree(self):
        print("Mass: ", self.mass, "Center: ", self.xCenterMass, ",", self.yCenterMass, ",", self.zCenterMass)
        if(self.hasChildren):
            self.q1.dispTree()
            self.q2.dispTree()
            self.q3.dispTree()
            self.q4.dispTree()
            self.q5.dispTree()
            self.q6.dispTree()
            self.q7.dispTree()
            self.q8.dispTree()
