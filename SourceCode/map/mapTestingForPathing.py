#TRIAL MAP FILES JUST TEST'S BEFORE GUI INTERFACE IS DECIDED

class Map () :
    def __init__ (self):
        self.currentMap=[]
        self.path=[]

    def newMap (self):
        newMap=[]
        for n in range (0,10):
            newMap.append([])
        for c in newMap :
            for n in range(0,5):
                c.append(0)

        Starter=newMap[0]
        Ender=newMap[9]
        #THIS SLOT SHOULD NOT BE CHANGED
        Starter[2]=2
        Ender[2]=3
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

    def ReturnMap (self, coorinates):
        
        verticalCoordinate=coorinates[0]
        horizontalCoordinate=coorinates[1]

        mapReadP1=self.currentMap
        mapReadP2=mapReadP1[verticalCoordinate]
        Value=mapReadP2[horizontalCoordinate]
        return Value
        

    def printMap (self):
        print (self.currentMap)


    def returnPath(self):
        currentMap=self.currentMap
        currentCooridnate=[0,2]
        self.path=[[0,2]]
        x=True

        while x==True :
            while True:
                loopCheck=True
                currentCooridnate[0]=currentCooridnate[0]+1
                
                if self.ReturnMap(currentCooridnate)==3:
                    x=False
                    break
                
                if self.ReturnMap(currentCooridnate)==2 or self.ReturnMap(currentCooridnate)==0:
                    self.path.append(currentCooridnate)
                    break

                currentCooridnate[0]=currentCooridnate[0]-1
                currentCooridnate[1]=currentCooridnate[1]+1

                if Map.ReturnMap(currentCooridnate)==3:
                    x=False
                    break
                
                if self.ReturnMap(currentCooridnate)==2 or self.ReturnMap(currentCooridnate)==0:
                    self.path.append(currentCooridnate)
                    break

                currentCooridnate[1]=currentCooridnate[1]-2

                if self.ReturnMap(currentCooridnate)==3:
                    x=False
                    break
                
                if self.ReturnMap(currentCooridnate)==2 or self.ReturnMap(currentCooridnate)==0:
                    self.path.append(currentCooridnate)
                    break
                
                
                currentCooridnate[0]=currentCooridnate[0]-1
                currentCooridnate[1]=currentCooridnate[1]+2

                if ReturnMap(currentCooridnate)==3:
                    x=False
                    break
                
                if self.ReturnMap(currentCooridnate)==2 or self.ReturnMap(currentCooridnate)==0:
                    self.path.append(currentCooridnate)
                    break
        return self.path
            
                    
            
        

TestMap=Map()

TestMap.newMap()

TestMap.printMap()

print(TestMap.returnPath())






















        
