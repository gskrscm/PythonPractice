
b = [1,2,3,4]

print(b[:2]) # slicing list to first two index s


# skiping in between one number - 3 rd value is range

print(b[:2:2])


c = [ 1, "abc", [1,2,3]]
c[1] = 3     # changing a value in the list with the help of index

c.append(4)  # adding a value to the list
c.append([2,3,4])

print(c)
print(len(c))


d = [1,2]
e = [3,4]
d.extend(e)  # adding e values to d

print(d)
