
>>> print("hello lateef")
hello lateef
>>> def hello(name):
	printhello lateef
	
SyntaxError: invalid syntax
>>> hello lateef
SyntaxError: invalid syntax
>>> def hello(name):
	print ("hello", name)

	
>>> hello("lateef")
hello lateef
>>> hello ("ibrahim")
hello ibrahim
>>> 
>>> 
>>> def add(x,y):
	return(x+y)

>>> sum1=add(x,y)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    sum1=add(x,y)
NameError: name 'x' is not defined
>>> sum1=add(23,12)
>>> 
>>> sum1
35
>>> 
sum2=add(20,30)
>>> sum2
50
>>> 
>>> 
>>> def studentscore(name, score):
	print(name "scored", score "marks")
	
SyntaxError: invalid syntax
>>> 
>>> def studentscore(name, score):
	print(name, "scored", score, "marks")

	
>>> studentscore(lateef, 85)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    studentscore(lateef, 85)
NameError: name 'lateef' is not defined
>>> studentscore("lateef", 85)
lateef scored 85 marks
>>> 
>>>  def studentscore(name="john", score=0):
	print(name, "scored", score, "marks")
	
SyntaxError: unexpected indent
>>> def studentscore(name="john", score=0):
	print(name, "scored", score, "marks")

	
>>> studentscore
<function studentscore at 0x0314D030>
>>> studentscore()
john scored 0 marks

def studentscore(name, *score):
        print(name)
        print(score)

studentscore('john', 43,56,98,76,56)
