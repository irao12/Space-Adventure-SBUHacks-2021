import pygame
import os

pygame.init()
WIDTH, HEIGHT = 1000, 600
CHAR_WIDTH, CHAR_HEIGHT = 50, 50
CHAR_SPEED = 20;

BACKGROUND = pygame.image.load(os.path.join("pictures", "spaceback.png"))#image for background
SHIP = pygame.transform.scale(pygame.image.load(os.path.join("pictures","spaceship.png")), (CHAR_WIDTH, CHAR_HEIGHT))#image for main character
ASTEROID = pygame.transform.scale(pygame.image.load(os.path.join("pictures","asteroid.png")),(CHAR_WIDTH,CHAR_HEIGHT))#image for asteroid

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE INVADERS RIP OFF")#who did this^  lmao  
from pygame.locals import(
  K_UP,                 #keys
  K_DOWN,
  K_LEFT,
  K_RIGHT,
  QUIT
)

#function for drawing
def draw_window(character):
  win.blit(BACKGROUND, (0,0))
  #win.fill((0, 0, 0)) #fills screen with black
  #pygame.draw.rect(win, (0, 0, 255), character)#draws it on the screen
  win.blit(SHIP, (character.x, character.y))
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

def main():
  clock = pygame.time.Clock()
  running = True
  mc = pygame.Rect(WIDTH*0.2, HEIGHT * 0.5, CHAR_WIDTH, CHAR_HEIGHT)#makes a character
  #mc.image = pygame.Surface[CHAR_WIDTH,CHAR_HEIGHT]
  #asteroid = pygame.Rect(WIDTH*0.2, HEIGHT * 0.5, )
  while running:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT: #when u press x button
        running = False
        
    clock.tick(60) 
    keys_pressed = pygame.key.get_pressed() #move more smoothly
    move(mc, keys_pressed)
    draw_window(mc)
  
  pygame.quit()

if __name__ == '__main__': #checks if name is main
    main()