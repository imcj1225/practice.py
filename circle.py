import math

class Circle:
    r = 0

    def __init__(self, r):
        self.r = r

    def set_r (self, r):
        self.r = r
    
    def get_v (self):
        print(math.pi * self.r ** 2)
       
    def get_c (self):
        print (2 * math.pi * self.r)


c = Circle(10)
c.get_v()
c.get_c()

c.set_r(20)
c.get_c()
