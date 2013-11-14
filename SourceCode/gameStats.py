class gameStats():
    def __init__(self):
        self.lives = 5
        self.cash = 100
    def getCash(self):
        return self.cash
    
    def setCash(self, newCash):
        self.cash = newCash

gameStats = gameStats()

print(gameStats.getCash())
gameStats.setCash(300000)
print(gameStats.getCash())

