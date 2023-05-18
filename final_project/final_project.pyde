add_library('minim')
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
player = Minim(this)
counter=0
click_list=[]
score=0
run=True
time0=30



#create a Tile class for each tile of the board

class Tile:
    
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.x=self.c*CELL_DIMENSION+self_START_X
        self.y=self.r*CELL_DIMENSION+self_START_Y
        #assign an index from 1 to 6 for usual tile
        self.ind = random.randint(1,6)
        self.img = loadImage(path + "/images/" + "candy"+str(self.ind) + ".png")
        
    #display the tile
    def display(self):
        image(self.img, self.c * CELL_DIMENSION+self_START_X, self.r * CELL_DIMENSION+self_START_Y,CELL_DIMENSION,CELL_DIMENSION)
        
    #create an upadate function for updating the index(1-6 for regular tiles, 0 for empty tile, 7 for special power tile)
    def update(self,ind):
        self.ind=ind
        self.img = loadImage(path + "/images/" + "candy"+str(self.ind) + ".png")
    
    
#create a puzzle class for the whole game
    
class Puzzle():
    
    def __init__(self):
        
        self.w=RESOL_WIDTH
        self.h=RESOL_HEIGHT
        self.levelpage=False
        self.gamestart=False
        self.gameover=False
        self.tiles=[]
        self.empty=0
        
        #initialize the sound
        self.bg_sound = player.loadFile(path + "/sounds/bg_music.wav")
        self.swap_sound = player.loadFile(path + "/sounds/swap.wav")
        self.magic_sound = player.loadFile(path + "/sounds/magic.mp3")
        try:
            self.bg_sound.loop()
        except AttributeError:
            print("Sometimes this version of Processing gives an error")
        
        #initialize an attribute for storing the game
        self.name=''
        self.bg_sound.loop()
        
        #initialize the attributes for loading images
        self.bg_img=loadImage(path+"/images/bg_game.png")
        self.bg_img1=loadImage(path+"/images/bg_menu.png")
        self.bg_img2=loadImage(path+"/images/bg_gameover.png")
        self.bg_img3=loadImage(path+"/images/bg_level.png")
        
        
        #make the board, a list of the tiles
        
        for r in range(NUM_ROWS):
            self.row=[]
            for c in range(NUM_COLS):
                self.row.append(Tile(r,c))
            self.tiles.append(self.row)  
       

    def display(self):
        
        #load background image
        image(self.bg_img,0,0,self.w,self.h)
        
        #load background gridlines of the board
        
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
                
        #display highlighted tiles while hovered over
        if mouseX in range(self_START_X,self_START_X+self_WIDTH-1) and mouseY in range(self_START_Y,self_START_Y+self_HEIGHT-1):
        
            col=(mouseX-self_START_X)//CELL_DIMENSION
            row=(mouseY-self_START_Y)//CELL_DIMENSION
            stroke(251,72,196)
            fill(224,220,223,120)
            rect(self_START_X+CELL_DIMENSION*col,self_START_Y+CELL_DIMENSION*row,CELL_DIMENSION,CELL_DIMENSION,10,10,10,10)
        
        #call the display of the objects of other classes
        watch.display()
        score1.display()
        
        
        #highlight the selected tile
        global click_list
        if click_list:
            r=click_list[0]
            c=click_list[1]
            if self.tiles[r][c].ind!=0:
                noFill()
                stroke(251,30,250)
                strokeWeight(5)
                rect(self_START_X+c*CELL_DIMENSION,self_START_Y+r*CELL_DIMENSION,CELL_DIMENSION,CELL_DIMENSION,10,10,10,10)
                strokeWeight(1)
            

            
     #create a function for swapping the tile images   
    def swap(self,r1,c1,r2,c2):
        
        temp = self.tiles[r1][c1].img
        self.tiles[r1][c1].img = self.tiles[r2][c2].img
        self.tiles[r2][c2].img = temp
        
        #play sound when swapped
        self.swap_sound.rewind()
        self.swap_sound.play()
        temp = self.tiles[r1][c1].ind
        self.tiles[r1][c1].ind = self.tiles[r2][c2].ind
        self.tiles[r2][c2].ind = temp

    # create a function for detecting more than 2 tile in a row or column 
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
        global time0
        
        #check the right side of selected tile
        for j in range(c+1,NUM_COLS):
            if self.tiles[r][j].ind==self.tiles[r][c].ind:
                right_counter+=1
            else:
                break
            
        #check the left side of selected tile   
        for j in range(c-1,-1,-1):
            if self.tiles[r][j].ind==self.tiles[r][c].ind:
                left_counter+=1
            else:
                break
        
        #if there is a streak of 3 or more than 3 tiles in a row
        if (right_counter+left_counter+1)>=3:
            
            h_indicator=True
            start_col=c-left_counter
            end_col=c+right_counter
            
        
        for j in range(start_col,end_col+1):
            
            #check the bottom rows of selected tile
            for i in range(r+1,NUM_ROWS):
                
                if self.tiles[i][j].ind==self.tiles[r][j].ind:
                    bottom_counter+=1
                else:
                    break
                
            #check the bottom rows of selected tile
            for i in range(r-1,-1,-1):
                
                if self.tiles[i][j].ind==self.tiles[r][j].ind:
                    top_counter+=1
                else:
                    break
            
            #if there is a streak of 3 or more than 3 tiles in a row    
            if (top_counter+bottom_counter+1)>=3:
                
                v_indicator=True
                start_r=r-top_counter
                end_r=r+bottom_counter
                
        #if there is a vertical streak, call the function for removing the tiles, increase the score   
        if  v_indicator:
            self.remove_v_tiles(start_r,end_r,c)
            score=score+(end_r-start_r+1)*100
            
            #if there is a vertical streak of more than 3 tiles, generate the power tile in a random tile of the board   
            if (end_r-start_r)>=3:
                random_row=random.randint(0,7)
                random_col=random.randint(0,9)
                self.tiles[random_row][random_col].update(7)
                self.falling()
         #if there is a horizontal streak, call the function for removing the tiles, increase the score       
        if  h_indicator:
            self.remove_h_tiles(start_col,end_col,r)
            score=score+(end_col-start_col+1)*100
            
            #if there is a horizontal streak, call the function for removing the tiles, increase the score
            if (end_col-start_col)>=3:
                random_row=random.randint(0,7)
                random_col=random.randint(0,9)
                self.tiles[random_row][random_col].update(7)
                self.falling()
                
        # if the player matches one streak, increase 2 seconds time
        if (v_indicator or h_indicator):
            time0+=2
        
             
        return (v_indicator or h_indicator)
    
     # create a function for removing vertical tiles
    def remove_v_tiles(self,start,ending,column):
        try:
            for i in range(start,ending+1):
    
                self.tiles[i][column].update(0)
                self.falling()
        except IndexError:
            print("Error")
            
        
     # create a function for removing horizontal tiles       
    def remove_h_tiles(self,start,ending,row):
        for j in range(start,ending+1):
            self.tiles[row][j].update(0)
            self.falling()  
            
   # create a function for checking if there is an empty file
    def check_empty(self,r,c):
        if r==0:
            return 0
        if self.tiles[r][c].ind==0:
            return self.check_empty(r-1,c)

        else:
            return r
    
    
    #create a function for dropping the tile when the tiles below are empty          
    def falling(self):
        global run
        if run == True:
            run = False
    
    
        for i in range(NUM_ROWS-1,0,-1):
            for j in range(NUM_COLS):
                if self.tiles[i][j].ind==0:
                    r=self.check_empty(i,j)

                    self.tiles[i][j].update(self.tiles[r][j].ind)
                    self.tiles[r][j].update(0)
                        
                    run = True
      
    
    
     #make a menu page function   
    def menu(self):
        image(self.bg_img1,0,0,RESOL_WIDTH,RESOL_HEIGHT)
        #load the font
        font=createFont("BobaCups.otf",22)
        textFont(font,22)
        textAlign(CENTER)
        fill(0,0,255)
        textSize(32)
        text("Enter your name here:",RESOL_WIDTH//2-30,355)
        textFont(font,22)
        textAlign(LEFT)
        fill(0,0,255)
        textSize(32)
        text(self.name,RESOL_WIDTH//2+160,355)
        
        
        
        textSize(24)
        fill(0,0,255)
        textAlign(CENTER)
        text("CREDITS: AYSA BINTE MASUD \n JEXI LO ",RESOL_WIDTH//2-30,555)
        
     #make a level page function   
    def level(self):
        
        image(self.bg_img3,0,0,RESOL_WIDTH,RESOL_HEIGHT)
        
        
        
    #check whether the game is over
    def check_game_over(self):
        global time0
        global score
        
        #when time ended
        if time0==0:
            self.gameover=True
        self.empty=0
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                if self.tiles[i][j].ind==0:
                    self.empty+=1
                    
        #when someone vanishes all the tiles from the board        
        if self.empty>=80:
            self.gameover=True
            
        
            
            
    #make a gameover page function  
        
    def display_gameover_screen(self):
        
        image(self.bg_img2,0,0,RESOL_WIDTH,RESOL_HEIGHT)
        global score
        textAlign(CENTER)
        fill(0,59,255)
        textSize(32)
    
        text("PLAYER: "+str(self.name),RESOL_WIDTH//2,RESOL_HEIGHT//2-10)
        textSize(32)
        fill(0,59,255)
        text("SCORE: "+"\n"+str(score),245,585)

        text("Press ENTER to go back to main menu",RESOL_WIDTH//2,562)
        
        rect(621,607,198,60,30,30,30,30)
        textSize(24)
        fill(255,255,255)
        text("Menu",RESOL_WIDTH//2,645)
        
            
#create a Tile class for the stopwatch shown beside the board in the game    
class StopWatch:
    def __init__(self):
        
        self.time_sound = player.loadFile(path + "/sounds/timeup.mp3")
        global time0
        
    #display the score
    def display(self):
        global time0
        
        #the game gets a bit slower for all the complex functions, that's why frameCount modulus 20 is written instead of frameCount modulus 60 for making it a realistic stopwatch
        if frameCount%20==0:
            if time0>=1:
                time0-=1
        textAlign(CENTER)
        fill(0,59,255)
        textSize(32)
        if time0>9:
            text("00:"+str(time0),245,380)
        else:
            text("00:0"+str(time0),245,380)
            
        #play the timeover sound when only 3 second is left
        if time0==3:
            self.time_sound.play()
            
 
#create a Tile class for the score board beside the tile board in the game
           
class score_self:
    def __init__(self):
        
        global score
       

    def display(self):
        
       
        textAlign(CENTER)
        fill(0,59,255)
        textSize(32)
        text(score,245,670)
            

        

#create an object of each class
watch=StopWatch()
score1=score_self()
puzzle=Puzzle()


def setup():
    size(RESOL_WIDTH, RESOL_HEIGHT)
 
                          
def draw():
    
    #display the menu page, level page, game screen and gameover screen
    if not puzzle.gamestart:
        if not puzzle.levelpage:
            puzzle.menu()
        else:
            puzzle.level()
    else: 
        puzzle.display()
        
    #check whether the game is over
    
    puzzle.check_game_over()
            
    if  puzzle.gameover:
        puzzle.gamestart=False
        puzzle.display_gameover_screen()
        
    
        
def keyPressed():
    global time0
    global score
    
    #input the player's name in the menu page
    if puzzle.levelpage==False:
        
        #only take uppercase letters
        
        if keyCode<= ord('Z') and keyCode>= ord('A'):
            puzzle.name+=chr(keyCode)
            
        #delete letter if backspace is pressed
        if key==BACKSPACE:
            puzzle.name = puzzle.name[:-1]
    

    if puzzle.levelpage==False and key==ENTER:
        puzzle.levelpage=True
        
    #Up for easy level and down for hard level
    if puzzle.levelpage==True:
        if keyCode==UP:
            time0=15
            puzzle.gamestart=True
            puzzle.levelpage=False
            
        elif keyCode==DOWN:
            time0=10
            puzzle.gamestart=True
            puzzle.levelpage=False
            
     #go back to main menu while pressed enter       
    if  puzzle.gameover:
        if keyCode==10:
            if puzzle.bg_sound.isPlaying():
                puzzle.bg_sound.pause()
            puzzle.__init__()
            time0=30
            score = 0
            
        
    
    
   

def mousePressed():
    global click_list
    global counter
    global time0
    global score
    
    

    
    
    #append the row and column of the clicked tile in the click_list list
    if puzzle.gamestart:
        counter+=1
        
        if mouseX in range(self_START_X,self_START_X+self_WIDTH-1) and mouseY in range(self_START_Y,self_START_Y+self_HEIGHT-1):
            col=(mouseX-self_START_X)//CELL_DIMENSION
            row=(mouseY-self_START_Y)//CELL_DIMENSION
            
            # puzzle.swap(row,col)
            click_list.append(row)
            click_list.append(col) 
        
        
        #only occurs for the second selected tile
        if counter==2:
            #chech whether the mouse is inside the board
            if mouseX in range(self_START_X,self_START_X+self_WIDTH-1) and mouseY in range(self_START_Y,self_START_Y+self_HEIGHT-1):
                
                #check if they are neighboring tile
                if (click_list[2]==click_list[0]+1 and click_list[3]==click_list[1]) or (click_list[2]==click_list[0]-1 and click_list[3]==click_list[1])or (click_list[2]==click_list[0] and click_list[3]==click_list[1]+1) or (click_list[2]==click_list[0] and click_list[3]==click_list[1]-1):
                    
                    #if the first selected tile is a power
                    if puzzle.tiles[click_list[0]][click_list[1]].ind==7:
                        
                        #detect the color of the second seleted tile
                        index=puzzle.tiles[click_list[2]][click_list[3]].ind
                        for i in range(NUM_ROWS-1,-1,-1):
                            for j in range(NUM_COLS):
                                if puzzle.tiles[i][j].ind==index:
                                    #delete all the tiles of same color, increase the score for each tile and play the sound
                                    puzzle.tiles[i][j].update(0)
                                    puzzle.magic_sound.rewind()
                                    puzzle.magic_sound.play()
                                    score+=100
                                    
                         #vanish the power tile and the other selected tile as well and increase the score for these two tiles           
                        puzzle.tiles[click_list[0]][click_list[1]].update(0)
                        puzzle.tiles[click_list[2]][click_list[3]].update(0)
                        score+=200
                        
                        #call the falling function after vanishing the tiles
                        
                        puzzle.falling()
                        
                        #empty the list and set the counter to 0 after vanishing
                        counter=0
                        click_list=[]
                    
                    #if the second selected tile is a power
                    elif puzzle.tiles[click_list[2]][click_list[3]].ind==7:
                        
                        #detect the color of the first seleted tile
                        index=puzzle.tiles[click_list[0]][click_list[1]].ind
                        for i in range(NUM_ROWS-1,-1,-1):
                            for j in range(NUM_COLS):
                                if puzzle.tiles[i][j].ind==index:
                                    #delete all the tiles of same color, increase the score for each tile and play the sound
                                    puzzle.tiles[i][j].update(0)
                                    puzzle.magic_sound.rewind()
                                    puzzle.magic_sound.play()
                                    score+=100
                        #vanish the power tile and the other selected tile as well and increase the score for these two tiles           
                        puzzle.tiles[click_list[0]][click_list[1]].update(0)
                        puzzle.tiles[click_list[2]][click_list[3]].update(0)
                        score+=200
                        #call the falling function after vanishing the tiles
                        puzzle.falling()
                        
                        #empty the list and set the counter to 0 after vanishing
                        counter=0
                        click_list=[]
                                    
                     #swap if both of the tiles are non-empty tiles and not the same colored tiles           
                    elif puzzle.tiles[click_list[0]][click_list[1]].ind!=0 and puzzle.tiles[click_list[2]][click_list[3]].ind!=0 and (puzzle.tiles[click_list[0]][click_list[1]].ind!=puzzle.tiles[click_list[2]][click_list[3]].ind):
                        puzzle.swap(click_list[0],click_list[1],click_list[2],click_list[3])
                        
                        #if there is no streak, change the tiles back to their places
                        
                        if not puzzle.detect_streak(click_list[0],click_list[1]) and not puzzle.detect_streak(click_list[2],click_list[3]):
                            puzzle.swap(click_list[0],click_list[1],click_list[2],click_list[3])
                            
                        #empty the list and set the counter to 0 after vanishing
                        counter=0
                        click_list=[]
                
                    else:
                        counter=0
                        click_list=[]
                else:
                    
                    #select the last tile that was clicked if any neighboring tiles are chosen
                    
                    counter=1
                    a=click_list[2]
                    b=click_list[3]
                    click_list=[]
                    click_list.append(a)
                    click_list.append(b)
                    
            
        




            
    
    

    
    

        

    

    
