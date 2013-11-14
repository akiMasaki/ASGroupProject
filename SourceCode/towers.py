class towers():
    def _init_(self):
        self.damage = 5
        self.range = 10
        self.cost = 15
        
    def towerDamage(self):
        return self.damage

    def towerCost(self, newCost):
        self.cost = newCost

    tower = towers()

    print(tower.towerDamage())
