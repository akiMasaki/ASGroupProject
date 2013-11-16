import pygame
import sys
# Add the folder path to the sys.path list
sys.path.append('/mob/')
sys.path.append('/tower/')
sys.path.append('/game stats/')
sys.path.append('/map/')
from mob import mob
from gameStats import gameStats

stats = gameStats.GameStats()
dwarf = mob.Mob_Dwarf()

def main():
# SETTING UP THE GAME AREA
    pygame.init()	
    screen = pygame.display.set_mode( (720,670) )
    background = pygame.Surface( screen.get_size() )
    background.fill(142,206,250)
    titleImage = pygame.image.load( "images/title.jpeg" )
    titleImage_position = image.get_rect()
    titleImage_position.bottom = 240
    titleImage_position.left = 200
    screen.blit(background,(0,0))
    screen.blit(image, titleImage_position)
    pygame.display.flip()

# MAIN GAME LOOP
    while True:
        pygame.event.pump()
        keyinput = pygame.key.get_pressed()
        if keyinput[pygame.K_ESCAPE] or pygame.event.peek( pygame.QUIT ):
            break
        screen.blit( background, (0,0) )
        screen.blit( image, titleImage_position )
        pygame.display.flip()

if __name__ == '__main__': main()


"""
#FUNCTION TESTING

while True:
    newGameMode = input('Enter Game Mode: ')
    if stats.setGameMode(newGameMode):
        print(stats.getError())
    else:
        break
print(stats.getCash(), stats.getMobDwarfKills())
stats.mobKilled('Dwarf')
print(stats.getCash(), stats.getMobDwarfKills())
"""
