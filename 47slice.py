Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #this is to know slicing
>>> a=(0,1,2,3,4,5,6,7,8,9)
>>> b=[0,1,2,3,4,5,6,7,8,9]
>>> c={'12345678'}
>>> x=slice(0,5)
>>> a(x)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a(x)
TypeError: 'tuple' object is not callable
>>> a[x]
(0, 1, 2, 3, 4)
>>> a[0:5]
(0, 1, 2, 3, 4)
>>> c[2:9]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    c[2:9]
TypeError: 'set' object is not subscriptable
>>> c[2:8]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    c[2:8]
TypeError: 'set' object is not subscriptable
>>> c='12345678'
>>> c[2:8]
'345678'
>>> #to use a negaitive number , you need to start from -1 rep the last number
>>> b[-1:-9:-2]
[9, 7, 5, 3]
>>> 
