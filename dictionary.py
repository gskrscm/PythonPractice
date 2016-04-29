
a = (1,2,3) #tuple - It is immutable list

b = {'a' : 5}  # Dictionary - key value pair

b ['c'] = 10 # Adding new value to dictionary. It can be added at the end or start or any where

# Changing value
b ['c'] = 20 # Changing value of a dictionary element

b [a] = 35  # Adding tuple 'a' as key.

print(b)
print(b['a'])
print(b[a])

del(b['c']) # deleting a key from the dictionary

print(b)