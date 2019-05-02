import random
import math
from tkinter import * 

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)
        
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
 
#200,140,400,240   
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
        canvas.create_rectangle(200,140,400,240, fill=self.fill2, width=4)
        canvas.create_rectangle(220,150,380,230, fill=self.fill3, width=4)
        canvas.create_rectangle(240,160,360,220, fill=self.fill4, width=4)
        canvas.create_line(280,180,280,205, width=5)
        canvas.create_line(277,180,311,170, width=8)
        canvas.create_line(308,170,308,200, width=5)
        canvas.create_oval(275,200,285,210,fill="black")
        canvas.create_oval(303,195,313,205,fill="black")
        
        #exit
        canvas.create_rectangle(0, 0, 33, 70, fill=self.fill1, width=4)
        canvas.create_text(16, 35, text="EXIT", fill="red", font="Arial 15 bold") 
               
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
    if (data.finalInfectedPeople/30)*100 > 50:
        canvas.create_text(300,145, text="You've infected " +
        str(round((data.finalInfectedPeople/30)*100)) + " % of the people! :)", 
        font="Arial 26", fill=fill3)
    else:
        canvas.create_text(300,145, text="You've only infected " +
        str(round((data.finalInfectedPeople/30)*100)) +" % of the people :(",
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
    if event.x > 200 and event.x < 400 and event.y < 420 and event.y > 380:
        data.mode = "playGame"

def goal1KeyPressed(event, data):
    pass

def goal1TimerFired(data):
    pass

def goal1RedrawAll(canvas, data):
    canvas.create_rectangle(0,0,600,500,outline="black", fill="salmon2", 
    width=2)
    canvas.create_rectangle(100,200,500,350,fill="gray90")
    canvas.create_text(300,250,text="Your goal is to infect 50% of the",font=
    "Arial 26")
    canvas.create_text(300,300,text=" of the people at the concert",
    font="Arial 26")
    canvas.create_rectangle(200,380,400,420,fill="gray90")
    canvas.create_text(300,400,text="Continue",font="Arial 26")

####################################
# homeScreen mode
####################################

def homeScreenMousePressed(event, data):
    if event.x > 250 and event.x < 350 and event.y < 320 and event.y > 270:
        data.mode = "goal1"
    elif event.x > 250 and event.x < 350 and event.y < 400 and event.y > 350:
        data.mode = "help"

def homeScreenKeyPressed(event, data):
    pass

def homeScreenTimerFired(data):
    pass

def homeScreenRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="green4")
    canvas.create_rectangle(200,150,400,250,fill="green3", width=0)
    canvas.create_text(300, 205,text="Just Sneeeze", font="Arial 26 bold")
    canvas.create_text(data.width/2, data.height/2+50,
                        text="Play Game", font="Arial 22 bold" )
    canvas.create_text(data.width/2, data.height/2+100,
                        text="Instructions", font="Arial 22 bold" )

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
    #REMEMBER TO SAY THAT PEOPLE WILL BE EXITING SO U CANT TAKE FOREVER TO MOVE MAIN PERSON
    canvas.create_text(data.width/2, data.height/2-40,
                       text="This is help mode!", font="Arial 26 bold")
    canvas.create_text(data.width/2, data.height/2-10,
                       text="How to play:", font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+40,
                       text="Press any key to keep playing!", font="Arial 20")

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
            if data.timerr%3==0 :
                person.armStatus+=1
                person.armStatus=person.armStatus%2
        
        if person.fill == "red":
            if data.timerr%7==0:
                person.armStatus+=1
                person.armStatus=person.armStatus%2
        
        if person.fill == "yellow":
            if data.timerr%13==0:
                person.armStatus+=1
                person.armStatus=person.armStatus%2

    for person in data.people:
        person.move(data)
        '''
        #collision with stage
        if collideWithStageTop(people.cx,people.cy,people.r):
        elif collideWithStageTop(people.cx,people.cy,people.r):
        elif collideWithStageTop(people.cx,people.cy,people.r):
        elif collideWithStageTop(people.cx,people.cy,people.r):
        '''    
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
    canvas.create_text(60, 480, text="Score: "+str(data.totalScore), font=
    "Arial 20")
        
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