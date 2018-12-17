# print the purpose of the program
print('This program will help you to convert your time in seconds to hours, minutes and seconds which will be display in written  and digital form')

#input the value in seconds to convert to hours, minutes and seconds
seconds=eval(input('please enter the seconds:'))

#convert the seconds to hour
hour=seconds//3600 #3600 makes one hour

#compute the remaining seconds after hours have been accounted for, less the initial value will continue to be run.
seconds= seconds % 3600

#convert the reamaining seconds to minutes
minutes=seconds//60

#compute the remaining seconds after the minutes has been accounted for
seconds= seconds % 60

#print out the result
print(hour, 'hr', minutes, 'mins', seconds, 'sec')

print('--------------------------------------------------------------')
print('The time will be brought in digital form')

input('please press enter to continue')

#To print out the result in digital form
print(hour, ':', sep='', end='')

#compute the tens result of digits
tens= minutes // 10

#compute the ones digit of minute
ones= minutes % 10

print(tens, ones, ':', sep='', end='')

#compute the tens digit of seconds
tens= seconds // 10

#compute the ones digit of seconds
ones= seconds % 10

print(tens, ones, sep='')

#input code to ensure proper command for exit
EXIT = 'E'
E= str(input(' please enter e to exit this program'))
if E== 'e':
    print('Thank you')
    input('press enter')
    
else:
    print('Invalid input!!!')
    E= str(input(' please enter e to exit this program'))
    if E== 'e':
        print('Thank you')
        input('press enter')

    else:
        print('Invalid input!!!')
        E= str(input(' please enter e to exit this program'))
        if E== 'e':
            print('Thank you')
            input('press enter')

        else:
            print('Invalid input!!!')
            E= str(input(' please enter e to exit this program'))
            if E== 'e':
                print('Thank you')
                input('press enter')

            else:
                print('Invalid input!!!')
                E= str(input(' please enter e to exit this program'))
                if E== 'e':
                    print('Thank you')
                    input('press enter')
