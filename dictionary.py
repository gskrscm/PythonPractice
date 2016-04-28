
a = (1,2,3) #tuple

b = {'a' : 5}

b ['c'] = 10

# Changing value
b ['c'] = 20

b [a] = 35

print(b)
print(b['a'])
print(b[a])

del(b['c'])

print(b)