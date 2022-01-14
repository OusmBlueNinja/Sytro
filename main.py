import sys, random, pygame
from pygame import mixer


# initializing the constructor
pygame.init()
mixer.init()
# screen resolution
res = (720,720)
mixer.music.load("data/sound/Main-Music.mp3")
mixer.music.set_volume(100)
mixer.music.play(loops = 1000)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255,255,255)

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
pink = (60,25,60)

# light shade of the button
color_light = (170,170,170)

# dark shade of the button
color_dark = (100,100,100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel',35)
Arial = pygame.font.SysFont('Arial',35)

class Score:
  def __init__(self):
    self.addsub = ''
    self.score = 0
  
  def updateScore(self, addsub, amount):
    if addsub =='+':
      self.score += amount
      print(self.score)
    if addsub == '-':
      self.score -= amount
    if addsub == 'return':
      return self.score
    
  def getRes():
    print(res[0]/2, res[1]/1)
    
score = Score()
# rendering a text written in
# this font
text = smallfont.render('Click Me ' , True , color)

class fallingBackround:
  def __init__(self):
    self.entities = []
    self.entitiePos = []
    self.x = 0
    self.y = 100
  
  def newEntitie(self):
    self.entities.append(len(self.entities))
    self.x = random.randrange(0,720)
    self.y = 0
    self.entitiePos.append([self.x, self.y])
    
  def entitieFall(self):
    self.entitiePos[0] -= 1
    for entities in self.entitiePos:
    	pygame.draw.rect(screen, red, (self.entitiePos[0], self.entitiePos[1], 20, 20)) 
    
    
    
    
    
    
    
    
 
    
  
  

back = fallingBackround()
back.newEntitie()
while True:
	
	for ev in pygame.event.get():
		
		if ev.type == pygame.QUIT:
			pygame.quit()
			

    
	back.entitieFall()

	# fills the screen with a color
	screen.fill(black)
	
	# stores the (x,y) coordinates into
	# the variable as a tuple
	mouse = pygame.mouse.get_pos()
	
	# if mouse is hovered on a button it
	# changes to lighter shade
	if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
		pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
		
	else:
		pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
  
  
	scoreText = Arial.render( 'Score: '+str(score.updateScore('return', None)) , True , color)
	# superimposing the text onto our button
	screen.blit(text , (width/2+13, height/2 + 5))
	screen.blit(scoreText , (30, 30))
	# updates the frames of the game
	pygame.display.update()
