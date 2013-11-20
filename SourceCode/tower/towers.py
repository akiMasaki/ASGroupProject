import sys
sys.path.append('../')
import map_object

class Tower(map_object.Map_Object):
    def _init_(self):
        self.dmg = 0
        self.rng = 0
        self.numbUpdates{'Damage':0,'Range':0}

#GET AND SET METHODS   
    def setDamage(self, nDamage):
        self.dmg = nDamage
    def getDamage(self):
        return self.dmg

    def setRange(self, nRange):
        self.rng = nRange
    def getRange(self):
        return self.rng

    def upgradeRange(self):
        self.rng = self.rng*1.5
    def upgradeDamage(self):
        self.dmg = self.dmg*1.25
