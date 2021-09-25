import pygame
import os
import random

pygame.init()
pygame.font.init()

FONT = pygame.font.SysFont("arial", 30)
FONT2 = pygame.font.SysFont("arial", 15)

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
def draw_window(character, asteroidlist):
  win.blit(BACKGROUND, (0,0)) #image, coords it starts at
  #win.fill((0, 0, 0)) #fills screen with black
  #pygame.draw.rect(win, (0, 0, 255), character)#draws it on the screen
  win.blit(SHIP, (character.x, character.y)) 
  
  for thing in asteroidlist:
      win.blit(ASTEROID, (thing.x, thing.y))
      
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

def lost():
  running = True
  while running:
    lost_words = FONT.render("YOU LOST", 1, (0,0,0))
    lost_box = pygame.Rect(WIDTH / 2 - 250, HEIGHT / 2 - 150, 500, 300) #created rectangle in middle
    pygame.draw.rect(win, (255, 255, 255), lost_box)
    win.blit(lost_words, (WIDTH/2 - lost_words.get_width()/2, HEIGHT/2 - lost_words.get_height()/2)) #puts words in center
    #display score later
    #store score as high score if greater than previous
    #^ or we can put this before lost() is called
    pygame.display.update()

def main():
  clock = pygame.time.Clock()
  pygame.time.set_timer(ADDASTEROID, 20)
  
  running = True
  mc = pygame.Rect(WIDTH*0.2, HEIGHT * 0.5, CHAR_WIDTH, CHAR_HEIGHT)#makes a character
  #mc.image = pygame.Surface[CHAR_WIDTH,CHAR_HEIGHT]
  asteroidlist = []

  #asteroid = pygame.Rect(WIDTH*0.2, HEIGHT * 0.5, )
  while running:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT: #when u press x button
        running = False
      if event.type == ADDASTEROID and random.random() < 0.1:
        create_asteroids(asteroidlist)
      if event.type == HITASTEROID:
        running = False
        lost()
        
        
    clock.tick(60) 
    
    keys_pressed = pygame.key.get_pressed() #move more smoothly
    move(mc, keys_pressed)
    move_asteroids(asteroidlist)
    check_collision(mc, asteroidlist)
    draw_window(mc, asteroidlist)

  pygame.quit()

if __name__ == '__main__': #checks if name is main
    main()