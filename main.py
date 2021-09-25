import pygame
import os
import random

pygame.init()
pygame.font.init()

FONT = pygame.font.SysFont("arial", 30)
FONT2 = pygame.font.SysFont("arial", 10)

WIDTH, HEIGHT = 1000, 600
CHAR_WIDTH, CHAR_HEIGHT = 50, 50
ASTEROID_WIDTH, ASTEROID_HEIGHT = 50, 50
CHAR_SPEED = 20

BACKGROUND = pygame.image.load(os.path.join("pictures", "spaceback.png"))#image for background
SHIP = pygame.transform.scale(pygame.image.load(os.path.join("pictures","spaceship.png")), (CHAR_WIDTH, CHAR_HEIGHT))#image for main character
ASTEROID = pygame.transform.scale(pygame.image.load(os.path.join("pictures","asteroid.png")),(CHAR_WIDTH,CHAR_HEIGHT))#image for asteroid

ADDASTEROID = pygame.USEREVENT + 1
HITASTEROID = pygame.USEREVENT + 2

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE INVADERS RIP OFF")#who did this^  lmao  
from pygame.locals import(
  K_UP,#keys
  K_DOWN,
  K_LEFT,
  K_RIGHT,
  QUIT
)

#function for drawing
def draw_window(character, asteroidlist, score):
  win.blit(BACKGROUND, (0,0)) #image, coords it starts at
  #win.fill((0, 0, 0)) #fills screen with black
  #pygame.draw.rect(win, (0, 0, 255), character)#draws it on the screen
  win.blit(SHIP, (character.x, character.y)) 
  
  for thing in asteroidlist:
      win.blit(ASTEROID, (thing.x, thing.y))

  score_string = FONT.render("Score: " + str(score), 1, (255,255,255))
  win.blit(score_string, (0,0))
      
  pygame.display.update() #updates the window

#function for moving the character
def move(character, keys_pressed):
  if keys_pressed[pygame.K_UP] and character.y > 0: 
    character.y -= CHAR_SPEED
  if keys_pressed[pygame.K_DOWN] and character.y + CHAR_HEIGHT < HEIGHT: 
    character.y += CHAR_SPEED
  if keys_pressed[pygame.K_LEFT] and character.x > 0: 
    character.x -= CHAR_SPEED
  if keys_pressed[pygame.K_RIGHT] and character.x + CHAR_WIDTH < WIDTH: 
    character.x += CHAR_SPEED

#max 12 asteroids
def create_asteroids(asteroidlist): 
  for count in range (12):
    y = count * ASTEROID_HEIGHT
    random_num = random.random()
    if random_num < 0.05:
      asteroid = pygame.Rect(WIDTH, y, ASTEROID_WIDTH, ASTEROID_HEIGHT)
      asteroidlist.append(asteroid)


def move_asteroids(asteroidlist):
  for a in asteroidlist:
    a.x -= 10
    if a.x + ASTEROID_WIDTH < 0:
      asteroidlist.remove(a)
      del a

def check_collision(character, asteroidlist):
  for a in asteroidlist:
    if character.colliderect(a):
      pygame.event.post(pygame.event.Event(HITASTEROID))

def lost(HIGHSCOREFROMFILE):
  lost_words = FONT.render("YOU LOST", 1, (0,0,0))
  replay_words = FONT.render("Press SPACE to replay", 1, (0,0,0))
  score_string = FONT.render("HIGH SCORE: " + str(HIGHSCOREFROMFILE), 1, (0,0,0))

  lost_box = pygame.Rect(WIDTH / 2 - 250, HEIGHT / 2 - 150, 500, 300) #created rectangle in middle
  pygame.draw.rect(win, (255, 255, 255), lost_box)

  win.blit(lost_words, (WIDTH/2 - lost_words.get_width()/2, HEIGHT/2 - 3*replay_words.get_height()/2))
  win.blit(replay_words, (WIDTH/2 - replay_words.get_width()/2, HEIGHT/2 - replay_words.get_height()/2))
  win.blit(score_string, (WIDTH/2 - score_string.get_width()/2, HEIGHT/2 + replay_words.get_height()/2))

  pygame.display.update()

def draw_menu():
  started = False

  while not started:
    win.fill((255,255,255)) #fills scren with white
    MENU_MESSAGE = FONT.render("Press the spacebar to start!", 1, (0,0,0))
    win.blit(MENU_MESSAGE, (WIDTH/2 - MENU_MESSAGE.get_width()/2, HEIGHT/2 - MENU_MESSAGE.get_height()/2))
    
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          started = True
            
    pygame.display.update() #updates the window
  

def main():
  draw_menu()

  score = 0
  HIGHSCORE = score
  
  while True:
    
    clock = pygame.time.Clock()
    pygame.time.set_timer(ADDASTEROID, 20)
    
    running = True
    mc = pygame.Rect(WIDTH*0.2, HEIGHT * 0.5, CHAR_WIDTH, CHAR_HEIGHT)#makes a character
    #mc.image = pygame.Surface[CHAR_WIDTH,CHAR_HEIGHT]
    asteroidlist = []

  #asteroid = pygame.Rect(WIDTH*0.2, HEIGHT * 0.5, )
    while running:
      
      clock.tick(60) 
      score += 1
      f=open("hscore.txt")
      HIGHSCOREFROMFILE = int(f.read())
      f.close()

      for event in pygame.event.get():
        if event.type == pygame.QUIT: #when u press x button
          running = False
        if event.type == ADDASTEROID and random.random() < 0.1:
          create_asteroids(asteroidlist)
        if event.type == HITASTEROID:
          running = False
          if score > HIGHSCORE:
            HIGHSCORE = score
          if score > HIGHSCOREFROMFILE:
            bb=open("hscore.txt","w")
            bb.write(str(score))
            bb.close()
            aa=open("hscore.txt","r")
            HIGHSCOREFROMFILE = int(aa.read())
            aa.close()
        
      
      keys_pressed = pygame.key.get_pressed() #move more smoothly
      move(mc, keys_pressed)
      move_asteroids(asteroidlist)
      check_collision(mc, asteroidlist)
      draw_window(mc, asteroidlist, score)
      
    while not running:
      lost(HIGHSCOREFROMFILE)
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            running = True
            score = 0

  pygame.quit()

if __name__ == '__main__': #checks if name is main
    main()