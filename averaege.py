print('welcome to the averaege calculator')
print('this is a program the average of 3 numbers')

first_number= float(input('please enter the first number:'))
second_number= float(input('please enter the second number:'))
third_number= float(input('please enter the third number:'))

def get_runnin_total(first_number, second_number, third_number):
    return (first_number +second_number + third_number)

runnin_total =get_runnin_total(first_number, second_number, third_number )
average = runnin_total / 3
print('the averaege of', first_number, second_number, third_number, 'is', average)
