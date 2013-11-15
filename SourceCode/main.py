import sys
# Add the folder path to the sys.path list
sys.path.append('/mob/')
sys.path.append('/tower/')
sys.path.append('/game stats/')
sys.path.append('/map/')
from mob import *
from gameStats import gameStats
#from tower import towers

stats = gameStats.GameStats()
dwarf = mob_dwarf.Mob_Dwarf()




print(dwarf.getHealth())


print(stats.getError())
if stats.setGameMode(3):
    pass
print(stats.getError())

