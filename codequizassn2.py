print('The is a simple 5 questions quiz')

print('Read the question very well before choosing an option')
print('Be careful! wrong answer attract loss loss of 5 marks')
score=0
wrong=0

input('please press 1 to load the first question:')
if input==1

qst1= input('Who creates all things?\n (a) Allah\n (b) Muhammad\n (c) Jesus\n')
if qst1=='a':
    print('correct')
    score=score+10
else:
    print('you are wrong')
    wrong=wrong-5

input('please press 2 to load the second question:')

qst2=input('Who is the first man created?\n (a) Jubril\n (b) Eve\n (c) Adam\n')
if qst2==('c'):
    print('correct')
    score=score+10
else:
    print('you are wrong')
    wrong=wrong-5
input('please press 3 to load the third question:')

qst3=input('Where is Dubai found?\n (a) Quwait\n (b) UAE\n (c) France\n')
if qst3==('b'):
    print('correct')
    score=score+10
else:
    print('you are wrong')
    wrong=wrong-5
    
input('please press 4 to load the fourth question:')

qst4=input("The university known as the first choice and nations' pride of Nigeria is? \n (a)UNIPORT\n (b) UNIZIK\n (c) UNILAG\n") 
if qst4==('c'):
    print('correct')
    score=score+10
else:
    print('you are wrong')
    wrong=wrong-5
input('please press 5 to load the last question:')

qst5=input('Who is the President of Turkey?\n (a) Erdogan\n (b)Abdul-Salam Aziz\n (c) John Kless\n')
if qst5==('a'):
    print('correct')
    score=score+10
else:
    print('you are wrong')
    wrong=wrong-5

print('you scored',score + wrong, 'of 50')

print('Thank you')

input('please press enter to qiut')
