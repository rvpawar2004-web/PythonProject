#hybride inheritance
class AB: # base class / parent class
    def displayA(self):
        print("class AB is call")

class DM(AB): # derived  base class / child  parent class
    pass

class BM(DM): # derived base class / child parent class
    def displayB(self):
        print("Class BM is call")



z=DM()
z.displayA()


z1=BM()
z1.displayB()
z1.displayA()
