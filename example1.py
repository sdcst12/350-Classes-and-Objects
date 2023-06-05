#!python3

# Basic Class Object


class example:
    x = 0
    y = 0

    def __init__(self,x=3,y=4):
        self.x = x
        self.y = y

    
    def __del__(self):
        print("Thank you for playing")

    def add(self):
        # adds the two numbers and returns the value
        return self.x + self.y
    
    def set(self,prop,value):
        if prop == "x":
            self.x = value
        elif prop == "y":
            self.y == value


app = example()
print( app.x , app.y , app.add() )

input("press Enter to run the next section of code")
app.set("x",10)
print( app.x , app.y , app.add() )

