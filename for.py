foods = ['bacon', 'jam', 'chicken', 'jelly']

for f in foods:
    print(f)
    print(len(f))
    if f is "jam" :
        print("Jam is in the list of foods")

print("---------------------")
for f in foods[:2]:
    print(f)