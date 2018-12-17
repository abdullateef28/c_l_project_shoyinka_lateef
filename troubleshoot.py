print('Help! My computer doesn\'t work!')
print('Does the computer make any sounds(fans, etc.)')
choice= input("or show any lights?(y/n):")
if choice == 'n': #the computer has no power
    choice = input('is it plugged in? (y/n):')
    if choice == 'n': #it is not pluged in
        print('plug it in. if the problem persists,')
        print('please run this program again')
    else:  #it is plugged in
        choice = input('is the switch in the \'on\' position? (y/n):')
        if choice == 'n':
            print('Turn it on. If the problem persists,')
            print('please run this program again.')
        else: #the switch is on
            choice = input ('Does the computer has a fuse? (y/n)')
            if choice == 'n':  #no fuse
                choice == input('Is the outlet okay?(y/n):')
                if choice == 'n':  #no fuse
                    print('check the outlet\'s circuit')
                    print('breaker or fuse. Move to a')
                    print('new outlet, if necessary.')
                    print('If the problem persists, ')
                    print('please run this program again.')
                else:   # beats me!
                    print('Please consult a service technician.')
            else:   #check fuse
                print('Check the fuse. Replace if ')
                print('necessary. If the problem ')
                print('persists, then ')
                print('please run this program again.')
else:   #the computer has power
    print('please consult a service technician.')
    
