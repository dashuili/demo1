import collections
str = "I'm maaz pleasa call me Mr maaz"

c= collections.Counter(str.split(' '))
print(c)
print(c.items())
for key,value in c.items():
    print(key,value)
    print(key+":" + value)


