import mob
class Mob_Runner(Mob):
    def __init__(self):
        self.damage         = 1
        self.speed          = 1
        self.health         = 1
        self.damageToBase   = 1

dwarf2=Mob_Runner()
print(dwarf1.getHealth())
