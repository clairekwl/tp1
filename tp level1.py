import random
import math
from tkinter import *

#need to add faces + direction
class People(object):
    def __init__(self, data):
        self.cx = random.randint(15, data.width-15)
        self.cy = random.randint(15, data.height-15)
        self.r = 10
        self.fill =  random.choice(["yellow","red","purple"])
        self.infectedColor = "green"
        
        #will have scores 10, 15 in higher levels
        self.score = random.choice([5, 10])
        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)
        self.facingDirection = None
    
    #might do score, or life bar
    def draw(self, canvas):
        canvas.create_oval(self.cx-self.r, self.cy-self.r, self.cx+self.r,
        self.cy+self.r, fill=self.fill, width=0)
        
        #arms
        upperArm = lowerArm = 4
        dist = 2
        dist2 = 5
        dist3 = 6
        canvas.create_polygon(self.cx+self.r-dist, self.cy-upperArm, self.cx+
        self.r-dist, self.cy+lowerArm, self.cx+self.r+dist2, self.cy+dist3,
         fill=self.fill) 
        canvas.create_polygon(self.cx-self.r+dist, self.cy+upperArm, self.cx-
        self.r+dist, self.cy-lowerArm, self.cx-self.r-dist2, self.cy+dist3,
         fill=self.fill) 
         
        '''' 
        #arm status1
        canvas.create_polygon(self.mx+self.mr-dist, self.my-upperArm, self.mx+
        self.mr-dist, self.my+lowerArm, self.mx+self.mr+dist2, self.my+dist3,
         fill="black") 
        canvas.create_polygon(self.mx-self.mr+dist, self.my+upperArm, self.mx-
        self.mr+dist, self.my-lowerArm, self.mx-self.mr-dist2, self.my-dist3,
         fill="black") 
        
        #arm status2
        canvas.create_polygon(self.mx+self.mr-dist, self.my-upperArm, self.mx+
        self.mr-dist, self.my+lowerArm, self.mx+self.mr+dist2, self.my-dist3,
         fill="black") 
        canvas.create_polygon(self.mx-self.mr+dist, self.my+upperArm, self.mx-
        self.mr+dist, self.my-lowerArm, self.mx-self.mr-dist2, self.my-dist3,
         fill="black") 
         '''
         
        canvas.create_text(self.cx, self.cy-13, text=str(self.score), font = 
        "Arial 10")
    
    def move(self, data):
        self.cx += self.dx
        self.cy += self.dy 
        if (self.cx+self.r >= data.width) or (self.cx-self.r <= 0):
            self.dx = -self.dx
        if (self.cy+self.r >= data.height) or (self.cy-self.r <= 0):
            self.dy = -self.dy
    
    def collidesWithPeople(self, other):
        if (not isinstance(other, People)): #other must be inst of People
            return False
        else:
            dist = ((other.cx - self.cx)**2 + (other.cy - self.cy)**2)**0.5
            return dist <= self.r + other.r
        
    def collidesWithSneeze(self, other):
        dist = ((other.sx - self.cx)**2 + (other.sy - self.cy)**2)**0.5
        return dist <= self.r + other.sr
    
    def changeColor(self):
        self.fill = self.infectedColor
    
    def sneezee(self);
        if 
            
    
class MainPerson(object):
    def __init__(self, data):
        self.sneezes = []
        self.mx = data.width/2
        self.my = 3*data.height/4
        self.mr = 10
        self.faceInt = 2
        self.facingDirection = "Up"
        
    def drawMain(self, canvas):
        canvas.create_oval(self.mx-self.mr, self.my-self.mr, self.mx+self.mr,
         self.my+self.mr, fill="black")
        
        #arm status0
        upperArm = lowerArm = 4
        dist = 2
        dist2 = 5
        dist3 = 6
        
        '''' 
        #arm status1
        canvas.create_polygon(self.mx+self.mr-dist, self.my-upperArm, self.mx+
        self.mr-dist, self.my+lowerArm, self.mx+self.mr+dist2, self.my+dist3,
         fill="black") 
        canvas.create_polygon(self.mx-self.mr+dist, self.my+upperArm, self.mx-
        self.mr+dist, self.my-lowerArm, self.mx-self.mr-dist2, self.my-dist3,
         fill="black") 
        
        #arm status2
        canvas.create_polygon(self.mx+self.mr-dist, self.my-upperArm, self.mx+
        self.mr-dist, self.my+lowerArm, self.mx+self.mr+dist2, self.my-dist3,
         fill="black") 
        canvas.create_polygon(self.mx-self.mr+dist, self.my+upperArm, self.mx-
        self.mr+dist, self.my-lowerArm, self.mx-self.mr-dist2, self.my-dist3,
         fill="black") 
         '''
        
        if self.facingDirection == "Up":
            canvas.create_oval(self.mx-self.mr/2, self.my-self.mr-self.faceInt,
             self.mx+self.mr/2, self.my-self.mr/2+self.faceInt, fill="white",
              width=0)
            canvas.create_polygon(self.mx+self.mr-dist, self.my-upperArm,
             self.mx+self.mr-dist, self.my+lowerArm, self.mx+self.mr+dist2,
              self.my+dist3, fill="black") 
            canvas.create_polygon(self.mx-self.mr+dist, self.my+upperArm, 
            self.mx-self.mr+dist, self.my-lowerArm, self.mx-self.mr-dist2,
             self.my+dist3, fill="black") 
            
        elif self.facingDirection == "Right":
            canvas.create_oval(self.mx+self.mr/2-self.faceInt, self.my-self.mr/2
            , self.mx+self.mr+self.faceInt, self.my+self.mr/2, fill="white",
             width=0)
            canvas.create_polygon(self.mx-self.mr+dist, self.my+upperArm, 
            self.mx-self.mr+dist, self.my-lowerArm, self.mx-self.mr-dist2,
             self.my+dist3, fill="black")
            
        elif self.facingDirection == "Down":
            canvas.create_oval(self.mx+self.mr/2, self.my+self.mr+self.faceInt,
             self.mx-self.mr/2, self.my+self.mr/2-self.faceInt, fill="white",
              width=0)
            canvas.create_polygon(self.mx+self.mr-dist, self.my-upperArm,
             self.mx+self.mr-dist, self.my+lowerArm, self.mx+self.mr+dist2,
              self.my-dist3, fill="black") 
            canvas.create_polygon(self.mx-self.mr+dist, self.my+upperArm, 
            self.mx-self.mr+dist, self.my-lowerArm, self.mx-self.mr-dist2,
             self.my-dist3, fill="black")
            
        elif self.facingDirection == "Left":
            canvas.create_oval(self.mx-self.mr/2+self.faceInt, self.my+self.mr/2
            , self.mx-self.mr-self.faceInt, self.my-self.mr/2, fill="white",
             width=0)
            canvas.create_polygon(self.mx+self.mr-dist, self.my-upperArm,
             self.mx+self.mr-dist, self.my+lowerArm, self.mx+self.mr+dist2,
              self.my+dist3, fill="black") 

            
    #do math to figure out range sneeze should go in depending dir      
    def sneeze(self):
        SneezeClass = Sneeze(-5,-5,(0,0))
          
        if self.facingDirection == "Up":
            #Generate between -pi/4 and pi/4
            upAngle = random.uniform(math.pi/3, 2*math.pi/3)
            xDir = math.cos(upAngle)*SneezeClass.velocity
            yDir = -math.sin(upAngle)*SneezeClass.velocity
            self.sneezes.append(Sneeze(self.mx,self.my,(xDir,yDir)))
            
        elif self.facingDirection == "Left":
            leftAngle = random.uniform(5*math.pi/6, 7*math.pi/6)
            xDir = math.cos(leftAngle)*SneezeClass.velocity
            yDir = -math.sin(leftAngle)*SneezeClass.velocity
            self.sneezes.append(Sneeze(self.mx,self.my,(xDir,yDir)))
            
        elif self.facingDirection == "Down":
            downAngle = random.uniform(4*math.pi/3, 5*math.pi/3)
            xDir = math.cos(downAngle)*SneezeClass.velocity
            yDir = -math.sin(downAngle)*SneezeClass.velocity
            self.sneezes.append(Sneeze(self.mx,self.my,(xDir,yDir)))
            
        elif self.facingDirection == "Right":
            rightAngle = random.uniform(-math.pi/6, math.pi/6)
            xDir = math.cos(rightAngle)*SneezeClass.velocity
            yDir = -math.sin(rightAngle)*SneezeClass.velocity
            self.sneezes.append(Sneeze(self.mx,self.my,(xDir,yDir)))
    
    def moveSneeze(self):
        for sneeze in self.sneezes:
            sneeze.move()
        
#actually draw the sneeze based on changing direction and time    
class Sneeze(object):
    def __init__(self, sx, sy, direction):
        self.prevLocation = []
        self.sx = sx
        self.sy = sy
        self.direction = direction
        self.sr = random.randint(3, 5)
        self.velocity = 10
        
    def drawTrail(self,canvas):
        r = self.sr
        for location in self.prevLocation:
            x = location[0]
            y = location[1]
            if r <= 7:
                r += 0.25
                canvas.create_oval(x-r, y-r, x+r, y+r, fill="green", width=0)
            
    def move(self):
        if self.velocity > 0:
            self.sx += self.direction[0]/10 * self.velocity
            self.sy += self.direction[1]/10 * self.velocity

####################################
#customize these functions
####################################

def init(data):
    data.people = [People(data) for i in range(30)]
    data.sneezeDirection = None
    
    #sneezes of random pp
    #data.allSneezes = 
    
    #main person init
    data.mainMove = 6
    data.mx = data.width/2
    data.my = (4*data.height)/5
    data.mr = 10
    data.mainPerson = MainPerson(data)
    
def mousePressed(event, data):
    pass

#check moving within window
def keyPressed(event, data):
    if event.keysym == "Up":
        data.mainPerson.my -= data.mainMove 
        data.mainPerson.facingDirection = "Up"
        
    elif event.keysym == "Down":
        data.mainPerson.my += data.mainMove
        data.mainPerson.facingDirection = "Down"
        
    elif event.keysym == "Left":
        data.mainPerson.mx -= data.mainMove
        data.mainPerson.facingDirection = "Left"
        
    elif event.keysym == "Right":
        data.mainPerson.mx += data.mainMove
        data.mainPerson.facingDirection = "Right"
        
    elif event.keysym == "space":
        #produce seven rays of sneeze
        data.mainPerson.sneeze()
        data.mainPerson.sneeze()
        data.mainPerson.sneeze()
        data.mainPerson.sneeze()
        data.mainPerson.sneeze()
        data.mainPerson.sneeze()
        data.mainPerson.sneeze()

def timerFired(data):
    for people in data.people:
        people.move(data)
        #checking people-sneeze collision
        for sneeze in data.mainPerson.sneezes:
            if people.collidesWithSneeze(sneeze):
                if people.score == 0:
                    people.dx = 0
                    people.dy = 0
                    people.changeColor()
                else:
                    people.score -= 5
                #release sneeze
        #for sneeze 
        
    for sneeze in data.mainPerson.sneezes:
        if sneeze.velocity <= 0:
            continue
        #a list of tuples containing previous locations
        sneeze.prevLocation.append((sneeze.sx,sneeze.sy))
        sneeze.move()
        sneeze.velocity -= 0.5

    #checking people collision
    for (i,people) in enumerate(data.people):
        for rest in data.people[i+1:]: 
            if people.collidesWithPeople(rest):
                people.dx = -people.dx 
                people.dy = -people.dy
                rest.dy = -rest.dy 
                rest.dx = -rest.dx

def redrawAll(canvas, data):
    #background
    canvas.create_rectangle(0, 0, data.width, data.height, fill="grey")
    
    for people in data.people:
        people.draw(canvas)
        if people.fill == "green":
            people.drawTrail(canvas)
    
    for sneeze in data.mainPerson.sneezes:
        sneeze.drawTrail(canvas)
    
    data.mainPerson.drawMain(canvas)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(700, 500)