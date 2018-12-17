
#print a MAX X MAX multiplication table

MAX = 18

#first, print heading
print(end='    ')
#print column heading numbers
for column in range(1, MAX + 1):
    print(end=' %2i ' % column)
print()     #go down to the  next line

#print table contents
for row in range(1, MAX + 1):
    print(end=' %2i ' % row)
    for column in range(1, MAX + 1):
        product = row*column
        print(end='%3i ' % product)
    print()






m
#print a multiplication table to 10 * 10
#print a column heading
print('      1   2   3   4   5   6   7   8   9   10')
print('  +------------------------------')
#print the 10 rows
for row in range(1,11):
    if row <10:
        print(' ', end='')
    print(row, '| ', end='')
    for column in range(1, 11):
        product = row * column;
        if product < 100:
            print(end=' ')
        if product < 10:
            print(end=' ')
        print(product, end=' ')
    print()

#print a MAX X MAX multiplication table

MAX = 18

#first, print heading
print(end='    ')
#print column heading numbers
for column in range(1, MAX + 1):
    print(end=' %2i ' % column)



print('....................................')
print('This print out number from 1 to the entered one')

n=1
stop=int(input('input the no:'))
while n <= stop:
    print(n)
    n+=1

print('....................................')
print('Indefinite loop')
done = False
while not done:
    entry = eval(input('input the no:'))
    if entry== 999:
        done = True
    else:
        print(entry)
