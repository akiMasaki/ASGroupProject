class Towers():
    def _init_(self):
        self.damage = 0
        self.range = 0
        self.cost = 0
        
    def setDamage(self, nDamage):
        self.damage = nDamage
    def getDamage(self):
        return self.damage

    def setRange(self, nRange):
        self.range = nRange
    def getRange(self):
        return self.range
    
    def setCost(self, nCost):
        self.cost = nCost
    def getCost(self):
        return self.cost

