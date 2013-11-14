

class gameStats():
    # Function that is run initialy setting an mount of lives and cash
    def __init__(self):
        self.lives = 5
        self.cash = 100
        self.gameMode = 1

    def gameMode(self):
        while True:
            self.gameMode=int(input("Set gamemode to 1 or 2"))
            if self.gameMode!=2 or self.gameMode!=1:
                print("Gamemode must be set to 1 or 2")
                continue
            if self.gameMode == 1:
                self.setLives(5)
                self.setCash(100)
            else:
                self.setLives(100)
                self.setCash(300000)
            return self.gameMode
            
    def getCash(self):
        return self.cash
    
    def setCash(self, newCash):
        self.cash = newCash
        
    def getLives(self):
        return self.lives
    
    def setLives(self, newLives):
        self.lives = newLives



gameStats = gameStats()

print(gameStats.getCash())

gameStats.setCash(300000)
print(gameStats.getCash())

print(gameStats.getLives())

gameStats.setLives(100)
print(gameStats.getLives())
