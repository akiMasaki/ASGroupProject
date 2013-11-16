#TRIAL MAP FILES JUST TEST'S BEFORE GUI INTERFACE IS DECIDED

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
    def getMap (self):
        return self.currentMap
        
    def updateMap (self,coordinates,changeValue):
        #cordinates get changed to location in array
        split=list(str(coordinates))
        verticalCoordinate=ord(split[0])-65
        horizontalCoordinate=int(split[1])-1
        #Updating the map instance to the new value
        mapUpdateP1=self.currentMap
        mapUpdateP2=mapUpdateP1[verticalCordinate]
        mapUpdateP2[horizontalCoridinate]=ChangeValue






















        
