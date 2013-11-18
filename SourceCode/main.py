import pygame
import sys
# Add the folder path to the sys.path list
sys.path.append('mob/')
sys.path.append('tower/')
sys.path.append('gameStats/')
sys.path.append('map/')
# import all the classes
import mob_dwarf
import mob_runner
import tower
import gameStats

from pygame.locals import * # for getting mouse position
    
def playTitle():
    #set up the text
    title1 = defaultFont.render('CLFS', 0, (0,0,0))
    title2 = defaultFont.render('Tower Defence', 0, (0,0,0))
    playText = defaultFont.render('Play', 0, (0,0,0))
    exitText = defaultFont.render('Exit', 0, (0,0,0))

    #get the background image and position
    titleImage = pygame.image.load('images/title_image.jpg')
    titleImage_position = titleImage.get_rect()
    print(titleImage.get_rect())

    #add the text and the images to the screen
    screen.blit(titleImage, titleImage_position)
    screen.blit(title1, (155,50))
    screen.blit(title2, (50,100))
    screen.blit(playText, (285,363))
    screen.blit(exitText, (285,451))

    #iterate though the list of events to see what is triggered
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # if the mouse has been pressed see where it has been pressed and if that means a button has been clicked
        # mousePos[0] is the x axis and mousePos[1] is the y axis
        elif event.type == MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if (mousePos[0] >= 257 and  mousePos[0] <= 428) and (mousePos[1] >= 348 and  mousePos[1] <= 421):
                gameStats.setLevel('MapSelect')
            if (mousePos[0] >= 257 and  mousePos[0] <= 428) and (mousePos[1] >= 436 and  mousePos[1] <= 509):
                pygame.quit()
            
    pygame.display.flip()

def playMapSelect():
    #create a blue background (will be cahnged into the map when i get it!)
    background = pygame.Surface(screen.get_size())
    background.fill((140,206,250))
    screen.blit(background, (0,0))

    # if the mouse has been pressed see where it has been pressed and if that means a button has been clicked
    # mousePos[0] is the x axis and mousePos[1] is the y axis
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            mapObjects['Mobs'].append(mob_dwarf.Mob_Dwarf())
            for o in mapObjects['Mobs']:
                print(o.getImagePath())
                dwarfImage = pygame.image.load(o.getImagePath())
                screen.blit(dwarfImage, mousePos)
            
    pygame.display.flip()

#MAIN

#dictionary to hold the map objects e.g. all the towers and mobs
mapObjects = {'Mobs':[],'Towers':[]}
    
# dictionary to hold the fuction for different levels
levelSelect = {'Title':playTitle, 'MapSelect':playMapSelect}

#instantiate the gameStats
gameStats = gameStats.GameStats()
gameStats.setLevel('Title')

pygame.init()
#create a screen of 720x670 with title and set default font for text
screen = pygame.display.set_mode((720,670))
pygame.display.set_caption('CLFS Tower Defence')
defaultFont = pygame.font.Font('fonts/miriamfixed.ttf', 48 )


# MAIN GAME LOOP
while gameStats.getLevel()!=None:
    pygame.event.pump()
    keyinput = pygame.key.get_pressed()
    #does user want to quit?
    if keyinput[pygame.K_ESCAPE] or pygame.event.peek(pygame.QUIT):
        break
    #use the level select top call the right fuction to display correct level
    levelSelect[gameStats.getLevel()]()



