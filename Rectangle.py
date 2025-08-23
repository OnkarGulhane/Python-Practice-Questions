class Rectangle:
    # def __init__(self,l,w):
    #     self.__length = l
    #     self.__width = w


    def setLength(self,l):
        self.__length = l

    def setWidth(self,w):
        self.__width = w

    def getLength(self):
        return set.__length

    def getWidth(self): 
        return set.__width  
    def Calculate(self):
        self.__a = self.__length *self.__width
        print('Area of Rectangle is:',self.__a)    

r = Rectangle()
a = float(input('Enter Length of Rectangle:'))
b = float(input('Enter width of Rectangle:'))
r .setLength(a)
r.setWidth(b)
r.Calculate()