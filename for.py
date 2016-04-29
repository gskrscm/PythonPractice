

# for loop helps to iterate the list

foods = ['bacon', 'jam', 'chicken', 'jelly']

for f in foods:
    print(f)
    print(len(f))
    if f is "jam" :
        print("Jam is in the list of foods")

# slicing the list to print first two values
print("---------------------")
for f in foods[:2]:
    print(f)

for n in range(10):
    if(n%2 is 0):
        print(n)

for n in range(0, 10, 2):
    print(n)

for n in range(10):
    if not n%2:
        print(n)

b =[]
for n in [2, 4, 5, 9, 12, 15]:
    if not n%2:
        b.append(n)

print(b)
