import random
import math
from tkinter import * 

#for social interaction could group by families - if ind of each color becomes closer then will stick together

############
#importing background images
############ 
'''
from PIL import ImageTk,Image  
import Image
root = Tk()  
canvas = Canvas(root, width = 300, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("ball.png"))  
canvas.create_image(20, 20, anchor=NW, image=img)  
root.mainloop() 
'''

############
#classes
############

class People(object):
    def __init__(self, data):
        self.cx = random.randint(15, data.width-15)
        self.cy = random.randint(15, data.height-15)
        self.r = 10
        self.fill =  random.choice(["yellow","red","purple"])
        self.infectedColor = "green"
        self.isInfected = False
        
        #will have scores 10, 15 in higher levels
        self.score = random.choice([5, 10])
        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)
        
        #self.faceDirection = random.choice[("Up", "Down", "Left", "Right")]
        self.infectedSneezes = []
    
    #might do score, or life bar
    def draw(self, canvas):
        canvas.create_oval(self.cx-self.r, self.cy-self.r, self.cx+self.r,
        self.cy+self.r, fill=self.fill, width=0)
        
        #arms
        upperArm = lowerArm = 4
        dist = 2
        dist2 = 5
        dist3 = 6
        
        #if self.faceDirection == "Up":
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
        if self.cx+self.r < 30 and self.cy+self.r < 60:
            self.dx = 0
            self.dy = 0
        if self.cx+self.r >= data.width:
            self.cx -= self.r
            self.dx = -self.dx
        elif self.cx-self.r <= 0:
            self.cx += self.r
            self.dx = -self.dx
        if self.cy+self.r >= data.height:
            self.dy = -self.dy
            self.cy -= self.r
        elif self.cy-self.r <= 0:
            self.dy = -self.dy
            self.cy += self.r
    
    def collidesWithPeople(self, other):
        if (not isinstance(other, People)): #other must be inst of People
            return False
        else:
            dist = ((other.cx - self.cx)**2 + (other.cy - self.cy)**2)**0.5
            return dist <= self.r + other.r
        
    def collidesWithSneeze(self, other):
        dist = ((other.sx - self.cx)**2 + (other.sy - self.cy)**2)**0.5
        return dist <= self.r + other.sr
    
    def collidesWithTrail(self, x, y, r):
        dist = ((x - self.cx)**2 + (y - self.cy)**2)**0.5
        return dist <= self.r + r
    
    def collideWithStageTop(self, x, y, r):
        return (self.cx+self.r > 200 and self.cx+self.r < 400 and self.cy+self.r
        > 40)
            
    def collideWithStageBottom(self, x, y, r):
        return (self.cx+self.r > 200 and self.cx+self.r < 400 and self.cy+self.r < 
        140 and self.cy+self.r > 40)
            
    def collideWithStageTop(self, x, y, r):
        return (self.cx+self.r > 200 and self.cx+self.r < 400 and self.cy+self.r < 
        140 and self.cy+self.r > 40)
            
    def collideWithStageTop(self, x, y, r):
        return (self.cx+self.r > 200 and self.cx+self.r < 400 and self.cy+self.r < 
        140 and self.cy+self.r > 40)           

    def changeColor(self):
        self.fill = self.infectedColor
    
    def infectedSneeze(self):
        SneezeClass = Sneeze(-5,-5,(0,0))
        randAngle = random.uniform(0, 2*math.pi)
        dx = math.cos(randAngle)*SneezeClass.velocity
        dy = -math.sin(randAngle)*SneezeClass.velocity
        
        if self.isInfected:
            self.infectedSneezes.append(Sneeze(self.cx,self.cy,(dx,dy)))
    
    
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
        

#actually draw the sneeze based on changing direction and time    
class Sneeze(object):
    def __init__(self, sx, sy, direction):
        self.prevLocation = []
        self.sx = sx
        self.sy = sy
        self.direction = direction
        self.sr = random.randint(3, 5)
        self.velocity = 10
        self.fillS = random.choice(["green2", "green3"])
        
    def drawTrail(self,canvas):
        r = self.sr
        for i in range(len(self.prevLocation)):
            x = self.prevLocation[i][0]
            y = self.prevLocation[i][1]
            if r <= 8.1:
                r += 0.25
                canvas.create_oval(x-r, y-r, x+r, y+r, fill=self.fillS, width=0)
            self.prevLocation[i] = (x,y,r)
        
    def move(self):
        self.sx += self.direction[0]/10 * self.velocity
        self.sy += self.direction[1]/10 * self.velocity


class Level1Background(object):
    def __init__(self):
        self.fill1 = "gray90"
        self.fill2 = "gray46"
        self.fill3 = "gray66"
        self.fill4 = "gray86"
    
    def drawBackground1(self, canvas):
        #stage
        canvas.create_rectangle(200, 40, 400, 140, fill=self.fill2, width=4)
        canvas.create_rectangle(220, 50, 380, 130, fill=self.fill3, width=4)
        canvas.create_rectangle(240, 60, 360, 120, fill=self.fill4, width=4)
        
        #exit
        canvas.create_rectangle(0, 0, 32, 70, fill=self.fill1, width=4)
        canvas.create_text(16, 35, text="EXIT", fill="red")
        
####################################
#customize these functions
####################################ç

def init(data):
    data.people = [People(data) for i in range(30)]
    data.sneezeDirection = None
    
    #main person init
    data.mainMove = 6
    data.mx = data.width/2
    data.my = (4*data.height)/5
    data.mr = 10
    data.mainPerson = MainPerson(data)
    
    #other pages
    data.mode = "homeScreen"
    
def mousePressed(event, data):
    if (data.mode == "homeScreen"): 
        homeScreenMousePressed(event, data)
    elif (data.mode == "playGame"): 
        playGameMousePressed(event, data)
    elif (data.mode == "help"): 
        helpMousePressed(event, data)

def keyPressed(event, data):
    #turning pages
    if (data.mode == "homeScreen"): 
        homeScreenKeyPressed(event, data)
    elif (data.mode == "playGame"): 
        playGameKeyPressed(event, data)
    elif (data.mode == "help"): 
        helpKeyPressed(event, data)

def timerFired(data):
    #turning pages
    if (data.mode == "homeScreen"): 
        homeScreenTimerFired(data)
    elif (data.mode == "playGame"):   
        playGameTimerFired(data)
    elif (data.mode == "help"):       
        helpTimerFired(data)
    
def redrawAll(canvas, data):
    #turning pages
    if (data.mode == "homeScreen"):
        homeScreenRedrawAll(canvas, data)
    elif (data.mode == "playGame"):
        playGameRedrawAll(canvas, data)
    elif (data.mode == "help"):      
        helpRedrawAll(canvas, data)

####################################
# homeScreen mode
####################################

def homeScreenMousePressed(event, data):
    if event.x > 250 and event.x < 350 and event.y < 320 and event.y > 270:
        data.mode = "playGame"
    elif event.x > 250 and event.x < 350 and event.y < 400 and event.y > 350:
        data.mode = "help"

def homeScreenKeyPressed(event, data):
    pass

def homeScreenTimerFired(data):
    pass

def homeScreenRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="green4")
    canvas.create_text(data.width/2, data.height/2-60,
                       text="ACHOOOO", font="Arial 26 bold")
    canvas.create_text(data.width/2, data.height/2+50,
                        tex="Play Game", font="Arial 22 bold" )
    canvas.create_text(data.width/2, data.height/2+100,
                        tex="Help", font="Arial 22 bold" )

####################################
# help mode
####################################

def helpMousePressed(event, data):
    pass

def helpKeyPressed(event, data):
    data.mode = "playGame"

def helpTimerFired(data):
    pass

def helpRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2-40,
                       text="This is help mode!", font="Arial 26 bold")
    canvas.create_text(data.width/2, data.height/2-10,
                       text="How to play:", font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+15,
                       text="Do nothing and score points!", font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+40,
                       text="Press any key to keep playing!", font="Arial 20")

####################################
# playGame LEVEL1 mode
####################################

def playGameMousePressed(event, data):
    data.score = 0

def playGameKeyPressed(event, data):
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

def playGameTimerFired(data):    
    for people in data.people:
        people.move(data)
        
        #collision with stage
        if collideWithStageTop(people.cx,people.cy,people.r):
        elif collideWithStageTop(people.cx,people.cy,people.r):
        elif collideWithStageTop(people.cx,people.cy,people.r):
        elif collideWithStageTop(people.cx,people.cy,people.r):
            
        #checking people-sneeze collision
        for sneeze in data.mainPerson.sneezes:
            if people.collidesWithSneeze(sneeze):
                if people.score == 5 and sneeze.velocity != 0:
                    people.score = 0
                    people.dx = 0
                    people.dy = 0
                    people.changeColor()
                    people.isInfected = True
                    people.infectedSneeze() #must call the infected func
                elif people.score > 5:
                    people.score -= 5
            #moreSneeze is a tuple of locations
            #checking people-trail collision
            for moreSneeze in sneeze.prevLocation:
                x, y, r = moreSneeze
                if people.collidesWithTrail(x,y,r):
                    if people.score == 5 and sneeze.velocity != 0:
                        people.score = 0
                        people.changeColor()
                        people.isInfected = True
                    elif people.score > 5 and people.score != 0:
                        people.score -= 5
        
    #main person sneeze   
    for sneeze in data.mainPerson.sneezes:
        if sneeze.velocity <= 0:
            continue
        #a list of tuples containing previous locations
        sneeze.prevLocation.append((sneeze.sx,sneeze.sy))
        sneeze.move()
        sneeze.velocity -= 0.6    
    
    
    #infected people sneezes
    for person in data.people:
        for sneeze in person.infectedSneezes:
            if sneeze.velocity <= 0:
                continue
            sneeze.prevLocation.append((sneeze.sx,sneeze.sy))
            sneeze.move()
            sneeze.velocity -= 0.5

    #checking people collision
    for (i,people) in enumerate(data.people):
        for rest in data.people[i+1:]: 
            if people.collidesWithPeople(rest) and people.fill != "green":
                people.cx -= people.r #move out of collision radius
                people.cy -= people.r
                people.dx = -people.dx 
                people.dy = -people.dy
                rest.dy = -rest.dy 
                rest.dx = -rest.dx

def playGameRedrawAll(canvas, data):
    #backdrop
    canvas.create_rectangle(0, 0, 600, 500, fill="salmon2")
    
    for person in data.people:
        person.draw(canvas)
        for sneeze in person.infectedSneezes:
            sneeze.drawTrail(canvas) 
    
    for sneeze in data.mainPerson.sneezes:
        sneeze.drawTrail(canvas)
    
    data.mainPerson.drawMain(canvas)
    
    Level1Background().drawBackground1(canvas)

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

run(600, 500)