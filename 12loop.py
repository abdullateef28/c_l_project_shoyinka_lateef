a=1
s=0
print ('enter numbers to add to the sum')
print ('enter 0 to quit')
while a!= 0:
    print ('current sum:', s)
    a= float(input('number?'))
    a= float(a)
    s+=a
print ('total sum = ', s)

b=[1,2,3,4,5,6,7,8,9,0]
for num in b:
    print(num)
