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

    def gameMode(self):
        if self.gameMode!=2 or self.gameMode!=1:
            self.error = "Gamemode must be set to 1 or 2"
            return 0
        if self.gameMode == 1:
            self.setHealth(5)
            self.setCash(100)
        else:
            self.setHealth(100)
            self.setCash(300000)
        return 1
        
    def getCash(self):
        return self.cash
    def setCash(self, newCash):
        self.cash = newCash
        
    def getHealth(self):
        return self.health
    def setHealth(self, newHealth):
        self.health = newHealth

    def getError(self):
        return self.error

    def currentTime():
        currentTime=time.time() - self.startTime
        return CurrentTime

    
#ALL BELOW NEED TO BE IN A DEBUGGING FUNCTION IN FUTURE


GameStats = GameStats()

print(GameStats.getCash())

GameStats.setCash(300000)
print(GameStats.getCash())

print(GameStats.getHealth())

GameStats.setHealth(100)
print(GameStats.getHealth())
