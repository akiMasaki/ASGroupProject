import pygame
import sys
# Add the folder path to the sys.path list
sys.path.append('mob/')
sys.path.append('tower/')
sys.path.append('gameStats/')
sys.path.append('map/')
import mob_dwarf
import mob_runner
import tower
import gameStats

def playTitle():
    screen.blit(titleImage, titleImage_position)
    screen.blit(title1, (155,50))
    screen.blit(title2, (50,100))
    pygame.display.flip()


    
gameStats = gameStats.GameStats()
gameStats.setLevel('Title')

pygame.init()
screen = pygame.display.set_mode((720,670))

#background = pygame.Surface(screen.get_size())
#background.fill((140,206,250))

titleImage = pygame.image.load( "images/title_image.jpg" )
titleImage_position = titleImage.get_rect()

defaultFont = pygame.font.Font('fonts/miriamfixed.ttf', 48 )
title1 = defaultFont.render('CLFS', 0, (0,0,0))
title2 = defaultFont.render('Tower Defence', 0, (0,0,0))

# MAIN GAME LOOP
while gameStats.getLevel()!=None:
    pygame.event.pump()
    keyinput = pygame.key.get_pressed()
    if keyinput[pygame.K_ESCAPE] or pygame.event.peek(pygame.QUIT):
        break
    
    if gameStats.getLevel() == 'Title':
        playTitle()



