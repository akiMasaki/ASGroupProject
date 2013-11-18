import time
class GameStats():
    # Function that is run initialy setting variables
    def __init__(self):
        self.health = 5
        self.cash = 100
        self.gameMode = 1
        self.currentTime = 0
        self.startTime = time.time()
        self.error = ''
        # killCash is a dictionary so self.killCash('Dwarf') returns 1
        self.killCash = {'Dwarf': 1, 'Runner': 2}
        self.towerCost = {'Tower1': 1, 'Tower2': 2}
        self.mobKills  = {'Dwarf':0,'Runner':0}
        self.level = None
        self.update()

    def setGameMode(self, mode):
        try:
            mode = int(mode)
        except ValueError:
            self.error='Not a valid Number'
            return True
        if mode!=2 and mode!=1:
            self.error = "Gamemode must be set to 1 or 2"
            return True
        if mode == 1:
            self.gameMode = 1
            self.setHealth(5)
            self.setCash(100)
            self.error = ''
        else:
            self.gameMode = 2
            self.setHealth(100)
            self.setCash(300000)
            self.error = ''
        return False
    def getGameMode(self):
        return self.gameMode
    
    def getCash(self):
        return self.cash
    def setCash(self, newCash):
        self.cash = newCash
        
    def getHealth(self):
        return self.health
    def setHealth(self, newHealth):
        self.health = newHealth

    def getLevel(self):
        return self.level
    def setLevel(self, newLevel):
        self.level = newLevel

    def getError(self):
        return self.error

    def getTime(self):
        return self.currentTime
    
    def getMobDwarfKills(self):
        return self.mobDwarfKills
    
    def update(self):
        self.currentTime=time.time() - self.startTime
    
    def mobKilled(self, mobType):
        self.cashDrop(self.killCash[mobType])
        if mobType == 'Dwarf':
            self.mobDwarfKills = self.mobDwarfKills + 1
        if mobType == 'Runner':
            self.mobRunnerKills = self.mobRunnerKills + 1

    def cashDrop(self, cashToAdd):
        self.cash = self.cash + cashToAdd
    
    def towerBought(self, towerType):
        self.cashSpent(self.towerCost[towerType])

    def cashSpent(self, cashToDeduct):
        self.cash = self.cash - cashToDeduct
        

"""
    fuction to output mob kills into a file to read in next round
    and add variable to hold toatal mob kills so at end of round:
    number in the file for dwarfs = number in the file for dwarfs + mobDwarfKills
"""
         
