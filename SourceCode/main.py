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

from pygame.locals import * # for getting mouse pos
    
def playTitle():
    title1 = defaultFont.render('CLFS', 0, (0,0,0))
    title2 = defaultFont.render('Tower Defence', 0, (0,0,0))
    playText = defaultFont.render('Play', 0, (0,0,0))
    exitText = defaultFont.render('Exit', 0, (0,0,0))
    
    titleImage = pygame.image.load('images/title_image.jpg')
    titleImage_position = titleImage.get_rect()
    
    screen.blit(titleImage, titleImage_position)
    screen.blit(title1, (155,50))
    screen.blit(title2, (50,100))
    screen.blit(playText, (285,363))
    screen.blit(exitText, (285,451))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if (mousePos[0] >= 257 and  mousePos[0] <= 428) and (mousePos[1] >= 348 and  mousePos[1] <= 421):
                gameStats.setLevel('MapSelect')
            if (mousePos[0] >= 257 and  mousePos[0] <= 428) and (mousePos[1] >= 436 and  mousePos[1] <= 509):
                pygame.quit()
            
    pygame.display.flip()

def playMapSelect():
    background = pygame.Surface(screen.get_size())
    background.fill((140,206,250))
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
    
    pygame.display.flip()

#MAIN 
    
levelSelect = {'Title':playTitle, 'MapSelect':playMapSelect}

gameStats = gameStats.GameStats()
gameStats.setLevel('Title')

pygame.init()
screen = pygame.display.set_mode((720,670))
pygame.display.set_caption('CLFS Tower Defence')
defaultFont = pygame.font.Font('fonts/miriamfixed.ttf', 48 )


# MAIN GAME LOOP
while gameStats.getLevel()!=None:
    pygame.event.pump()
    keyinput = pygame.key.get_pressed()
    if keyinput[pygame.K_ESCAPE] or pygame.event.peek(pygame.QUIT):
        break

    levelSelect[gameStats.getLevel()]()



