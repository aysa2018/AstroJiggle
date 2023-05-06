import random
import os
import time
path = os.getcwd()
RESOL_WIDTH=1440
RESOL_HEIGHT=795
self_WIDTH=860
self_HEIGHT=688
CELL_DIMENSION=86
self_START_X=490
self_START_Y=53
NUM_ROWS=8
NUM_COLS=10
counter=0
click_list=[]
score=0

#create a Tile class for each tile of the self

class Tile:
    
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.x=self.c*CELL_DIMENSION+self_START_X
        self.y=self.r*CELL_DIMENSION+self_START_Y
        self.img = loadImage(path + "/images/" + "candy"+str(random.randint(1,5)) + ".png")
    
    def display(self):
        image(self.img, self.c * CELL_DIMENSION+self_START_X, self.r * CELL_DIMENSION+self_START_Y,CELL_DIMENSION,CELL_DIMENSION)
    
    
    def is_clicked(self):
        if mouseX >= self.x and mouseX <= self.x + CELL_DIMENSION and mouseY >= self.y and mouseY <= self.y + CELL_DIMENSION:
            return True
        else:
            return False    
        
 

        
#create a list class for all the initial tiles of the table
    
class Puzzle():
    
    def __init__(self):
        self.prevTime = millis()
        self.w=RESOL_WIDTH
        self.h=RESOL_HEIGHT
        self.tiles=[]
        self.bg_img=loadImage(path+"/images/BG.png")
        
        #make the list of the tile
        
        for r in range(NUM_ROWS):
            self.row=[]
            for c in range(NUM_COLS):
                self.row.append(Tile(r,c))
            self.tiles.append(self.row)  
   
    
        

    def display(self):
        # duration = millis()-self.prevTime
        # self.prevTime = millis()
        # print(duration)
        #load background image
        image(self.bg_img,0,0,self.w,self.h)
        
        
        
        #load background gridline of the self
        
        for i in range(self_START_X,self_START_X+self_WIDTH):
            for j in range(self_START_Y,self_START_Y+self_HEIGHT):
                if (i-self_START_X)%CELL_DIMENSION==0 and (j-self_START_Y)%CELL_DIMENSION==0:
                    stroke(180)
                    fill(200,200,255,100)
                    rect(i, j, CELL_DIMENSION, CELL_DIMENSION,10,10,10,10)
                    
        # display tiles of the table 
        
        for row in self.tiles:
            for tile in row:
                tile.display()
        if mouseX in range(self_START_X,self_START_X+self_WIDTH-1) and mouseY in range(self_START_Y,self_START_Y+self_HEIGHT-1):
        
            col=(mouseX-self_START_X)//CELL_DIMENSION
            row=(mouseY-self_START_Y)//CELL_DIMENSION
            stroke(251,72,196)
            fill(224,220,223,120)
            rect(self_START_X+CELL_DIMENSION*col,self_START_Y+CELL_DIMENSION*row,CELL_DIMENSION,CELL_DIMENSION,10,10,10,10)
        watch.display()
        score1.display()
        
    # Check for a vertical line at r1, c1
    def vLineAt(self, r1, c1):
        if r1-2 >= 0 and self.tiles[r1-2][c1] == self.tiles[r1-1][c1] and self.tiles[r1-1][c1] == self.tiles[r1][c1]:
            return True
        if r1-1 >= 0 and r1+1 < NUM_ROWS and self.tiles[r1-1][c1] == self.tiles[r1][c1] and self.tiles[r1][c1] == self.tiles[r1+1][c1]:
            return True
        if r1+2 < NUM_ROWS and self.tiles[r1][c1] == self.tiles[r1+1][c1] and self.tiles[r1+1][c1] == self.tiles[r1+2][c1]:
            return True
        
        return False
        
        # Check for a horizontal line at r1, c1
    def hLineAt(self, r1, c1):
        if c1-2 >= 0 and self.tiles[r1][c1-2] == self.tiles[r1][c1-1] and self.tiles[r1][c1-1] == self.tiles[r1][c1]:
            return True
        if c1-1 >= 0 and c1+1 < NUM_COLS and self.tiles[r1][c1-1] == self.tiles[r1][c1] and self.tiles[r1][c1] == self.tiles[r1][c1+1]:
            return True
        if c1+2 < NUM_COLS and self.tiles[r1][c1] == self.tiles[r1][c1+1] and self.tiles[r1][c1+1] == self.tiles[r1][c1+2]:
            return True
        
        return False
    
    # def canSwap(self, r1, c1, r2, c2):
    #     # Swap them
    #     self.swap(r1, c1, r2, c2)
        
    #     if self.hLineAt(r1, c1) or self.hLineAt(self, r2, c2) or self.vLineAt(self, r1, c1) or self.vLineAt(self, r2, c2):
    #         # Swap them back
    #         self.swap(r1, c1, r2, c2)
    #         return True
        
    #     # Swap them back
    #     self.swap(r1, c1, r2, c2)
        
    #     return False
                
        

        
    def swap(self,r1,c1,r2,c2):
        
        temp = self.tiles[r1][c1].img
        self.tiles[r1][c1].img = self.tiles[r2][c2].img
        self.tiles[r2][c2].img = temp
    
        
    def check_match(self):
        global score
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.vLineAt(r,c) or self.hLineAt(r,c):
                    score+=100
        
            

#create a Tile class for each tile of the self    
class StopWatch:
    def __init__(self,time):
        self.x=100
        self.y=500
        self.w=200
        self.h=100
        self.time=time

    def display(self):
        noStroke()
        fill(255,255,255)
        rect(self.x,self.y,self.w,self.h,50,50,50,50)
        if frameCount%10==0:
            if self.time>=1:
                self.time-=1
        textAlign(CENTER)
        fill(0)
        textSize(25)
        if self.time>9:
            text("00:"+str(self.time),200,560)
        else:
            text("00:0"+str(self.time),200,560)
 
#create a Tile class for each tile of the self
           
class score_self:
    def __init__(self,sc):
        self.x=100
        self.y=200
        self.w=200
        self.h=100
        global score
       

    def display(self):
        
        noStroke()
        fill(200,122,200)
        rect(self.x,self.y,self.w,self.h,50,50,50,50)
        textAlign(CENTER)
        fill(0)
        textSize(25)
        text(score,200,260)
            

        


watch=StopWatch(30)
score1=score_self(150)
puzzle=Puzzle()
# game=Game()

def setup():
    size(RESOL_WIDTH, RESOL_HEIGHT)
                       
def draw():
    
    puzzle.display()
    

def mousePressed():
    global click_list
    global counter
    counter+=1
    puzzle.check_match()
    if mouseX in range(self_START_X,self_START_X+self_WIDTH-1) and mouseY in range(self_START_Y,self_START_Y+self_HEIGHT-1):
        col=(mouseX-self_START_X)//CELL_DIMENSION
        row=(mouseY-self_START_Y)//CELL_DIMENSION
        # puzzle.swap(row,col)
        click_list.append(row)
        click_list.append(col) 
        
        

    if counter==2:

        if mouseX in range(self_START_X,self_START_X+self_WIDTH-1) and mouseY in range(self_START_Y,self_START_Y+self_HEIGHT-1):

            if (click_list[2]==click_list[0]+1 and click_list[3]==click_list[1]) or (click_list[2]==click_list[0]-1 and click_list[3]==click_list[1])or (click_list[2]==click_list[0] and click_list[3]==click_list[1]+1) or (click_list[2]==click_list[0] and click_list[3]==click_list[1]-1):
    
                puzzle.swap(click_list[0],click_list[1],click_list[2],click_list[3])
                counter=0
                click_list=[]
            else:
                counter=1
                a=click_list[0]
                b=click_list[1]
                click_list=[]
                click_list.append(a)
                click_list.append(b)
                
            
        
   



            
    
    

    
    
  
        

    

    
