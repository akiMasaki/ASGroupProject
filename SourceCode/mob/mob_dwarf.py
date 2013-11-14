import mob
class Mob_Dwarf(mob):
  def __init__(self):
    self.damage       = 1
    self.speed        = 1
    self.health       = 1
    self.damageToBase = 1
  
dwarf1 = Mob_Dwarf()
print(dwarf1.getHealth())
