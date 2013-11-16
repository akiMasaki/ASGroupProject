#Map Files
class Map () :
    def __init__ (self):
        self.currentMap=[]

    def newMap (self):
        newMap=[]
        for n in range (0,10):
            newMap.append([])
        for c in newMap :
            for n in range(0,5):
                c.append(0)
        self.currentMap=newMap
    def returnMap (self):
        return self.currentMap
        
    def updateMap (self,Cordintes,ChangeValue):
        #cordinates get changed to location in array
        split=list(str(Cordintes))
        verticalCordinate=ord(split[0])-64
        horizontalCoridinate=int(split[1])
        #Updating the map instance to the new value
        mapUpdateP1=self.currentMap
        mapUpdateP2=mapUpdateP1[VerticalCordinate]
        MapupdateP2[horizontalCordiante]=ChangeValue
        
        






















        
