import pygame, random, time, sys, json
from pygame import mixer

score = 0
speed = 5

width = 1280
height = 720

pygame.init()
mixer.init()
pygame.font.init()

logo = pygame.image.load('data/images/Logo.png')
pygame.display.set_icon(logo)

Arial = pygame.font.SysFont('Arial',35)


screen = pygame.display.set_mode((1280, 720))
screan = pygame.display.set_mode((1280, 720))

gameDisplay = pygame.display.set_mode((width, height))


pygame.display.set_caption('Sytro v0.1.0')

clock = pygame.time.Clock()


mixer.music.load("data/sound/Main-Music.mp3")

mixer.music.set_volume(100)

mixer.music.play(loops = 1000)



RGB1 = 1
RGB2 = 2
RGB3 = 3


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


enemy_size = 50
enemy_pos = [random.randint(5,width-enemy_size), 1]
enemy_list = [enemy_pos]
class Score:
  
  def __init__(self):
    self.gain = 1
    self.score = 0
    self.figScore = 0
    
  def plussScore(self):
    if self.score >= 100:
      self.gain += 1
      self.score = 0
    self.score += self.gain
    self.figScore += self.gain
    
    print(self.gain)
    return self.figScore

score = Score()


def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 200 and delay < 0.1:
        x_pos = random.randint(0,width-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])
        
        
def draw_ememies(enemy_list, COLLOR2):
   for enemy_pos in enemy_list:
       pygame.draw.rect(screan, COLLOR2, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)) 
       time.sleep(0.001)
def update_enemy_pos(enemy_list, score):
  
  
    for idx, enemy_pos in enumerate(enemy_list):
       if enemy_pos [1] >= 0 and enemy_pos[1] < height:
         enemy_pos[1] += speed
       else:
         enemy_list.pop(idx)
         score += 1
         pygame.display.update()
    return score
  
  
while True:
  for ev in pygame.event.get():
    if ev.type == pygame.QUIT:
      
      pygame.quit()   
        
  RGB1 += 1
  RGB2 += 2
  RGB3 += 3
  
  if RGB1 >= 255:
   RGB1 = 0
  if RGB2 >= 255:
   RGB2 = 0
  if RGB3 >= 255:
   RGB3 = 0
  if RGB1 <= 10 and RGB2 <= 10 and RGB3 <= 10:
    RGB3, RGB2, RGB1 = 69, 69, 69
    
  color = (RGB1,RGB2,RGB3)
  
  screan.fill(black)
  
  text = Arial.render('+'+str(score.gain) , True , white)
  
  draw_ememies(enemy_list, color)
  update_enemy_pos(enemy_list, 720)
  
  mouse = pygame.mouse.get_pos()
  
  if ev.type == pygame.MOUSEBUTTONDOWN:		
			#if the mouse is clicked on the
			# button the game is terminated
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
      drop_enemies(enemy_list)
      score.plussScore()
  if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
    pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
    
  else:
   pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
   
  scoreText = Arial.render( 'Score: '+str(score.figScore) , True , white)
	# superimposing the text onto our button
  screen.blit(text , (width/2+13, height/2+5))
  
  screen.blit(scoreText , (30, 30))
  
  clock.tick(60)
  
  
  pygame.display.update()

