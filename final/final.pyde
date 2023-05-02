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
bool= False

#create a Tile class for each tile of the board

class Tile:
    
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.img = loadImage(path + "/images/" + "candy"+str(random.randint(1,6)) + ".png")
    
    def display(self):
        image(self.img, self.c * CELL_DIMENSION+BOARD_START_X, self.r * CELL_DIMENSION+BOARD_START_Y,CELL_DIMENSION,CELL_DIMENSION)
        
        

 
#create a Selected Tile class for each tile of the board    
# class selected_tile:
    
#     def __init__(self, x, y):
#         self.row =(y-BOARD_START_Y)//CELL_DIMENSION
#         self.col =(x-BOARD_START_X)//CELL_DIMENSION
        
#     def display(self):
#         noStroke()
#         fill(224,220,223,120)
#         rect(BOARD_START_X+CELL_DIMENSION*self.col,BOARD_START_Y+CELL_DIMENSION*self.row,CELL_DIMENSION,CELL_DIMENSION)
        
#create a list class for all the initial tiles of the table
    
class Puzzle(list):
    
    def __init__(self):
        self.prevTime = millis()
        self.w=RESOL_WIDTH
        self.h=RESOL_HEIGHT
        self.bg_img=loadImage(path+"/images/BG.png")

        
        #make the list of the tile
        
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                self.append(Tile(r,c))

                       

    def display(self):
        # duration = millis()-self.prevTime
        # self.prevTime = millis()
        # print(duration)
        #load background image
        image(self.bg_img,0,0,self.w,self.h)
        
        #load background of the board
        
        fill(248,200,220,150)
        rect(BOARD_START_X,53,BOARD_WIDTH,BOARD_HEIGHT,2,2,2,2)
        
        #load background gridline of the board
        
        for i in range(BOARD_START_X,BOARD_START_X+BOARD_WIDTH):
            for j in range(BOARD_START_Y,BOARD_START_Y+BOARD_HEIGHT):
                if (i-BOARD_START_X)%CELL_DIMENSION==0 and (j-BOARD_START_Y)%CELL_DIMENSION==0:
                    stroke(180)
                    noFill()
                    rect(i, j, CELL_DIMENSION, CELL_DIMENSION)
                    
        # display tiles of the table 
        
        for tile in self:
            tile.display()
        if mouseX in range(BOARD_START_X,BOARD_START_X+BOARD_WIDTH-1) and mouseY in range(BOARD_START_Y,BOARD_START_Y+BOARD_HEIGHT-1):
        
            col=(mouseX-BOARD_START_X)//CELL_DIMENSION
            row=(mouseY-BOARD_START_Y)//CELL_DIMENSION
            stroke(251,72,196)
            fill(224,220,223,120)
            rect(BOARD_START_X+CELL_DIMENSION*col,BOARD_START_Y+CELL_DIMENSION*row,CELL_DIMENSION,CELL_DIMENSION)
        watch.display()
        score.display()
        
    def swap(self,r,c):
        # find the tile behind r and c
        for t1 in self:
            if t1.r == r and t1.c == c:
                break
                
        # check is any of the tile neighbours the empty one (i.e. with v=16)
        emptyNeighbourTile = None
        for n in [[0,-1],[0,1],[1,0],[-1,0]]:
            for t2 in self:
                if t2.r == t1.r+n[0] and t2.c == t1.c+n[1]:
                    emptyNeighbourTile = t2
                    break
            if emptyNeighbourTile != None:
                break
        
        # if that is true then find the empty tile and swap the tiles 
        if emptyNeighbourTile != None:
            tmp = t1.r
            t1.r = emptyNeighbourTile.r 
            emptyNeighbourTile.r = tmp
        
            tmp = t1.c
            t1.c = emptyNeighbourTile.c 
            emptyNeighbourTile.c = tmp

        

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
    background(210)
                       
def draw():
    background(210)
    # game.display()
    puzzle.display()

def mouseClicked():
    
    if mouseX in range(BOARD_START_X,BOARD_START_X+BOARD_WIDTH-1) and mouseY in range(BOARD_START_Y,BOARD_START_Y+BOARD_HEIGHT-1):
        col=(mouseX-BOARD_START_X)//CELL_DIMENSION
        row=(mouseY-BOARD_START_Y)//CELL_DIMENSION
        
    puzzle.swap(row,col)
    
    
    
    

    
    
  
        

    

    
            
    
    

    
