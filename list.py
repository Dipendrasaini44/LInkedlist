thislist = ["apple", "banana", "cherry"]
newlist = thislist

print(newlist)

thislist = list(("apple", "banana", "cherry"))

print(thislist)

class Person:

    def __init__(self,fname,lname):
        self.fname= fname
        self.lname= lname

    def printg(self):
        print(self.fname)


class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def print1(self):
        print(self.graduationyear)


e1= Student("Dipendra","saini",1997)

e1.printg()
e1.print1()


# All these objects have a iter() method which is used to get an iterator:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
# print(next(myit))
