Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=2
b=2
print(a+b)
4
print(a-b)
0
print(a*b)
4
print(a//b)
1
print(a/b)
1.0
print(a**b)
4
print(a%b)
0
#Assignment
a=4
b=6
a+=b
a
10
a-=3
a
7
a*=4
a
28
a**=3
a
21952
a//=3
a
7317
a/=2
a
3658.5
a%=4
a
2.5
print(a+=b)
SyntaxError: invalid syntax
b+=a
b
8.5
b-=3
b
5.5
b*=3
b
16.5
b**=3
b
4492.125
b//=3
b
1497.0
b/=2
b
748.5
b%=2
b
0.5
#comparision
a=5
b=8
a<b
True
a>b
False
b>a
True
b<a
False
a<=b
True
b>=a
True
a!=b
True
a==b
False
a=5
b=5
a==b
True
#Logica
#Logical
a=20
b=40
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or b>=a
True
a!=b or a==b
True
not True
False
not False
True
#indentifiy
a=3
type(a) is int
True
type(a) is not int
False
type(a) is float
False
a=5.6
type(a) is float
True
type(a)is not float
False
b="uday"
type(b) is string
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    type(b) is string
NameError: name 'string' is not defined. Did you forget to import 'string'?

type(b) is str
True
type(b) is not str
False
c=4+3j
type(c) is complex
True
type(c) is not complex
False
d=True
type(d) is bool
True
type(d) is not bool
False
>>> a=2,3,4,5,6,7,10,9
>>> 9 in a
True
>>> 20 not in a
True
>>> 30 in a
False
>>> #Bitwise
>>> a=3
>>> b=4
>>> a&b
0
>>> bin(3)
'0b11'
>>> bint(4)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    bint(4)
NameError: name 'bint' is not defined. Did you mean: 'bin'?
>>> bin(4)
'0b100'
>>> a=2
>>> b=4
>>> a|b
6
>>> #~Negosiation
>>> a=5
>>> ~a
-6
>>> a=-3
>>> ~a
2
>>> a=3
>>> b=4#Xor
>>> a^b
7
>>> #Left Shift
>>> a<<b
48
>>> #right shift
>>> a>>b
0
>>> a=5
>>> b>>2
1
