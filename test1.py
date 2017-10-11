class parent:

    def __init__(self,x):
        self.x=x
        self.identity()

    def identity(self):
        print("this is parent")

    def age(self):
        print(self.x)

class child(parent):

    def __init__(self,x):
        #parent.__init__(self,x)
        self.x=x+1
        self.identity()
        print("hi")

    def identity(self):
        print("this is child")
Mary=parent(35)
Tom=child(3)
