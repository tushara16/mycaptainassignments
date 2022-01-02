# 1. Tuples are immutable,then how can you change a value in a tuple?
# ANSWER: we can convert the tuple into a list, change the list, and convert the list back into a tuple.

# 2. SETS in pythom
# SET:
# is unoredered,unchangeable,unindexed. But we can add and remove items from a set.
# Denoted with curly braces
# there are no duplicate items in a SET
# eg: set1={'car','bike','bicycle'}


# 3.creating dict with number as a key
keys=['1','2','3','4','5']
values=['python','java','c++','c','javascript']
data=dict(zip(keys,values))
print(data)


# methods of dict

dict1={'one':'1','two':'2','three':'3','four':'4'}
a=dict1.get('two')
b=dict1.items()
c=dict1.copy()
d=data.fromkeys(values)
e=dict1.keys()
f=dict1.pop('three')
g=dict1.popitem()
h=dict1.update({'five':'5'})
i=dict1.values()
print(a)
print(b)
print(c)
print(d)
print(e)
print(dict1)
print(g)
print(dict1)
print(h)
print(dict1)
print(i)


# methods of string


text="hello,How are you"
txt="   cookies   "
txt1="hello\n this is tushara "
txt2="20"
j=text.capitalize()
k=text.casefold()
l=text.center(40)
m=text.encode()
n=text.endswith(".")
o=text.expandtabs(10)
p=text.find("are")
q=text.isalpha()
r=text.isprintable()
s=text.isidentifier()
t=".".join(dict1)
u=text.maketrans("h","y")
v=text.partition("are")
w=text.replace("hello","hi")
x=txt.rstrip()
y=txt.lstrip()
z=txt1.splitlines()
A=text.swapcase()
B=txt2.zfill(10)
print(j)
print(k)
print(l)
print(m)
print(n)
print(o)
print(p)
print(q)
print(r)
print(s)
print(t)
print(text.translate(u))
print(v)
print(w)
print("out of all foods",x,"are my favourite")
print("out of all foods",y,"are my favourite")
print(z)
print(A)
print(B)
