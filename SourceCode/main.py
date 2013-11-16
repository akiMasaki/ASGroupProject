import sys
# Add the folder path to the sys.path list
sys.path.append('/mob/')
sys.path.append('/tower/')
sys.path.append('/game stats/')
sys.path.append('/map/')
from mob import mob
#from mob import mob_dwarf
from gameStats import gameStats

stats = gameStats.GameStats()
dwarf = mob.Mob_Runner()

while True:
    newGameMode = input('Enter Game Mode: ')
    if stats.setGameMode(newGameMode):
        print(stats.getError())
    else:
        break
print(stats.getCash(), stats.getMobDwarfKills())
stats.mobKilled('Dwarf')
print(stats.getCash(), stats.getMobDwarfKills())
