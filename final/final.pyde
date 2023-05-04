import random
import os
import time
path = os.getcwd()
RESOL_WIDTH=1440
RESOL_HEIGHT=795
BOARD_WIDTH=860
BOARD_HEIGHT=688
CELL_DIMENSION=86
BOARD_START_X=490
BOARD_START_Y=53
NUM_ROWS=8
NUM_COLS=10
counter=0
click_list=[]

#create a Tile class for each tile of the board

class Tile:
    
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.x=self.c*CELL_DIMENSION+BOARD_START_X
        self.y=self.r*CELL_DIMENSION+BOARD_START_Y
        self.img = loadImage(path + "/images/" + "candy"+str(random.randint(1,6)) + ".png")
    
    def display(self):
        image(self.img, self.c * CELL_DIMENSION+BOARD_START_X, self.r * CELL_DIMENSION+BOARD_START_Y,CELL_DIMENSION,CELL_DIMENSION)
    
    
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
        duration = millis()-self.prevTime
        self.prevTime = millis()
        print(duration)
        #load background image
        image(self.bg_img,0,0,self.w,self.h)
        
        
        
        #load background gridline of the board
        
        for i in range(BOARD_START_X,BOARD_START_X+BOARD_WIDTH):
            for j in range(BOARD_START_Y,BOARD_START_Y+BOARD_HEIGHT):
                if (i-BOARD_START_X)%CELL_DIMENSION==0 and (j-BOARD_START_Y)%CELL_DIMENSION==0:
                    stroke(180)
                    fill(200,200,255,100)
                    rect(i, j, CELL_DIMENSION, CELL_DIMENSION,10,10,10,10)
                    
        # display tiles of the table 
        
        for row in self.tiles:
            for tile in row:
                tile.display()
        if mouseX in range(BOARD_START_X,BOARD_START_X+BOARD_WIDTH-1) and mouseY in range(BOARD_START_Y,BOARD_START_Y+BOARD_HEIGHT-1):
        
            col=(mouseX-BOARD_START_X)//CELL_DIMENSION
            row=(mouseY-BOARD_START_Y)//CELL_DIMENSION
            stroke(251,72,196)
            fill(224,220,223,120)
            rect(BOARD_START_X+CELL_DIMENSION*col,BOARD_START_Y+CELL_DIMENSION*row,CELL_DIMENSION,CELL_DIMENSION,10,10,10,10)
        watch.display()
        score.display()
        
  

        
    def swap(self,r1,c1,r2,c2):
    
        temp = self.tiles[r1][c1]
        self.tiles[r1][c1] = self.tiles[r2][c2]
        self.tiles[r2][c2] = temp
        
        temp = self.tiles[r1][c1].img
        self.tiles[r1][c1].img = self.tiles[r2][c2].img
        self.tiles[r2][c2].img = temp
        
        
   

#create a Tile class for each tile of the board    
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
 
#create a Tile class for each tile of the board
           
class score_board:
    def __init__(self,score):
        self.x=100
        self.y=200
        self.w=200
        self.h=100
        self.score=score
       

    def display(self):
        
        noStroke()
        fill(200,122,200)
        rect(self.x,self.y,self.w,self.h,50,50,50,50)
        textAlign(CENTER)
        fill(0)
        textSize(25)
        text(self.score,200,260)
            

        


watch=StopWatch(30)
score=score_board(150)
puzzle=Puzzle()
# game=Game()

def setup():
    size(RESOL_WIDTH, RESOL_HEIGHT)
                       
def draw():
    
    puzzle.display()
    

def mouseClicked():
    global click_list
    global counter
    counter+=1
    
    if mouseX in range(BOARD_START_X,BOARD_START_X+BOARD_WIDTH-1) and mouseY in range(BOARD_START_Y,BOARD_START_Y+BOARD_HEIGHT-1):
        col=(mouseX-BOARD_START_X)//CELL_DIMENSION
        row=(mouseY-BOARD_START_Y)//CELL_DIMENSION
        # puzzle.swap(row,col)
        click_list.append(row)
        click_list.append(col) 
        
        

    if counter==2:
        # print(click_list[0],click_list[1],click_list[2],click_list[3])
        puzzle.swap(click_list[0],click_list[1],click_list[2],click_list[3])
        counter=0
        click_list=[]
        
        
   



            
    
    

    
    
  
        

    

    
