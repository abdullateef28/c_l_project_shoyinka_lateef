Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[3,4,5,6,7,8,9]
>>> x
[3, 4, 5, 6, 7, 8, 9]
>>> x[4]
7
>>> y=['max',1,3,56.5,[3,3]]
>>> y
['max', 1, 3, 56.5, [3, 3]]
>>> y[0]
'max'
>>> x.insert(2, 'tom')
>>> x
[3, 4, 'tom', 5, 6, 7, 8, 9]
>>>  x.remove('tom')
SyntaxError: unexpected indent
>>> x.remove('tom')
>>> x
[3, 4, 5, 6, 7, 8, 9]
>>> x.pop()
9
>>> x
[3, 4, 5, 6, 7, 8]
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> y.sort()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    y.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> s = y.copy()
>>> s
['max', 1, 3, 56.5, [3, 3]]
>>> 
