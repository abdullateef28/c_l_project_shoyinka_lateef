from random import randint

roll_again=''
while(roll_again.lower() !='e') :
    roll_again = input('ready to roll? enter=roll. e=exit')
    if(roll_again.lower() !='e'):
        num_rolled = randint(1,6)
        print('you rrolled a', num_rolled)
    else:
         pass

print('thanks for playing')













from random import randint

roll_again=''
while(roll_again !='e') :
    roll_again = input('ready to roll? enter=roll. e=exit')
    if(roll_again !='e'):
        num_rolled = randint(1,6)
        print('you rrolled a', num_rolled)
    else:
         pass

print('thanks for playing')

