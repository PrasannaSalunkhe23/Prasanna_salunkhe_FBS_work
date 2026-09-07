#3. Create a class shirt with members as sid,sname,type(formal etc.)price and size(small,large)
# add following methods.
#a.constructor(support both paramerterized and parameterless)
#2.Destructor
#3.showbook
#4.for each size od shirt price should be change by 10%.
#(eg. if 1000 is price then small price =1000,medium=1100,large=1200 and xlarge=1300)use static concept

class Shirt:
    #static method
    @staticmethod
    def changePrice(price, size):
        if size=="small":
            return price
        elif size=="medium":
            return price+(price*10/100)
        elif size=="large":
            return price+(price*20/100)
        elif size=="xlarge":
            return price+(price*30/100)
        else:
            return price

    #Constructor
    def __init__(self,sid=0,sname="",type="",price=0,size=""):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=Shirt.changePrice(price,size)
        self.size=size

    # Getter and Setter
    def getSID(self):
        return self.sid
    def setSID(self,NewSID):
        self.sid=NewSID

    def getSName(self):
        return self.sname
    def setSName(self,NewSName):
        self.sname=NewSName

    def getType(self):
        return self.type
    def setType(self,NewType):
        self.type=NewType

    def getPrice(self):
        return self.price
    def setPrice(self,NewPrice):
        self.price=NewPrice

    def getSize(self):
        return self.size
    def setSize(self,NewSize):
        self.size=NewSize

    #showShirt
    def showShirt(self):
        print(f"SID={self.sid}\t Shirt_Name={self.sname}\t Type={self.type}\t Price={self.price}\t Size={self.size}")

    #Destructor
    def __del__(self):
        print('Shirt Object Destroyed')
        
#Parameterized
s1=Shirt(192,"Raymond Shirt","Formal",1200,"small")
s2=Shirt(192,"Raymond Shirt","Formal",1200,"medium")
s3=Shirt(192,"Raymond Shirt","Formal",1200,"large")
s4=Shirt(192,"Raymond Shirt","Formal",1200,"xlarge")
s1.showShirt()
s2.showShirt()
s3.showShirt()
s4.showShirt()
#Parameterless
s5=Shirt()
s5.showShirt()