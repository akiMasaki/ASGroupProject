#class to define what all objects that will be placed on the map will have
class Map_Object():
    def __init__(self):
        self.position = [None,None]
        self.imagePath = None
        
    def getPosition(self):
        return self.position
    
    def getImagePath(self):
        return self.imagePath
    def setImagePath(self,newPath):
        self.imagePath = newPath
        
