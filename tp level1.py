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
        self.score = random.randint(0, 15)
        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)
        self.facingDirection = None

    #might do score, or life bar
    def draw(self, canvas):
        canvas.create_oval(self.cx-self.r, self.cy-self.r, self.cx+self.r,
        self.cy+self.r, fill=self.fill)
        canvas.create_text(self.cx, self.cy-13, text=str(self.score), font = "Arial 10")
    
    #how to prevent ball bouncing back n forth along border??
    def move(self, data):
        self.cx += self.dx
        self.cy += self.dy 
        if (self.cx+self.r >= data.width) or (self.cx-self.r <= 0):
            self.dx = -self.dx
        if (self.cy+self.r >= data.height) or (self.cy-self.r <= 0):
            self.dy = -self.dy
        #if isCollide()
    
    #def isCollide(self, data):
       # if
    
        
class MainPerson(object):
    def __init__(self, data):
        self.sneezes = []
        self.mx = data.width/2
        self.my = 3*data.height/4
        self.mr = 10
        self.facingDirection = "Up"
        
    def drawMain(self, canvas):
        canvas.create_oval(self.mx-self.mr, self.my-self.mr, self.mx+self.mr, self.my+self.mr, fill="black")
    
    #do math to figure out range sneeze should go in depending dir      
    def sneeze(self):
        print("hDHFLKASDJF")
        print(self.facingDirection)
        SneezeClass = Sneeze(-5,-5,(0,0))
          
        if self.facingDirection == "Up":
            #Generate between -pi/4 and pi/4
            upAngle = random.uniform(math.pi/4, 3*math.pi/4)
            xDir = math.cos(upAngle)*SneezeClass.velocity
            yDir = -math.sin(upAngle)*SneezeClass.velocity
            self.sneezes.append(Sneeze(self.mx,self.my,(xDir,yDir)))
            
        elif self.facingDirection == "Left":
            leftAngle = random.uniform(3*math.pi/4, 5*math.pi/4)
            xDir = math.cos(leftAngle)*SneezeClass.velocity
            yDir = -math.sin(leftAngle)*SneezeClass.velocity
            self.sneezes.append(Sneeze(self.mx,self.my,(xDir,yDir)))
            
        elif self.facingDirection == "Down":
            downAngle = random.uniform(5*math.pi/4, 7*math.pi/4)
            xDir = math.cos(downAngle)*SneezeClass.velocity
            yDir = -math.sin(downAngle)*SneezeClass.velocity
            self.sneezes.append(Sneeze(self.mx,self.my,(xDir,yDir)))
            
        elif self.facingDirection == "Right":
            rightAngle = random.uniform(-math.pi/4, math.pi/4)
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
        self.sr = random.randint(5, 8)
        self.velocity = 10
    
    #def drawSneeze(self, canvas):
        #canvas.create_oval(self.sx-self.sr, self.sy-self.sr, self.sx+self.sr,
        #self.sy+self.sr, fill="green")
        
    def drawTrail(self,canvas):
        r = self.sr
        for location in self.prevLocation:
            x = location[0]
            y = location[1]
            if r > 0.5:
                r -= 0.3
                canvas.create_oval(x-r, y-r, x+r, y+r, fill="green", width=0)
            
    def move(self):
        
        if self.velocity > 0:
            self.sx += self.direction[0]/10 * self.velocity
            self.sy += self.direction[1]/10 * self.velocity
    

####################################
# customize these functions
####################################

def init(data):
    data.people = [People(data) for i in range(20)]
    data.sneezeDirection = None
    
    #main person init
    data.mainMove = 5
    data.mx = data.width/2
    data.my = (4*data.height)/5
    data.mr = 10
    data.mainPerson = MainPerson(data)
    
def mousePressed(event, data):
    pass

#check moving within window
def keyPressed(event, data):
    print(event.keysym)
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
        data.mainPerson.sneeze()

def timerFired(data):
    for people in data.people:
        people.move(data)

    for sneeze in data.mainPerson.sneezes:
        if sneeze.velocity <= 0:
            continue
        #Have a list of tuples containing previous locations
        sneeze.prevLocation.append((sneeze.sx,sneeze.sy))
        sneeze.move()
        sneeze.velocity -= 0.5

def redrawAll(canvas, data):
    #background
    canvas.create_rectangle(0, 0, data.width, data.height, fill="grey")
    
    for people in data.people:
        people.draw(canvas)
    
    for sneeze in data.mainPerson.sneezes:
        #sneeze.drawSneeze(canvas)
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