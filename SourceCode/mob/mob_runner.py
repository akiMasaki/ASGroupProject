import mob
class Mob_Runner(mob.Mob):
  def __init__(self):
    self.damage       = 1
    self.speed        = 1
    self.health       = 1
    self.damageToBase = 1
  
dwarf1 = Mob_Runner()
print(dwarf1.getHealth())
