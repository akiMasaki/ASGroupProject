import sys
# Add the folder path to the sys.path list
sys.path.append('/mob/')
sys.path.append('/tower/')
sys.path.append('/game stats/')
sys.path.append('/map/')
from mob import mob_dwarf
from gameStats import gameStats
from towers import towers

stats = gameStats.GameStats()
print(stats.getError())
if stats.setGameMode(3):
    pass
print(stats.getError())

