Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> a="i am in class"
>>> a[8]+a[9]+a[10]+a[11]
'clas'
>>> a[8]+a[9]+a[10]+a[11]+a[12]
'class'
>>> a[2]+a[3]
'am'
>>> a[1]
' '
>>> a[4]
' '
>>> a[7]
' '
>>> a="vijayawada is a royal city"
>>> a[15]+a[16]+a[17]+a[18]+a[19]
' roya'
>>> a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
>>> a[22]+a[23]+a[24]+a[25]
'city'
>>> a="vizag is a city of destiny"
>>> a[-12]+a[-13]+a[-14]+a[-15]
'ytic'
>>> a[-15]+a[-14]+a[-13]+a[-12]
'city'
>>> a[-26]+a[-25]+a[-24]+a[-23]+a[-22]
'vizag'
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'destiny'
>>> a="Simple is better than complex"
>>> a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
>>> aa[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    aa[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
NameError: name 'aa' is not defined. Did you mean: 'a'?
>>> a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'Simple'
>>> #indexing completed
>>> a="Codegnan"
>>> a=[0:4]
SyntaxError: invalid syntax
a=[0: 4]
SyntaxError: invalid syntax
a[0:4]
'Code'
a[:4]
'Code'
a[4:]
'gnan'
a="work hard untill you succeed"
a[11:18]
'ntill y'
a[10:17]
'untill '
a[5:9]
'hard'
a[0:4]
'work'
a[17:20]
'you'
a[21:28]
'succeed'
a="Time is very precious"
a[13:21]
'precious'
a[8:12]
'very'
a="I love python"
a[11:7]
''
a[-11:-7]
'love'
a[-6:-1]
'pytho'
a[-6]
'p'
a[-6:]
'python'
b="today is weekend"
a[-15:-10]
'I l'
b=[-15:-10]
SyntaxError: invalid syntax
b=[-16:-11]
SyntaxError: invalid syntax

b[-16:-11]
'today'
b[-10:-8]
'is'
b[-8:]
' weekend'
#slicing completed
#Index[a] slicing[a:b] striding[a:b:c]
a="Data science"
a[::]
'Data science'
a[::1]
'Data science'
a[::2]
'Dt cec'
a="Machine learning"
a[::4]
'Miln'
a[::6]
'Men'
a[::2]
'Mcielann'
a[5:]
'ne learning'
a[:9]
'Machine l'
a[::7]
'M n'
a="Cloud computing"
a[1:11:2]
'lu op'
a[2:14:4]
'ocu'
a[5:13:3]
' mt'
a[4:12:2]
'dcmu'
a="Python course"
a[-1:-11:-2]
'ero o'
a[-2:-12:-3]
'sont'
# in positive striding highest to lowest not possible
