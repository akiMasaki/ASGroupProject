#Map Files
class Map () :
    def __init__ (self):
        self.map=[]

    def setMap (self):
        newMap=[]
        for n in range (0,10):
            newMap.append([])
        for c in newMap :
            for n in range(0,10):
                c.append(0)
        self.map=newMap
    def returnMap (self):
        return self.map






















        
