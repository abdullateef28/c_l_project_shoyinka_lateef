dividend, divisor= eval(input('please input two numbers:'))
print(dividend, '/', divisor, '=', dividend/divisor)

#input the value in seconds to convert to hours, minutes and seconds
seconds=eval(input('please enter the seconds:'))

#convert the seconds to hour
hour=seconds//3600 #3600 makes one hour

#compute the remaining seconds after hours have been accounted for less the initial value will continue to be run.
seconds= seconds % 3600

#convert the reamaining seconds to minutes
minutes=seconds//60

#compute the remaining seconds after the minutes has been accounted for
seconds= seconds % 60

#print out the result
print(hour, 'hr', minutes, 'mins', seconds, 'sec')

print('--------------------------------------------------------------')
print('the time will be brought in digital form')
#input the value in seconds to convert to hours, minutes and seconds
seconds=eval(input('please enter the seconds:'))

#convert the seconds to hour
hour=seconds//3600 #3600 makes one hour

#compute the remaining seconds after hours have been accounted for less the initial value will continue to be run.
seconds= seconds % 3600

#convert the reamaining seconds to minutes
minutes=seconds//60

#compute the remaining seconds after the minutes has been accounted for
seconds= seconds % 60

#print out the result
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

print('........................................')
a= str(input('put an integer for a'))
b= 'shoyinka'
print(a,b ,sep=':')

print('..............................................')
print(3,  5,  'string', 10, sep='')
print(3,  5,  'string', 10, sep=':')

