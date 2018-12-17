Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 9>10
False
>>> 9<10 and 7>5
True
>>> 8==10 or 3<4
True
>>> a=("abcde")
>>> b=("abcde")
>>> a is b
True
>>> a=(12345)
>>> b=(12345)
>>> a=b
>>> a=b
>>> a is b
True
>>> s=(1,2,3,4,5)
>>> d=(1,2,3,4,5)
>>> s is d
False
>>> strind= ("asdfh")
>>> a in strind
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a in strind
TypeError: 'in <string>' requires string as left operand, not int
>>> 
>>> string= ("asdfh")
>>> a in string
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a in string
TypeError: 'in <string>' requires string as left operand, not int
>>> strind= ("asdfh")
>>> 'a' in strind
True
>>> 'as' in strind
True
>>> 'ad' in strind
False
>>> 'fh' in strind
True
>>> 
