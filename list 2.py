Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: C:/Users/Asus-PC/Documents/phyton/list.py =============
>>> 
>>> 
============= RESTART: C:/Users/Asus-PC/Documents/phyton/list.py =============
Traceback (most recent call last):
  File "C:/Users/Asus-PC/Documents/phyton/list.py", line 2, in <module>
    ptint (names)
NameError: name 'ptint' is not defined
>>> 
============= RESTART: C:/Users/Asus-PC/Documents/phyton/list.py =============
['lateef', 'azeez', 'toyeeb']
>>> names=["lateef", "azeez", "toyeeb"]
>>> names
['lateef', 'azeez', 'toyeeb']
>>> names[0]
'lateef'
>>> names[-2]
'azeez'
>>> names.append("ismail")
>>> names
['lateef', 'azeez', 'toyeeb', 'ismail']
>>> age=(12, 23, 6, 5)
>>> names.extend(age)
>>> names
['lateef', 'azeez', 'toyeeb', 'ismail', 12, 23, 6, 5]
>>> names.remove("ismail")
>>> names
['lateef', 'azeez', 'toyeeb', 12, 23, 6, 5]
>>> print(names)
['lateef', 'azeez', 'toyeeb', 12, 23, 6, 5]
>>> print(names,age)
['lateef', 'azeez', 'toyeeb', 12, 23, 6, 5] (12, 23, 6, 5)
>>> len(names)
7
>>> max(age)
23
>>> 
