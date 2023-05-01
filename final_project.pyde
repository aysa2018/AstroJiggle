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

class Tile:
    
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.img = loadImage(path + "/images/" + "img"+str(random.randint(1,4)) + ".png")
    
    def display(self):
        image(self.img, self.c * CELL_DIMENSION+BOARD_START_X, self.r * CELL_DIMENSION+BOARD_START_Y,CELL_DIMENSION,CELL_DIMENSION)
        
# class selected_tile:
    
#     def __init__(self, x, y):
#         self.row =(y-BOARD_START_Y)//CELL_DIMENSION
#         self.col =(x-BOARD_START_X)//CELL_DIMENSION
   
#     def display(self):
#         noStroke()
#         fill(224,220,223,120)
#         rect(BOARD_START_X+CELL_DIMENSION*self.col,BOARD_START_Y+CELL_DIMENSION*self.row,CELL_DIMENSION,CELL_DIMENSION)
        
        
class Puzzle(list):
    
    def __init__(self):
        self.prevTime = millis()
        self.w=RESOL_WIDTH
        self.h=RESOL_HEIGHT
        self.bg_img=loadImage(path+"/images/layer_0.png")
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                self.append(Tile(r,c))

                       

    def display(self):
        # duration = millis()-self.prevTime
        # self.prevTime = millis()
        # print(duration)
        
        image(self.bg_img,0,0,self.w,self.h)
        fill(248,200,220,50)
        rect(BOARD_START_X,53,BOARD_WIDTH,BOARD_HEIGHT)
        
        for i in range(BOARD_START_X,BOARD_START_X+BOARD_WIDTH):
            for j in range(BOARD_START_Y,BOARD_START_Y+BOARD_HEIGHT):
                if (i-BOARD_START_X)%CELL_DIMENSION==0 and (j-BOARD_START_Y)%CELL_DIMENSION==0:
                    stroke(180)
                    noFill()
                    rect(i, j, CELL_DIMENSION, CELL_DIMENSION)
        for tile in self:
            tile.display()
        watch.display()
        score.display()
        

def print_display(x,y):
    col=(x-BOARD_START_X)//CELL_DIMENSION
    row=(y-BOARD_START_Y)//CELL_DIMENSION
    noStroke()
    fill(224,220,223,120)
    rect(BOARD_START_X+CELL_DIMENSION*col,BOARD_START_Y+CELL_DIMENSION*row,CELL_DIMENSION,CELL_DIMENSION)
   

        
    
class StopWatch:
    def __init__(self,time):
        self.x=100
        self.y=500
        self.w=200
        self.h=100
        self.time=time

    def display(self):
        
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
            
class score_board:
    def __init__(self,score):
        self.x=100
        self.y=200
        self.w=200
        self.h=100
        self.score=score
       

    def display(self):
        
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
    if mouseX in range(BOARD_START_X,BOARD_START_X+BOARD_WIDTH-1) and mouseY in range(BOARD_START_Y,BOARD_START_Y+BOARD_HEIGHT-1):
        print_display(mouseX,mouseY)
    
# def mousePressed():
#     if mouseX in range(BOARD_START_X,BOARD_START_X+BOARD_WIDTH-1) and mouseY in range(BOARD_START_Y,BOARD_START_Y+BOARD_HEIGHT-1):
#         cur_tile=selected_tile(mouseX,mouseY)
#         cur_tile.display()
    
    

    
    
  
        

    

    
