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
run=True
time=1000
easy=False
advanced=True

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



class EmptyTile():
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.x=self.c*CELL_DIMENSION+self_START_X
        self.y=self.r*CELL_DIMENSION+self_START_Y
        self.ind = 0
        self.img = loadImage(path + "/images/" + "candy"+str(self.ind) + ".png")
    def display(self):
        image(self.img, self.c * CELL_DIMENSION+self_START_X, self.r * CELL_DIMENSION+self_START_Y,CELL_DIMENSION,CELL_DIMENSION)
    
    
#create a list class for all the initial tiles of the table
    
class Puzzle():
    
    def __init__(self):
        self.prevTime = millis()
        self.w=RESOL_WIDTH
        self.h=RESOL_HEIGHT
        self.levelpage=False
        self.gamestart=False
        self.gameover=False
        self.tiles=[]
        self.bg_img=loadImage(path+"/images/BG.png")
        self.bg_img1=loadImage(path+"/images/BG1.png")

        
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
                    fill(255,255,255,100)
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
        global score
        
        for j in range(c+1,NUM_COLS):
            if self.tiles[r][j].ind==self.tiles[r][c].ind:
                right_counter+=1
            else:
                break
            
        for j in range(c-1,-1,-1):
            if self.tiles[r][j].ind==self.tiles[r][c].ind:
                left_counter+=1
            else:
                break
        
    
        if (right_counter+left_counter+1)>=3:
            
            h_indicator=True
            start_col=c-left_counter
            end_col=c+right_counter
        
        for j in range(start_col,end_col+1):
            for i in range(r+1,NUM_ROWS):
                
                if self.tiles[i][j].ind==self.tiles[r][j].ind:
                    bottom_counter+=1
                else:
                    break
            for i in range(r-1,-1,-1):
                
                if self.tiles[i][j].ind==self.tiles[r][j].ind:
                    top_counter+=1
                else:
                    break
                
            if (top_counter+bottom_counter+1)>=3:
                
                v_indicator=True
                start_r=r-top_counter
                end_r=r+bottom_counter
            
        if  v_indicator:
            self.remove_v_tiles(start_r,end_r,c)
            score=score+(end_r-start_r+1)*100
        if  h_indicator:
            self.remove_h_tiles(start_col,end_col,r)
            score=score+(end_col-start_col+1)*100
        
        
             
        return (v_indicator or h_indicator)
        
    def remove_v_tiles(self,start,ending,column):
        for i in range(start,ending+1):
            self.tiles[i][column]=EmptyTile(i,column)

            # if frameCount % 10 == 0:
            # self.falling()
            
    def remove_h_tiles(self,start,ending,row):
        for j in range(start,ending+1):
            self.tiles[row][j]=EmptyTile(row,j)
            # if frameCount % 10 == 0:
            # self.falling()   
            
    # def falling(self):
    #     global run
    #     while run == True:
    #         run = False
      
    #     for r in range(NUM_ROWS - 2, 0, -1):
    #         for c in range(NUM_COLS):
    #             if self.tiles[r][c].ind != 0 and self.tiles[r+1][c].ind == 0:
    #                 temp=self.tiles[r][c].ind
    #                 self.tiles[r][c].ind = self.tiles[r-1][c].ind
    #                 self.tiles[r+1][c].ind = temp
    #                 temp=self.tiles[r][c].img
    #                 self.tiles[r][c].img = self.tiles[r-1][c].img
    #                 self.tiles[r+1][c].img = temp
                   
    #     for c in range(NUM_COLS):
    #         if self.tiles[0][c].ind==0:
    #             self.tiles[0][c].ind=random.randint(1,6)
    #     run = True
    
        
    def menu(self):
        image(self.bg_img1,0,0,RESOL_WIDTH,RESOL_HEIGHT)
        textAlign(CENTER)
        fill(0,0,255)
        textSize(45)
        text("Enter your name here:_ _ _ _ ",RESOL_WIDTH//2-30,355)
        
        fill(0,0,255)
        rect(590,420,195,50,50,50,50,50)
        textAlign(CENTER)
        fill(255,255,255)
        textSize(25)
        text("RULES",RESOL_WIDTH//2-30,455)
        fill(0,0,255)
        rect(590,520,195,50,50,50,50,50)
        textSize(25)
        fill(255,255,255)
        text("LEADERBOARD",RESOL_WIDTH//2-30,555)
        fill(0,0,255)
        rect(590,620,195,50,50,50,50,50)
        textSize(25)
        fill(255,255,255)
        text("CREDITS",RESOL_WIDTH//2-30,655)
        
    def level(self):
        global easy
        global advanced
        image(self.bg_img1,0,0,RESOL_WIDTH,RESOL_HEIGHT)
        textAlign(CENTER)
        font=createFont("BobaCups.otf",22)
        textFont(font,22)
        fill(0,0,255)
        textSize(22)
        text("LEVELS",RESOL_WIDTH//2-30,355)
        
        fill(0,0,255)
        rect(590,420,195,50,50,50,50,50)
        textAlign(CENTER)
        fill(255,255,255)
        textSize(22)
        text("EASY",RESOL_WIDTH//2-30,455)
        fill(0,0,255)
        rect(590,520,195,50,50,50,50,50)
        textSize(22)
        fill(255,255,255)
        text("REGULAR",RESOL_WIDTH//2-30,555)
        fill(0,0,255)
        rect(590,620,195,50,50,50,50,50)
        textSize(22)
        fill(255,255,255)
        text("ADVANCED",RESOL_WIDTH//2-30,655)
        
    
                
        
            
    
        
    
    
    
    def check_game_over(self):
        global time
        if time==0:
            self.gameover=True
            
            
        
    def display_gameover_screen(self):
        bg_img=loadImage(path+"/images/BG.png")
        image(bg_img,0,0,RESOL_WIDTH,RESOL_HEIGHT)
        global score
        textAlign(CENTER)
        fill(255,0,0)
        textSize(25)
        text("GAMEOVER",RESOL_WIDTH//2,RESOL_HEIGHT//2-10)
        textSize(15)
        fill(0,0,0)
        text("Your score: "+str(score),RESOL_WIDTH//2,RESOL_HEIGHT//2+20)
        
        
            
#create a Tile class for each tile of the self    
class StopWatch:
    def __init__(self,t):
        self.x=100
        self.y=500
        self.w=200
        self.h=100
        global time
        time=t

    def display(self):
        global time
        noStroke()
        fill(255,255,255)
        rect(self.x,self.y,self.w,self.h,50,50,50,50)
        if frameCount%10==0:
            if time>=1:
                time-=1
        textAlign(CENTER)
        fill(0)
        textSize(25)
        if time>9:
            text("00:"+str(time),200,560)
        else:
            text("00:0"+str(time),200,560)
 
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
    
    
    if not puzzle.gamestart:
        if not puzzle.levelpage:
            puzzle.menu()
        else:
            puzzle.level()
    else: 
        puzzle.display()
    
    puzzle.check_game_over()
            
    if  puzzle.gameover:
        puzzle.gamestart=False
        puzzle.display_gameover_screen()
    
        
def keyPressed():
    global time
    global easy
    global advanced
    if puzzle.levelpage==False and key==ENTER:
        puzzle.levelpage=True
    
   

def mousePressed():
    global click_list
    global counter
    global time
    

    if puzzle.levelpage==True:
        if mouseX in range(590,590+195) and mouseY in range(420,420+50):
            time=40
        elif mouseX in range(590,590+195) and mouseY in range(520,520+50):
            time=30
        elif mouseX in range(590,590+195) and mouseY in range(620,620+50):
            time=20
            
        puzzle.gamestart=True
        puzzle.levelpage=False
    
    if puzzle.gamestart:
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
                    if puzzle.tiles[click_list[0]][click_list[1]].ind!=0 and puzzle.tiles[click_list[2]][click_list[3]].ind!=0 and (puzzle.tiles[click_list[0]][click_list[1]].ind!=puzzle.tiles[click_list[2]][click_list[3]].ind):
                        puzzle.swap(click_list[0],click_list[1],click_list[2],click_list[3])
                    
                        if not puzzle.detect_streak(click_list[0],click_list[1]) and not puzzle.detect_streak(click_list[2],click_list[3]):
                            puzzle.swap(click_list[0],click_list[1],click_list[2],click_list[3])
                        
                        counter=0
                        click_list=[]
                    # puzzle.check_match()
                    else:
                        counter=0
                        click_list=[]
                else:
                    counter=1
                    a=click_list[0]
                    b=click_list[1]
                    click_list=[]
                    click_list.append(a)
                    click_list.append(b)
                    
            
        




            
    
    

    
    

        

    

    
