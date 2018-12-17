class person:
    def __init__(self):
        print('our class is created')
    def __del__(self):
        print('our class is destroyed')
    def setfullname(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def printfullname(self):
        print(self.firstname,'',self.lastname)

personname=person()
personname.setfullname('programming', 'knowledge')
personname.printfullname()
personname.__del__()


class parent:
    value1= 'this is value 1'
    value2= 'this is value 2'

class child (parent):
    pass

parent_=parent
child_=child

print (parent.value1)
print (parent.value2)

print(child.value1)
print(child.value2)

class parent1:
    value1= 'this is value 1'
    value2= 'this is value 2'

class parent2:
    value3= 'this is value 3'
    value4= 'this is value 4'

class child (parent1, parent2):
    pass

parent_=parent
child_=child

print (parent.value1)
print (parent.value2)

print(child_.value3)
print(child_.value4)
