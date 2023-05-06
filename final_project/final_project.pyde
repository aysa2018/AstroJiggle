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
EMPTY=-1

#create a Tile class for each tile of the self

class Tile:
    
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.x=self.c*CELL_DIMENSION+self_START_X
        self.y=self.r*CELL_DIMENSION+self_START_Y
        self.ind = random.randint(1,6)
        self.img = loadImage(path + "/images/" + "candy"+str(self.ind) + ".png")
    
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
        

        
    def swap(self,r1,c1,r2,c2):
        
        temp = self.tiles[r1][c1].img
        self.tiles[r1][c1].img = self.tiles[r2][c2].img
        self.tiles[r2][c2].img = temp
        
        temp = self.tiles[r1][c1].ind
        self.tiles[r1][c1].ind = self.tiles[r2][c2].ind
        self.tiles[r2][c2].ind = temp
        
    def detect_streak(self,r,c):
   
        
        top_counter=0
        bottom_counter=0
        left_counter=0
        right_counter=0
        h_indicator=False
        v_indicator=False
        end_col=c
        start_col=c
        start_r=r
        end_r=r
        
            
        for j in range(c+1,NUM_COLS):
            print("RIGHT SEARCH ",self.tiles[r][j].ind,self.tiles[r][c].ind)
            if self.tiles[r][j].ind==self.tiles[r][c].ind:
                right_counter+=1
                
            else:
                break
            
                
        for j in range(c-1,-1,-1):
            print("LEFT SEARCH ",self.tiles[r][j].ind,self.tiles[r][c].ind)
            if self.tiles[r][j].ind==self.tiles[r][c].ind:
                left_counter+=1
                
            else:
                break
        
        
        print("RIGHT CNT: ",right_counter,"LEFT CNT: ",left_counter)
        if (right_counter+left_counter+1)>=3:
            print("OHOHOHOHOHOHOHOHO")
            h_indicator=True
            start_col=c-left_counter
            end_col=c+right_counter
        
        
        for j in range(start_col,end_col+1):

            for i in range(r+1,NUM_ROWS):
                print("BOTTOM SEARCH ",self.tiles[i][j].ind,self.tiles[r][j].ind)
                if self.tiles[i][j].ind==self.tiles[r][j].ind:
                    bottom_counter+=1
                    
                else:
                    break
            for i in range(r-1,-1,-1):
                print("TOP SEARCH ",self.tiles[i][j].ind,self.tiles[r][j].ind)
                if self.tiles[i][j].ind==self.tiles[r][j].ind:
                    top_counter+=1
                
                else:
                    break
                
            if (top_counter+bottom_counter+1)>=3:
                print("HEHEHEHEHEHEH")
                v_indicator=True
                start_r=r-top_counter
                end_r=r+bottom_counter
            
            
            
        if  v_indicator:
            self.remove_v_tiles(start_r,end_r,c)
        if  h_indicator:
            self.remove_h_tiles(start_col,end_col,r)
        
        
        print("TOP CNT: ",top_counter,"BOT CNT: ",bottom_counter)
             
        return (v_indicator or h_indicator)
        
    def remove_v_tiles(self,start,ending,column):
        for i in range(start,ending+1):
            a=loadImage(path + "/images/" + "candy"+str(0) + ".png")
            
            self.tiles[i][column].img=a
            self.tiles[i][column].ind=0
            
    def remove_h_tiles(self,start,ending,row):
        for j in range(start,ending+1):
            a=loadImage(path + "/images/" + "candy"+str(0) + ".png")
            self.tiles[row][j].img=a
            self.tiles[row][j].ind=0
        
       
        
        
            
                
                
                    
    # def allSame(self,a, b, c, d=None, e=None):
    #     if d == None and e == None:
    #         if a.img == b.img and b.img == c.img:
    #             return True
    #         return False
    #     if e == None:
    #         if a.img == b.img and b.img == c.img and c.img== d.img:
    #             return True
    #         return False
    #     if a.img == b.img and b.img == c.img and c.img == d.img and d.img == e.img:
    #         return True
    #     return False
        
    # def check_match(self):
    #     global score
    #     # 3 horizontal
        
    #     for r in range(NUM_ROWS - 1, -1, -1):
    #         for c in range(NUM_COLS-2):
    
    #             if self.allSame(self.tiles[r][c],self.tiles[r][c+1],self.tiles[r][c+2]):
    #                 print(score)
    #                 self.tiles[r][c] = None
    #                 self.tiles[r][c+1] = None
    #                 self.tiles[r][c+2] = None
    #                 score+=100
    #                 print("h",score)
               
        
    #     # 3 vertical
    #     for r in range(NUM_ROWS- 2 - 1, -1, -1):
    #         for c in range(NUM_COLS):
    #             if self.allSame(self.tiles[r][c], self.tiles[r+1][c], self.tiles[r+2][c]):
    #                 self.tiles[r][c] = None
    #                 self.tiles[r+1][c] = None
    #                 self.tiles[r+2][c] = None
    #                 score+=100
    #                 print("v",score)
                
                
                

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
    def __init__(self):
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
score1=score_self()
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
    # puzzle.check_match()
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
                
                # print("CHECKING IND: ",click_list[2],click_list[3])
                # print(puzzle.detect_streak(click_list[2],click_list[3]))
                # print(puzzle.detect_streak(click_list[2],click_list[3]))
                
                if not puzzle.detect_streak(click_list[0],click_list[1]) and not puzzle.detect_streak(click_list[2],click_list[3]):
                    puzzle.swap(click_list[0],click_list[1],click_list[2],click_list[3])
                    
                counter=0
                click_list=[]
                # puzzle.check_match()
            else:
                counter=1
                a=click_list[0]
                b=click_list[1]
                click_list=[]
                click_list.append(a)
                click_list.append(b)
                
            
        
   



            
    
    

    
    
  
        

    

    
