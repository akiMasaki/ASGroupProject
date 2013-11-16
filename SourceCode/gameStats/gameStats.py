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
        self.mobRKill #Variables need to be looked at by mob team
        self.mobDKill
        self.update()

    def setGameMode(self, mode):
        if mode!=2 or mode!=1:
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

    def getError(self):
        return self.error

    def getTime(self):
        return self.currentTime
    
    def update(self):
        self.currentTime=time.time() - self.startTime
    
    def kill(self):
        if (self.mobDKillC==self.mobDKill + 1):
            self.cashDrop(25)
            self.mobDKillC=self.mobDKill
        if (self.mobRKillC==self.mobRKill + 1):
            self.cashDrop(30)
            self.mobRKillC=self.mobRKill

    def cashDrop(self, cashToAdd):
        self.cash = self.cash + cashToAdd
