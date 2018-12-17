#Print out the purpose of the program
print('this is a program for a menu based system')
#2)Print out the instructions
print('select a number for the options in the menu')
#3)Display the options
#4)Ask the user to make a choice
menu=input('please select an option\n (1)option 1\n (2) option 2\n')
#5)Print out the user’s choice
if (menu=='1'):
    print('option 1')
elif (menu=='2'):
    print('option 2')

else:
        print('invalid choice')

#Display the purpose of the program
print('welcome to the BMI calculator')
#2)Display the instructions to the user
print('please enter your weight in kilogram and height in metre')
#3)Prompt the user to enter their weight
weight=float(input('please enter your weight'))
#4)Prompt the user to enter their height
height=float(input('please enter your height'))
#5)Calculate the BMI of the user
bmi=weight/height*height
#6)Round up the BMI to 1 decimal place
bmi= round(bmi, 1)
#7)Display the BMI
print('your BMI is',bmi)
#8)Evaluate the BMI and give a verdict
if bmi<18.5:
    print('underweight')
elif bmi>=18.5 and bmi<25:
    print('normal')
elif bmi>=25 and bmi<30:
    print('overweight')
else:
    print('obese')
