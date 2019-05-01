import random
import math
from tkinter import * 

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
        
        self.timer = random.randint(8, 20)
        #will have scores 10, 15 in higher levels
        self.score = random.choice([25,50,75,100])
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.sneezed = False
        #self.inGreenZone = False
                
        self.infectedSneezes = []
        self.infectedPeople = 0
        
        self.armStatus = 0
    
    #arm status1
    def draw(self, canvas):
        if self.armStatus == 0:
            canvas.create_oval(self.cx-self.r, self.cy-self.r, self.cx+self.r,
            self.cy+self.r, fill=self.fill, width=0)
            
            upperArm = lowerArm = 5
            dist = 2
            dist2 = 3
            dist3 = 10
            canvas.create_polygon(self.cx+self.r-dist, self.cy-upperArm, self.cx+
            self.r-dist, self.cy+lowerArm, self.cx+self.r+dist2, self.cy-dist3,
            fill=self.fill) 
            canvas.create_polygon(self.cx-self.r+dist, self.cy+upperArm, self.cx-
            self.r+dist, self.cy-lowerArm, self.cx-self.r-dist2, self.cy+dist3,
            fill=self.fill) 
        
        elif self.armStatus == 1:
            canvas.create_oval(self.cx-self.r, self.cy-self.r, self.cx+self.r,
            self.cy+self.r, fill=self.fill, width=0)
            
            upperArm = lowerArm = 5
            dist = 2
            dist2 = 3
            dist3 = 10
            canvas.create_polygon(self.cx+self.r-dist, self.cy-upperArm, self.cx+
            self.r-dist, self.cy+lowerArm, self.cx+self.r+dist2, self.cy+dist3,
            fill=self.fill) 
            canvas.create_polygon(self.cx-self.r+dist, self.cy+upperArm, self.cx-
            self.r+dist, self.cy-lowerArm, self.cx-self.r-dist2, self.cy-dist3,
            fill=self.fill)  
        '''
        elif self.armStatus == 2:
            canvas.create_oval(self.cx-self.r, self.cy-self.r, self.cx+self.r,
            self.cy+self.r, fill=self.fill, width=0)
            
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
            ''' 
    
    def drawScore(self, canvas):
        canvas.create_text(self.cx, self.cy-13, text=str(self.score), font = 
        "Arial 10")
    
    def move(self, data):
        #varying speeds for different ages
        if self.fill == "purple":
            if self.dx == -1:
                self.dx -= 4
            elif self.dx == 1:
                self.dx += 4
            if self.dy == -1:
                self.dy -= 4
            elif self.dy == 1:
                self.dy += 4
        elif self.fill == "red":
            if self.dx == -1:
                self.dx -= -2
            elif self.dx == 1:
                self.dx += 2
            if self.dy == -1:
                self.dy -= 2
            elif self.dy == 1:
                self.dy += 2
                
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
 
    def changeColor(self):
        if self.score == 75:
            self.fill = "pale green"
        elif self.score == 50:
            self.fill = "green yellow"
        elif self.score == 25:
            self.fill = "medium sea green"
        elif self.score == 0:
            self.fill = "green"
        self.inGreenZone = True
    
    def infectedSneeze(self):
        SneezeClass = Sneeze(-5,-5,(0,0))
        randAngle = random.uniform(0, 2*math.pi)
        dx = math.cos(randAngle)*SneezeClass.velocity
        dy = -math.sin(randAngle)*SneezeClass.velocity
        
        if self.isInfected and not self.sneezed and self.timer<=0:
            self.infectedSneezes.append(Sneeze(self.cx,self.cy,(dx,dy)))
            self.sneezed = True
            
'''
    def isInsideStage(self, x, y, r):
        
    
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
'''   
    
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
        canvas.create_rectangle(0, 0, 33, 70, fill=self.fill1, width=4)
        canvas.create_text(16, 35, text="EXIT", fill="red", font="Arial 15 bold")
        
class ReportLose(object):
    def __init__(self):
        self.fill1 = "yellow"
        self.fill2 = "light goldenrod"
    
    def draw(self, canvas):
        canvas.create_rectangle(0,0,600,500,fill=self.fill1,width=0)
        canvas.create_rectangle(200,250,400,310,fill=self.fill2,width=0)
        #canvas.create_text("you infected # people before time ran out)
        canvas.create_rectangle(200,320,400,380,fill=self.fill2,width=0)
        '''
        if data.infectedPeople/30 < 70:
            canvas.create_text()
        else:
            canvas.create_text()
        '''
        
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
    data.countDownLevel1 = 20
    data.timer = 0
    data.infectedPeople = 0
    data.isGameOver = False
    
def mousePressed(event, data):
    if (data.mode == "homeScreen"): 
        homeScreenMousePressed(event, data)
    elif (data.mode == "playGame"): 
        playGameMousePressed(event, data)
    elif (data.mode == "help"): 
        helpMousePressed(event, data)
    elif (data.mode == "goal1"): 
        goal1MousePressed(event, data)    

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
    canvas.create_rectangle(100,200,500,350,fill="gray90", stipple="gray50")
    canvas.create_text(300,250,text="Your goal is to infect 70% of the",font=
    "Arial 26")
    canvas.create_text(300,300,text=" of the people at (_____) concert",
    font="Arial 26")
    canvas.create_rectangle(200,380,400,420,fill="gray90",stipple="gray50")
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
    canvas.create_text(data.width/2, data.height/2-60,
                       text="Just Sneeze (will import graphics and gradient)", font="Arial 26 bold")
    canvas.create_text(data.width/2, data.height/2+50,
                        text="Play Game", font="Arial 22 bold" )
    canvas.create_text(data.width/2, data.height/2+100,
                        text="Help", font="Arial 22 bold" )

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
    data.timer += 1
    if data.timer%10 == 0 and data.countDownLevel1 != 0:
        data.countDownLevel1 -= 1
        if data.countDownLevel1 == 0:
            data.isGameOver == True
                #finalInfectedPeople = data.infectedPeople
    
    #changing arms
    for person in data.people:
        #changing arms (purple young walk fastest, red middle, yellow slowest)
        if person.fill == "purple":
            if data.timer%8==0 :
                person.armStatus+=1
                person.armStatus=person.armStatus%2
        
        if person.fill == "red":
            if data.timer%13==0:
                person.armStatus+=1
                person.armStatus=person.armStatus%2
        
        if person.fill == "yellow":
            if data.timer%19==0:
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
                if person.score == 25:
                    person.score = 0
                    person.dx = person.dy = 0
                    person.changeColor()
                    person.isInfected = True
                    data.infectedPeople += 1
                    person.infectedSneeze() #must call the infected func
                elif person.inGreenZone and person.score != 0:
                    person.score -= 25
           
        #checking people-trail collision
        for sneeze in data.mainPerson.sneezes:
            for moreSneeze in sneeze.prevLocation:
                x, y, r = moreSneeze
                if person.collidesWithTrail(x,y,r):
                    if person.score == 20:
                        person.score = 0
                        person.changeColor()
                        person.isInfected = True
                        data.infectedPeople += 1
                        person.infectedSneeze()
                    elif person.score != 20 and person.score != 0:
                        person.score -= 20
        
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
    
    #infected people sneezes
    for person in data.people:
        for sneeze in person.infectedSneezes:
            for rest in data.people:  
                if rest.collidesWithSneeze(sneeze):
                    if rest.score <= 5:
                        rest.score = 0
                        rest.dx = rest.dy = 0
                        rest.changeColor()
                        rest.isInfected = True
                        data.infectedPeople += 1
                        rest.infectedSneeze() #must call the infected func
                    elif rest.score > 5:
                        rest.score -= 5   
                        
    #checking other people collsion with random sneeze trail
    for person in data.people:
        for sneeze in person.infectedSneezes:
            for rest in data.people:
                for moreSneeze in sneeze.prevLocation:
                    x, y, r = moreSneeze
                    if rest.collidesWithTrail(x,y,r):
                        rest.inGreenZone = True 
                        if rest.score <= 5:
                            rest.score = 0
                            rest.changeColor()
                            rest.isInfected = True
                            data.infectedPeople += 1
                            rest.infectedSneeze()
                        elif rest.score > 5 and rest.score != 0:
                            rest.score -= 5
                        
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
     str(round(data.infectedPeople/30)) + "%", font="Arial 26 bold", fill=
     "green")
    
    if data.countDownLevel1 == 0:
        ReportLose().draw(canvas)
        
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