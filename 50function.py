#to define a function, use def
 #def nameoffunction (arg1, ar2, ar3...)
 #print the command
    #functions help you to easily repeat a procedure you will be using

def sum(arg1, arg2):
    if type(arg1) != type(arg2):
         print('please give the args of same type')
         return
    return (arg1 + arg2)

a= sum(15, 60)
print(a)
print(sum('hello ', 'world'))
print(sum(23.44, 35.55))
print(sum('hello', 15))

#default argguments
def student(name='unknown name', age=0):
    print('name:', name)
    print('age', age)
    
student('tom', 22)

def student(name, age, **marks):  # * is used to input multiples value for the score
    print('name:', name)    # ** is used to allow the addition of key values, and the values will be printed in form of a dictionary
    print('age', age)
    print('marks', marks)
    #for x in marks:
    for key, value in marks.items():
        print(key, '', value)
student('tom', 22, english=78, math=90, chemistry=69, physics=88)
#in dictionary, anythin before the colon is a key and anythin after it is a value
# D.items is used for listin 
