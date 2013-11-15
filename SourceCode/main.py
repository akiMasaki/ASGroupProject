import sys
# Add the folder path to the sys.path list
sys.path.append('/mob/')
sys.path.append('/tower/')
sys.path.append('/game stats/')
sys.path.append('/map/')
<<<<<<< HEAD
#from mob import mob_dwarf
=======
from mob import *
from mob_dwarf import Mob_Dwarf
from gameStats import gameStats
>>>>>>> a2816a57db893876738b76b3cae7dbacfc397d7e
#from tower import towers
from gameStats import gameStats

<<<<<<< HEAD
<<<<<<< HEAD
stats = gameStats.GameStats()
#dwarf = mob_dwarf.Mob_Dwarf()



=======
stats = gameStats.GameStats
dwarf = mob_dwarf.Mob_Dwarf
>>>>>>> a2816a57db893876738b76b3cae7dbacfc397d7e
=======
stats = gameStats.GameStats
dwarf = mob_dwarf.Mob_Dwarf
>>>>>>> a34f9a5acaf1fdc764db98e4173a037832b93e32

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
    


GameStats = GameStats()

print(GameStats.getCash())

GameStats.setCash(300000)
print(GameStats.getCash())

print(GameStats.getHealth())

GameStats.setHealth(100)
print(GameStats.getHealth())
