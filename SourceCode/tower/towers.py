import sys
sys.path.append('../')
import map_object

class Tower(map_object.Map_Object):
    def _init_(self):
        self.damage = 0
        self.Range = 0
        self.updateTower = {damage: 0, Range: 0}

#GET AND SET METHODS   
    def setDamage(self, nDamage):
        self.damage = nDamage
    def getDamage(self):
        return self.damage

    def setRange(self, nRange):
        self.Range = nRange
    def getRange(self):
        return self.Range
        
    def towerUpdate(self):
        nRamage = self.damage*1.25
        nRange  = self.Range*1.2
