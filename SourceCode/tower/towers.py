import sys
sys.path.append('../')
import map_object

class Tower(map_object.Map_Object):
    def _init_(self):
        self.damage = 0
        self.range = 0
        self.position = [0,0]

#GET AND SET METHODS   
    def setDamage(self, nDamage):
        self.damage = nDamage
    def getDamage(self):
        return self.damage

    def setRange(self, nRange):
        self.range = nRange
    def getRange(self):
        return self.range
