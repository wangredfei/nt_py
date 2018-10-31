class Mynub():
    def __init__(self,v):
        self.v = v 
    def __repr__(self):
        return 'Mynub(%s)'%self.v
    def __sub__(self,value):
        return Mynub(self.v - value.v)
h1 = Mynub(100)
h2 = Mynub(200)
print(h1,"-",h2,"=",h1-h2)
