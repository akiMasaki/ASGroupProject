import sys
sys.path.append('../')
import map_object

class Mob(map_object.Map_Object):
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

