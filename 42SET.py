Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A= {1,2,3,4,5,6,7,8,9}
>>> A
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> B= {10, 11, 12, 13, 14, 15}
>>> b
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> B
{10, 11, 12, 13, 14, 15}
>>> A | B
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
>>> A.union(B)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
>>> A & B
set()
>>> A.intersection(B)
set()
>>> A-B
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> B-A
{10, 11, 12, 13, 14, 15}
>>> A ^ B
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
>>> A.symmetric_difference(B)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
>>> 
dir(A)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> 
