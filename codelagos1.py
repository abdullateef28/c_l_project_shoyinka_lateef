#Print out the purpose of the program
print("this is a program to find the highest common factor of two numbers")
#Print out the instructions

print("please enter the whole numbers")
#Ask the user to enter a first number

first_number = int(input("enter the first no"))
#Ask the user to enter a second number

second_number = int(input("enter the second no"))
#If the second number is greater than the first number, swap the two numbers
if(second_number>first_number):
	temp=first_number
	first_number=second_number
	second_number=temp
	print (second_number, first_number)

high_number= first_number
low_number=second_number
#Find the quotient and remainder of the first number in terms of the second number
#Assign the quotient to the number and the remainder to the second number
#If the remainder is 0, stop

while(second_number > 0):
        qoutient=first_number// second_number
        remainder= first_number% second_number
        first_number= second_number
        second_number = remainder

print('the hcf of', high_number, 'and', low_number, 'is', first_number)
