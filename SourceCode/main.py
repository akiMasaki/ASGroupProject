import sys
# Add the folder path to the sys.path list
sys.path.append('/mob/')
sys.path.append('/tower/')
sys.path.append('/game stats/')
sys.path.append('/map/')
#from mob import mob_dwarf
#from mob_dwarf import Mob_Dwarf
from gameStats import gameStats

stats = gameStats.GameStats()
#dwarf = mob_dwarf.Mob_Dwarf()

#not working atm
while True:
    newGameMode = input('Enter Game Mode: ')
    try:
        newGameMode = int(newGameMode)
    except ValueError:
        print('Not a valid Number')
        continue
    
    if stats.setGameMode(newGameMode):
        print(stats.getError())
    else:
        break
