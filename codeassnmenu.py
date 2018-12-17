print('This is a simple area calculator program')

shapes=input('Choose the shapes you intend to find an area for\n (a) Triangle\n (b)Square\n (c) Rectangle\n')
if shapes=='a':
    print('Triangle')
    base = float(input('input the base of the triangle?'))
    height = float(input('input the height of the triangle?'))
    area= 0.5 * base * height
    round(area,2)
    print('The area of the Triangle is', area)
elif shapes=='b':
    print('Square')
    length = float(input('input the length of the square?'))
    area= length * length
    round(area,2)
    print('The area of the square is', area)
elif shapes=='c':
    print('Rectangle')
    length = float(input('input the lenght of the rectangle ?'))
    bredth = float(input('input the bredth of the rectangle ?'))
    area= length * bredth
    round(area,2)
    print('The area of the rectangle is', area)
else:
    print('Invalid choice!')

input('please press any key to exit')
