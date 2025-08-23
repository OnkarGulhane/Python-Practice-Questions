import math

class Point:
    def accept(self):
        self.x = float(input('Enter x-coordinate: '))
        self.y = float(input('Enter y coordinate:' ))
    def display(self):
        print('(',self.x,',',self.y,')') 

    @staticmethod
    def distance(p1,p2):
        d = math.sqrt((math.pow(p2.x-p1.x,2))  +(math.pow(p2.y-p1.y,2)) )
        print('Distance:',d)

p1 = Point()
print('Enter First point:')
p1.accept()        
print('Enter Second Point:')
p2 = Point()
p2.accept()

print('Both Points: ')
p1.display()
p2.display()

Point.distance(p1,p2)
