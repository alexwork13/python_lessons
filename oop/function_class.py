import math
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        return (math.sqrt((self.coor2[0]-self.coor1[0])**2 + (self.coor2[1]-self.coor1[1])**2)) 
    
    def slope(self):
        pass


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

dist = li.distance()
print(dist)