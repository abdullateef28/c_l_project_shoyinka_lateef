print("this is a program to find hcf of two numbers")
x=int(input("enter the first no"))
y=int(input("enter the second no"))

while(y):
    x,y = y, x%y

    

print("the hcf is:")

print (x)

