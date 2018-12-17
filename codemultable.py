#Step 1. Welcome the user
print('welcome to the multiplication table')
#2)Step 2. Print out instructions
print('please enter the number you want to view its multiplication table')
#3)Step 3. Ask the user to enter a value
value= int(input('please enter a number:'))
#4)Step 4. Print out the multiplication table
for i in range(1,13,1):
    print(value, '*', i, '=', value * i)
#5)Step 5. Stop
print('stop')

upper_limit= int(input('please input an upper limit:'))
number_list = []
prime_number_list = []
upper_limit = upper_limit +1
for i in range(2, upper_limit, 1):
    number_list.append(i)
    print(len(number_list))

prime_number= 2

while(len(number_list)>0):
    for i in number_list:
        if(i % prime_number == 0):
            number_list.remove(i)
    print(len(number_list))
    prime_number_list.append(prime_number)
    prime_number = number_list.pop(0)
prime_number_list.append(prime_number)
print(prime_number_list)

            
