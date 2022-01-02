# step function in python
for i in range(6):
  print(i)

for a in range(1,6):
  print(a)

for x in range(0,7,2):
  print(x)




colours=['purple','black','green','blue']
items=['canvas','brushes','pallete']
shapes=['circle','triangle','square']
c=colours.copy()
d=colours.count('purple')
e=colours.index('green')
print(c)
print(d)
print(e)
colours.insert(2,'yellow')
colours.append('white')
colours.extend(items)
items.reverse()
items.sort()
shapes.pop(2)
shapes.remove('circle')
print(colours)
print(items)
print(shapes)
