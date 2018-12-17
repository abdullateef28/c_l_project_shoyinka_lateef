print("This will help you know if a string entered is 5 in lenth or not")

string=str(input("write a letter:"))
if len(string)>5:
    print("the length of the string is more than 5")
elif len(string)<5:
    print("the length of the string is less than 5")
else:
    print ("the length of the string is 5, good!")

print("This will help you determine if a number is even or odd")

x=int(input("input a number:"))
if x % 2!=0 :
    print(x, "is odd")
else:
    print (x, "is even")

print("This will help you determine if a year is a leap year")
t=int(input("input a year:"))
if t % 4==0:
    print(t, "is a leap year")
else:
    print(t, "is not a leap year")

print ("Thank you")

input ("enter 0 to exit")
