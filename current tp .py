import random
import math
from tkinter import * 

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)

def isInsideStage(x, y, r):
    return (x+r<=401 and x-r>=199 and y+r<=241 and y-r>=139) 

def isInsideRealm(x, y, r):
    return (x+r<=420 and x-r>=190 and y+r<=260 and y-r>=120) 
        
############
#classes
############

class People(object):
    def __init__(self, data):
        self.cx = random.randint(15, data.width-15)
        self.cy = random.randint(15, data.height-15)
        self.r = 10
        self.fill = random.choice(["yellow","red","purple"])
        self.isInfected = False
        
        self.timer = random.randint(5, 15)
        #will have scores 10, 15 in higher levels
        self.score = 15
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        
        self.sneezed = False
        self.infectedSneezes = []
        self.armStatus = 0
    
    #arm status1
    def draw(self, canvas):
        if isInsideStage(self.cx, self.cy, self.r):
            #people entering
            self.cx = 10
            self.cy = 480
        canvas.create_oval(self.cx-self.r, self.cy-self.r, self.cx+self.r,
        self.cy+self.r, fill=self.fill, width=0)
        
        upperArm = lowerArm = 5
        dist = 2
        dist2 = 3
        dist3 = 7
        if self.armStatus == 0:
            canvas.create_polygon(self.cx+self.r-dist, self.cy-upperArm, self.cx+
            self.r-dist, self.cy+lowerArm, self.cx+self.r+dist2, self.cy-dist3,
            fill=self.fill) 
            canvas.create_polygon(self.cx-self.r+dist, self.cy+upperArm, self.cx-
            self.r+dist, self.cy-lowerArm, self.cx-self.r-dist2, self.cy+dist3,
            fill=self.fill) 
        
        elif self.armStatus == 1:
            canvas.create_polygon(self.cx+self.r-dist, self.cy-upperArm, self.cx+
            self.r-dist, self.cy+lowerArm, self.cx+self.r+dist2, self.cy+dist3,
            fill=self.fill) 
            canvas.create_polygon(self.cx-self.r+dist, self.cy+upperArm, self.cx-
            self.r+dist, self.cy-lowerArm, self.cx-self.r-dist2, self.cy-dist3,
            fill=self.fill)  
    
    def drawScore(self, canvas):
        canvas.create_text(self.cx, self.cy-13, text=str(self.score), 
        font = "Arial 10")
        if self.fill == "red":
            self.score = 10
        elif self.fill == "yellow":
            self.score = 5
    
    def move(self, data):
        #varying speeds for different ages
        if self.fill == "purple":
            if self.dx == -1:
                self.dx -= 3.5
            elif self.dx == 1:
                self.dx += 3.5
            if self.dy == -1:
                self.dy -= 3.5
            elif self.dy == 1:
                self.dy += 3.5
        elif self.fill == "red":
            if self.dx == -1:
                self.dx -= -1.7
            elif self.dx == 1:
                self.dx += 1.7
            if self.dy == -1:
                self.dy -= 1.7
            elif self.dy == 1:
                self.dy += 1.7
                
        self.cx += self.dx
        self.cy += self.dy 
        if self.cx+self.r < 30 and self.cy+self.r < 60:
            self.dx = self.dy = 0
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
            return (distance(other.cx, other.cy, self.cx, self.cy) <= self.r +
            other.r)
        
    def collidesWithSneeze(self, other):
        return (distance(other.sx, other.sy, self.cx, self.cy) <= self.r + 
        other.sr)
    
    def collidesWithTrail(self, x, y, r):
        return distance(x, y, self.cx, self.cy) <= self.r + r
 
    def changeColor(self, data):
        if self.fill == "green": return
        self.fill = "green"
        data.infectedPeople += 1
    
    def infectedSneeze(self):
        SneezeClass = Sneeze(-5,-5,(0,0))
        randAngle = random.uniform(0, 2*math.pi)
        dx = math.cos(randAngle)*SneezeClass.velocity
        dy = -math.sin(randAngle)*SneezeClass.velocity
        
        if self.isInfected and not self.sneezed and self.timer<=0:
            self.infectedSneezes.append(Sneeze(self.cx,self.cy,(dx,dy)))
            self.sneezed = True                    
 
           
    
    
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
        dist3 = 7
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
            
    #do math to figure out range sneeze should go in depending direction     
    def sneeze(self):
        SneezeClass = Sneeze(-5,-5,(0,0))
          
        if self.facingDirection == "Up":
            upAngle = random.uniform(math.pi/3, 2*math.pi/3)
            xDir = math.cos(upAngle)*SneezeClass.velocity
            yDir = -math.sin(upAngle)*SneezeClass.velocity
            
        elif self.facingDirection == "Left":
            leftAngle = random.uniform(5*math.pi/6, 7*math.pi/6)
            xDir = math.cos(leftAngle)*SneezeClass.velocity
            yDir = -math.sin(leftAngle)*SneezeClass.velocity
            
        elif self.facingDirection == "Down":
            downAngle = random.uniform(4*math.pi/3, 5*math.pi/3)
            xDir = math.cos(downAngle)*SneezeClass.velocity
            yDir = -math.sin(downAngle)*SneezeClass.velocity
            
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
                r += 0.22
                canvas.create_oval(x-r, y-r, x+r, y+r, fill=self.fillS, width=0)
            self.prevLocation[i] = (x,y,r)
        
    def move(self):
        self.sx += self.direction[0]/12 * self.velocity
        self.sy += self.direction[1]/12 * self.velocity

class Level1Background(object):
    def __init__(self):
        self.fill1 = "gray90"
        self.fill2 = "gray46"
        self.fill3 = "gray66"
        self.fill4 = "gray86"
    
    def drawBackground1(self, canvas):
        #stage
        canvas.create_rectangle(200,140,400,240, fill=self.fill2, width=0)
        canvas.create_rectangle(220,150,380,230, fill=self.fill3, width=0)
        canvas.create_rectangle(240,160,360,220, fill=self.fill4, width=0)
        canvas.create_line(280,180,280,205, width=5)
        canvas.create_line(277,180,311,170, width=8)
        canvas.create_line(308,170,308,200, width=5)
        canvas.create_oval(275,200,285,210,fill="black")
        canvas.create_oval(303,195,313,205,fill="black")
        
        #exit
        canvas.create_rectangle(0,0,33,70, fill=self.fill1, width=4, 
        outline="gray34")
        canvas.create_text(16,35, text="EXIT", fill="red", font="Arial 15 bold")
        
        #entrance
        canvas.create_rectangle(0,420,40,500, fill=self.fill1, width=4,
        outline="gray34") 
        canvas.create_text(20,445, text="EN", fill="red", font="Arial 14 bold")
        canvas.create_text(20,460, text="TER", fill="red", font="Arial 14 bold")
               
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
    
    data.mode = "homeScreen"
    data.spacePressed = 0
    data.countDownLevel1 = 25
    data.timerr = 0
    data.isGameOver = False
    
    data.infectedPeople = 0
    data.finalInfectedPeople = 0
    data.totalScore = 0
    
def mousePressed(event, data):
    if (data.mode == "homeScreen"): 
        homeScreenMousePressed(event, data)
    elif (data.mode == "playGame"): 
        playGameMousePressed(event, data)
    elif (data.mode == "help"): 
        helpMousePressed(event, data)
    elif (data.mode == "goal1"): 
        goal1MousePressed(event, data)  
    elif (data.mode == "reportResult"): 
        reportResultMousePressed(event, data) 
    elif (data.mode == "scoreBoard"): 
        scoreBoardMousePressed(event, data)

def keyPressed(event, data):
    #turning pages
    if (data.mode == "homeScreen"): 
        homeScreenKeyPressed(event, data)
    elif (data.mode == "playGame"): 
        playGameKeyPressed(event, data)
    elif (data.mode == "help"): 
        helpKeyPressed(event, data)
    elif (data.mode == "goal1"): 
        goal1KeyPressed(event, data)
    elif (data.mode == "reportResult"): 
        reportResultKeyPressed(event, data)
    elif (data.mode == "scoreBoard"): 
        scoreBoardKeyPressed(event, data)

def timerFired(data):
    #turning pages
    if (data.mode == "homeScreen"): 
        homeScreenTimerFired(data)
    elif (data.mode == "playGame"):   
        playGameTimerFired(data)
    elif (data.mode == "help"):       
        helpTimerFired(data)
    elif (data.mode == "goal1"): 
        goal1TimerFired(data)
    elif (data.mode == "reportResult"): 
        reportResultTimerFired(data)
    elif (data.mode == "scoreBoard"): 
        scoreBoardTimerFired(data)
    
def redrawAll(canvas, data):
    #turning pages
    if (data.mode == "homeScreen"):
        homeScreenRedrawAll(canvas, data)
    elif (data.mode == "playGame"):
        playGameRedrawAll(canvas, data)
    elif (data.mode == "help"):      
        helpRedrawAll(canvas, data)
    elif (data.mode == "goal1"): 
        goal1RedrawAll(canvas, data)
    elif (data.mode == "reportResult"): 
        reportResultRedrawAll(canvas, data)
    elif (data.mode == "scoreBoard"): 
        scoreBoardRedrawAll(canvas, data)

####################################
# reportResult mode
####################################
def reportResultMousePressed(event, data):
    if event.x > 200 and event.x < 400 and event.y < 310 and event.y > 250:
        data.mode = "playGame"
    elif event.x > 200 and event.x < 400 and event.y < 380 and event.y > 320:
        data.mode = "homeScreen"
    #elif event.x > 200 and event.x < 400 and event.y < 450 and event.y > 390
        #data.mode = "scoreBoard"

def reportResultKeyPressed(event, data):
    pass

def reportResultTimerFired(data):
    pass

def reportResultRedrawAll(canvas, data): 
    fill1 = "yellow"
    fill2 = "light goldenrod" 
    fill3 = "springGreen4"
    
    canvas.create_rectangle(0,0,600,500, fill=fill1, width=0)
    if (data.finalInfectedPeople/30)*100 > 70:
        canvas.create_text(300,145, text="You've infected " +
        str(round((data.finalInfectedPeople/30)*100)) + " % of the people! :)", 
        font="Arial 26", fill=fill3)
    else:
        canvas.create_text(300,145, text="You've only infected " +
        str(round((data.finalInfectedPeople/30)*100)) +"% of the people :(",
        font="Arial 26", fill=fill3)
    
    canvas.create_text(300, 185, text="Your score is " + str(data.totalScore),
    font="Arial 26", fill=fill3)
    canvas.create_rectangle(200,250,400,310, fill=fill3, width=0)
    canvas.create_text(300,280, text="Try Again", font="Arial 20")
    canvas.create_rectangle(200,320,400,380, fill=fill3, width=0)
    canvas.create_text(300,350, text="Quit", font="Arial 20")
    canvas.create_rectangle(200,390,400,450, fill=fill3, width=0)
    canvas.create_text(300,420, text="High Score Board", font="Arial 20")
 
####################################
# goal1 mode
####################################

def goal1MousePressed(event, data):
    if event.x > 200 and event.x < 400 and event.y < 400 and event.y > 350:
        data.mode = "playGame"

def goal1KeyPressed(event, data):
    pass

def goal1TimerFired(data):
    pass

def goal1RedrawAll(canvas, data):
    fill1 = "springGreen4"
    canvas.create_rectangle(0,0,600,500,outline="black", fill="PeachPuff2", 
    width=2)
    canvas.create_rectangle(100,150,500,300,fill="gray90", outline=fill1)
    canvas.create_text(300,200,text="Your goal is to infect 70% of the",font=
    "Arial 26", fill=fill1)
    canvas.create_text(300,250,text=" of the people at the concert",
    font="Arial 26", fill=fill1)
    canvas.create_rectangle(200,350,400,400,fill="gray90",outline=fill1)
    canvas.create_text(300,375,text="Continue",font="Arial 26", fill=fill1)

####################################
# homeScreen mode
####################################

def homeScreenMousePressed(event, data):
    if event.x > 250 and event.x < 350 and event.y < 250 and event.y > 210:
        data.mode = "goal1"
    elif event.x > 250 and event.x < 350 and event.y < 300 and event.y > 260:
        data.mode = "help"

def homeScreenKeyPressed(event, data):
    pass

def homeScreenTimerFired(data):
    pass

def homeScreenRedrawAll(canvas, data):
    fill4 = "green yellow"
    fill5 = "green"
    
    canvas.create_rectangle(0, 0, data.width, data.height, fill="cornsilk4")
    canvas.create_rectangle(85,77,515,425, width=0, fill="cornsilk3")
    canvas.create_rectangle(150,125,450,375, width=0, fill="cornsilk2")
    canvas.create_rectangle(220,180,380,330, width=0, fill="ivory2")
    canvas.create_text(300, 45,text="Just Sneeeze", font="Arial 43",
    fill=fill4)
    canvas.create_text(300, 100,text="Just Sneeeze", font="Arial 30 ",
    fill=fill4)
    canvas.create_text(300, 150,text="Just Sneeeze", font="Arial 20 ",
    fill=fill4)
    canvas.create_text(300, 230, text="Play Game", font="Arial 22 ",
    fill=fill5)
    canvas.create_text(300, 280, text="Instructions", font="Arial 22 ",
    fill=fill5)

####################################
# help mode
####################################

def helpMousePressed(event, data):
    if event.x > 430 and event.x < 530 and event.y < 450 and event.y > 414:
        data.mode = "playGame"

def helpKeyPressed(event, data):
    pass

def helpTimerFired(data):
    pass

def helpRedrawAll(canvas, data):
    #REMEMBER TO SAY THAT PEOPLE WILL BE EXITING SO U CANT TAKE FOREVER TO MOVE MAIN PERSON
    canvas.create_rectangle(0,0,data.width,data.height, fill="cornsilk4")
    canvas.create_text(90,25, text="Just Sneeeze", fill="green yellow", 
    font="Arial 26")
    canvas.create_rectangle(48,50,550,460, fill="cornsilk2")
    canvas.create_line(300,50,300,460, width=0.5)
    #left side
    canvas.create_text(74,64, text="Goal:", font="Arial 16 bold")
    canvas.create_text(170,83, text="You are an evil person carrying a")
    canvas.create_text(178,97, text="deadly virus, and you plan to infect")
    canvas.create_text(179,111, text="as many people as possible at a      ")
    canvas.create_text(92,125, text="concert.")
    
    canvas.create_text(89,150, text="Controls:", font="Arial 16 bold")
    canvas.create_text(170,168, text="You may only sneeze ONCE!")
    canvas.create_text(170,182, text="Control the movement of your")
    canvas.create_text(172,196, text="person with ARROW KEYS.")
    canvas.create_text(170,218, text="Press SPACE to sneeze.")
    canvas.create_rectangle(84,228,272,258, fill="cornsilk3", width=0)
    canvas.create_text(170,243, text="Space", fill="dim gray")
    
    canvas.create_text(89,280, text="Strategy:", font="Arial 16 bold")
    canvas.create_text(178,298, text="Choose when you sneeze carefully.")
    canvas.create_text(172,312, text="You want to maxmize the affected")
    canvas.create_text(100,326, text="population.")
    canvas.create_text(174,355, text="Factors that you want to consider:")
    canvas.create_text(170,375, text="1. Ages of nearby targets")
    canvas.create_text(170,390, text="2. Interactions between people")
    canvas.create_text(170,414, text="*Some people might exit, so you")
    canvas.create_text(170,429, text="are losing people with time!")
    
    #right side
    canvas.create_text(369,64, text="Types of People:", font="Arial 16 bold")
    
    cx = 320
    r = 10
    cy = 90
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="purple", width=0)
    upperArm = lowerArm = 5
    dist = 2
    dist2 = 3
    dist3 = 7
    canvas.create_polygon(cx+r-dist, cy-upperArm, cx+r-dist, cy+lowerArm, 
    cx+r+dist2, cy+dist3,fill="purple") 
    canvas.create_polygon(cx-r+dist, cy+upperArm, cx-r+dist, cy-lowerArm, cx-r-
    dist2, cy+dist3,fill="purple")
    
    cx1 = 320
    cy1 = 150
    canvas.create_oval(cx1-r, cy1-r, cx1+r, cy1+r, fill="red", width=0)
    canvas.create_polygon(cx1+r-dist, cy1-upperArm, cx1+r-dist, cy1+lowerArm, 
    cx1+r+dist2, cy1+dist3,fill="red") 
    canvas.create_polygon(cx1-r+dist, cy1+upperArm, cx1-r+dist, cy1-lowerArm, 
    cx1-r-dist2, cy1+dist3,fill="red")
    
    cx2 = 320
    cy2 = 220
    canvas.create_oval(cx2-r, cy2-r, cx2+r, cy2+r, fill="yellow", width=0)
    canvas.create_polygon(cx2+r-dist, cy2-upperArm, cx2+r-dist, cy2+lowerArm, 
    cx2+r+dist2, cy2+dist3,fill="yellow") 
    canvas.create_polygon(cx2-r+dist, cy2+upperArm, cx2-r+dist, cy2-lowerArm,
    cx2-r-dist2, cy2+dist3,fill="yellow")
    
    canvas.create_text(430,90, text="Kids: Hard to infect because")
    canvas.create_text(430,105, text="moves around the most quickly.")
    canvas.create_text(430,122, text="15 points", font='Arial 14 bold')
    canvas.create_text(430,150, text="Adults: Not as hard to infect")
    canvas.create_text(430,165, text="because they move around at ")
    canvas.create_text(430,180, text="average speed.")
    canvas.create_text(430,195, text="10 points", font='Arial 14 bold')
    canvas.create_text(430,220, text="Seniors: Very easy to infect")
    canvas.create_text(432,235, text="because they move around super ")
    canvas.create_text(430,250, text="slowly.")
    canvas.create_text(430,265, text="5 points", font='Arial 14 bold')
    
    canvas.create_text(340,290, text="Scoring:", font="Arial 16 bold")
    canvas.create_text(426,308, text="The game ends when timer hits 0.")
    canvas.create_text(408,323, text="For each person you infect,")
    canvas.create_text(414,338, text="you obtain the corresponding")
    canvas.create_text(376,353, text="number of points.")
    
    #button
    canvas.create_rectangle(430,414,530,450, fill="cornsilk3", width=0)
    canvas.create_text(480,430, text="Click to Play")

####################################
# playGame LEVEL1 mode
####################################

def playGameMousePressed(event, data):
    pass
    
def playGameKeyPressed(event, data):
    if data.spacePressed == 0 and data.isGameOver == False:
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
            data.spacePressed += 1
            #produce seven rays of sneeze
            data.mainPerson.sneeze()
            data.mainPerson.sneeze()
            data.mainPerson.sneeze()
            data.mainPerson.sneeze()
            data.mainPerson.sneeze()
            data.mainPerson.sneeze()
            data.mainPerson.sneeze()

def playGameTimerFired(data): 
    #gather around stage
    for person in data.people:
        if (isInsideRealm(person.cx, person.cy, person.r) and not isInsideStage(
        person.cx, person.cy, person.r)):
            person.dx = person.dy = 0.1
    
    data.timerr += 1
    if data.timerr%10 == 0 and data.countDownLevel1 != 0:
        data.countDownLevel1 -= 1
        if data.countDownLevel1 == 0:
            data.isGameOver == True
            data.finalInfectedPeople = data.infectedPeople
            data.mode = "reportResult"
    
    #changing arms
    for person in data.people:
        #changing arms (purple young walk fastest, red middle, yellow slowest)
        if person.fill == "purple":
            if data.timerr%2==0 :
                person.armStatus+=1
                person.armStatus=person.armStatus%2
        
        if person.fill == "red":
            if data.timerr%5==0:
                person.armStatus+=1
                person.armStatus=person.armStatus%2
        
        if person.fill == "yellow":
            if data.timerr%9==0:
                person.armStatus+=1
                person.armStatus=person.armStatus%2

    for person in data.people:
        person.move(data)
        #checking people-sneeze collision
        for sneeze in data.mainPerson.sneezes:
            if person.collidesWithSneeze(sneeze):
                data.totalScore += person.score
                person.score = 0
                person.changeColor(data)
                person.isInfected = True
                person.infectedSneeze() #must call the infected func
           
        #checking people-trail collision
        for sneeze in data.mainPerson.sneezes:
            for moreSneeze in sneeze.prevLocation:
                x, y, r = moreSneeze
                if person.collidesWithTrail(x,y,r):
                    data.totalScore += person.score
                    person.score = 0
                    person.changeColor(data)
                    person.isInfected = True
                    person.infectedSneeze()
        
    #main person sneeze   
    for sneeze in data.mainPerson.sneezes:
        if sneeze.velocity <= 0:
            continue
        #a list of tuples containing previous locations
        sneeze.prevLocation.append((sneeze.sx,sneeze.sy))
        sneeze.move()
        sneeze.velocity -= 0.6    

    #randomizing sneeze time
    for person in data.people:
        if person.isInfected and person.timer > 0:
            person.timer -= 1
        if person.isInfected and person.timer <= 0 and not person.sneezed:
            person.infectedSneeze() #method changes sneezed status to true
            person.dx = person.dy = 0    
    
    #infected people sneezes
    for person in data.people:
        for sneeze in person.infectedSneezes:
            for rest in data.people:  
                if rest.collidesWithSneeze(sneeze):
                    data.totalScore += person.score
                    rest.score = 0
                    rest.changeColor(data)
                    rest.isInfected = True
                    rest.infectedSneeze() #must call the infected func
                        
    #checking other people collsion with random sneeze trail
                for moreSneeze in sneeze.prevLocation:
                    x, y, r = moreSneeze
                    if rest.collidesWithTrail(x,y,r):
                        data.totalScore += person.score
                        rest.score = 0
                        rest.changeColor(data)
                        rest.isInfected = True
                        rest.infectedSneeze()
                        
            if sneeze.velocity <= 0:
                continue
            sneeze.prevLocation.append((sneeze.sx,sneeze.sy))
            sneeze.move()
            sneeze.velocity -= 0.5

    #checking people collision
    for (i,person) in enumerate(data.people):
        for rest in data.people[i+1:]: 
            if person.collidesWithPeople(rest) and person.fill != "green":
                person.cx -= person.r #move out of collision radius
                person.cy -= person.r
                person.dx = -person.dx 
                person.dy = -person.dy
                rest.dy = -rest.dy 
                rest.dx = -rest.dx
                
def playGameRedrawAll(canvas, data):
    #backdrop
    canvas.create_rectangle(0, 0, 600, 500, fill="salmon2")
    
    for person in data.people:
        person.drawScore(canvas)
        person.draw(canvas)
        for sneeze in person.infectedSneezes:
            sneeze.drawTrail(canvas)
            
    for sneeze in data.mainPerson.sneezes:
        sneeze.drawTrail(canvas)
    
    data.mainPerson.drawMain(canvas)
    
    #level1
    Level1Background().drawBackground1(canvas)
    canvas.create_text(565, 25, text=data.countDownLevel1, font="Arial 35 bold")
    canvas.create_text(440, 480, text="Infected Percentage: " +
     str(round((data.infectedPeople/30)*100)) + "%", font="Arial 26 bold", fill=
     "green")
    canvas.create_text(110, 480, text="Score: "+str(data.totalScore), font=
    "Arial 26 bold")
        
####################################
# use the run function as-is
####################################

def run(width=300, height=300):     

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
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()   
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