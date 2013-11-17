class Mob():
  def __init__(self):
    self.speed = 0
    self.health = 0
    self.damageToBase = 0
  
  
  #GET AND SET METHORDS
  def setSpeed(self, newSpeed):
    self.speed= newSpeed
  def getSpeed(self):
    return self.speed
    
  def setHealth(self, newHealth):
    self.health = newHealth
  def getHealth(self):
    return self.health
    
  def setDamageToBase(self, newDamageToBase):
    self.damageToBase= newDamageToBase
  def getDamageToBase(self):
    return self.DamageToBase

"""
#DERRIVED CLASSES
class Mob_Dwarf(Mob):
  def __init__(self):
    self.speed        = 1
    self.health       = 1
    self.damageToBase = 1

class Mob_Runner(Mob):
  def __init__(self):
    self.speed        = 2
    self.health       = 1
    self.damageToBase = 1
  
"""
