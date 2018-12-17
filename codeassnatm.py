print('A basic simulation of ATM machine')

print('The ATM card pin is 1234')

card=int(input('please enter your secret code:'))
if card==1234:
    print('what do you like to do?')

    menu=input('(1)inquiry\n (2)withdrawal\n (3)buy airtime\n (4) pay bills\n (5) transfer money\n')
    if menu=='1':
        print ('inquiry')
        print('your account balance is:\n #100,000.\n')
        print('Thank you for banking with us')
    elif menu=='2':
        print('withdrawal')
        amount=input('please enter an amount in digit of thousand')
        print(amount, 'withdrawn')
        print('Thank you for banking with us')
    elif menu=='3':
        input('Enter the phone number:')
        print('Transaction succesful')
    elif menu=='4':
        input('Enter your bill number')
        print('Transaction succesful')
    elif menu=='5':
        input('Input the account number')
        input('Input the amount')
        print('Transaction succesful')
        

else:
    print('invalid pin')

input('enter any key to exit')
