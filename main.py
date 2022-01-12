

#Imports
from pygame import draw, mixer
import json, sys, time, pygame, random
from pygame.locals import *
from pygame import font 

#colors
red = (255,0,0)
orange = (255,165,0)
yellow = (255,255,0)
green = (0,255,0)
blue = 	(0,0,255)
purple = (255,0,255)
white = (255,255,255)
black =  (0,0,0)
grey = (12, 24, 36)

#Load Files

logo=pygame.image.load('data/images/Logo.png')
Player=pygame.image.load('data/images/Player.png')



#debug
DEBUG = True
Playing = True
Tryed = False

#init stuffs
mixer.init()
pygame.init()



#asked if you want full screan
Fullscrean = False

if Fullscrean:
  WIDTH = 1920
  HEIGHT = 1080
  win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
else: 
  WIDTH = 1280
  HEIGHT = 720
  win = pygame.display.set_mode((WIDTH, HEIGHT))

#Constants
TITLE = "Sytro v0.5"

#pygame initialization

pygame.display.set_caption(TITLE)
pygame.display.set_icon(logo)
clock = pygame.time.Clock()

#sizes
size = [22, 22]


def Music_Player(PlayPause, needload):
    if needload == True:
      mixer.music.load("data/sounds/Main-Music.mp3")
        
    if PlayPause == 'play':
      mixer.music.set_volume(100)
      mixer.music.play()
    if PlayPause == 'pause':
      mixer.music.pause()
      

def moveComputer():
    prob = random.randrange(0, 1)
    if prob >= 1:
        randommovement = 4
    else:
        randommovement = random.randrange(1,3)
    if Playing == True: 
        
    
      if computer.y <= 1:
          randommovement = 3
      if randommovement == 1:
          computer.left_pressed = True
      else:
          player.left_pressed = False
      if randommovement == 2:
          computer.right_pressed = True
      else:
          player.right_pressed = False
      if randommovement == 4:
          computer.up_pressed = True
      else:
          player.up_pressed = False
      if randommovement == 3:
          computer.down_pressed = True
      else:
          player.down_pressed = False
      if randommovement == 0:
          computer.down_pressed = True
      else:
          player.down_pressed = False
    else:
        computer.down_pressed = True
        computer.down_pressed = True
        computer.up_pressed = True
        computer.up_pressed = True
        computer.down_pressed = True
        computer.down_pressed = True
        computer.up_pressed = True
        computer.up_pressed = True


# Makes It So You Cant Go Out Of Bounds⁡
def Bounds():
    if Player.y <= 1:
        Player.right_pressed = True
    else:
        Player.right_pressed = False
        
def drawGround():
    pygame.draw.rect(win, (0,255,0), (0, (WIDTH -100), 200, 1000)) 
    
        

#Player Class
class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = white
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 3
        self.canGoDown = True
    
    def draw(self, win):
        #pygame.draw.rect(win, self.color, self.rect)
        win.blit(pygame.image.load('data/images/Player.png'),(self.x, self.y))

    def update(self):
        self.velX = 0
        self.velY = 0
        
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
            
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
            
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
            
        if self.down_pressed and not self.up_pressed and self.canGoDown == True:
            self.velY = self.speed
            
        
        self.x += self.velX
        self.y += self.velY
        
        if DEBUG == True:
          print(self.y, self.x, self.velX, self.velY, self.speed)

        self.rect = pygame.Rect(int(self.x), int(self.y), 22, 22)
    
    
    def Gravity(self):
        self.Grav_Speed = 2.3
        if self.y <= (HEIGHT - 100):
          self.y += self.Grav_Speed
          self.canGoDown = True

        else:
         self.canGoDown = False
                   
        
        
        
        
class COMPUTER:
    def __init__(self, x, y):
        self.x = int(random.randrange(0, WIDTH))
        self.y = int(random.randrange(0, HEIGHT))
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = red
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 1
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        
    
    def update(self):
        self.velX = 0
        self.velY = 0
        
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
            
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
            
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
            
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
            
        
        self.x += self.velX
        self.y += self.velY
          

        self.rect = pygame.Rect(int(self.x), int(self.y), size[0], size[0])

#Player Initialization
player = Player(WIDTH/2, HEIGHT/2)
computer = COMPUTER(WIDTH/2, HEIGHT/3)

def colide(playery, playerx, computery, computerx, size):
    p_x = playerx
    p_y = playery
    player_size = size[0]
    enemy_size = size[1]

    e_x = computerx
    e_y = computery
    if  (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
       if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
           return True
    return False

#Main Loop
Music_Player('play', True)
while Playing:
    if colide(player.y, player.x, computer.y, computer.x, size):
        Playing = False
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
            
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.left_pressed = True
            if event.key == pygame.K_d:
                player.right_pressed = True
            #if Player.canGoDown == False:  
            if event.key == pygame.K_w:
                player.up_pressed = True
            if event.key == pygame.K_s:
                player.down_pressed = True
            if event.key == pygame.K_LSHIFT:
                player.speed = 4
                
                
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.left_pressed = False
            if event.key == pygame.K_d:
                player.right_pressed = False
            if event.key == pygame.K_w:
                player.up_pressed = False
            if event.key == pygame.K_s:
                player.down_pressed = False
            if event.key == pygame.K_LSHIFT:
                player.speed = 3
                
    #moveComputer()
        
    #Draw
    win.fill(grey)  
    player.Gravity()
    computer.draw(win)
    player.draw(win)
    
    drawGround()
    

    #update
    player.update()
    computer.update()
    
    pygame.display.flip()
    clock.tick(240)


Music_Player('pause', False)
while not Playing:
    if DEBUG == True and Tryed == False:
        print('game over')
        Tryed = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print('restarting')
                Playing = True    