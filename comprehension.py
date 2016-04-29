

a = [2, 4, 9, 5, 15]

b = [i for i in a if not i%2]

print(b)

c = {i:i*i for i in a}

print(c)

d = {'a':3, 'b':5}

print(d.keys())

for i in d.keys():
    #print(i)
    print(d[i])


f = {1:2, 2:3, 3:4, 4:5}
g = []
# create a list of values whose key is even number

for i in f.keys():
     if not i%2:
         g.append(f[i])

print(g)