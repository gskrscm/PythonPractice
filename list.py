
b = [1,2,3,4]

print(b[:2])


# skiping in between one number - 3 rd value is range

print(b[:22])
print(b[:2:2])


c = [ 1, "abc", [1,2,3]]
c[1] = 3

c.append(4)
c.append([2,3,4])

print(c)
print(len(c))


d = [1,2]
e = [3,4]
d.extend(e)

print(d)
