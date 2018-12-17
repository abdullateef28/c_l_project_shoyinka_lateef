x=eval(input('input x:'))
if x<10:
    y=x
    print('y is', y)

print('to print a digit form of a division')
num= eval(input('please enter an int in the range of 0-9999'))
if (num < 0):  #the bracket is not important
    num= 0
if (num > 9999):
    num= 9999

print(end='[') #end='')
#to print the thousand digit
digit= num//1000
print(digit, end='')
num=num % 1000  #so as to get the hunderth value[ num%=1000]
          
#to print the hundreth digit
digit= num//100
print(digit, end='')
num=num % 100  #so as to get the tenth value

#to print the tenth digit
digit= num//10
print(digit, end='')
num=num % 10  #so as to get the one value

print(num, ']')         

n=int(input("number?"))
if n<0:
    print("the absolute value of" ,n, "is", -n)
    print("the absolute value of" ,n, "is", -n)
    print("the absolute value of" ,n, "is", -n)
else:
    print( "the absolute value of",n, "is", n)

sumoftwo=50+50
print(sumoftwo)


name=input("name?")
if name=="lateef":
    print("the name entered is", name)
elif name=="toyeeb":
    print("the name entered is", name)
else:
    print ("the name entred is not valid")
if name=="ismail":
    print("the first son of the family")
if name=="azeez":
    print("the first son of his mother")
if name=="habeeb":
    print("the first son of his mother")
else:
    print("the name entered doesn't belong to the family")

name=input("name?")
if name=="dog":
    print("name entered is animal")
    print("name is valid")
elif name=="cat":
    print("name entered is animal")
    print("name is valid")
elif name=="rat":
    print("name entered is animal")
    print("name is valid")
x=10
if x!=100:
    print ('x is',x)
if x >0:
    print('x is positive')

