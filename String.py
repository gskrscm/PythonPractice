
a = "Siva"

print(a[:2])  # string slice - printing first two characters

#last one to print
print(a[-1:]) # printing last one character


print(a[::-1]) # reversing the string and printing

# indexing  Forward : 0 1 2 ...  backwar: -1, -2, -3
print(a[-2:-4:-1])

print(a[-4:-2:1])

a = "abhi"
b = "shek"

c = a + b #  Adding two strings

print(c)

d = a[:2] + b[2:]  # adding two string and also slicing

print(d)


k = a[:2] + b [-2:]   # more optimized way to get above result
print(k)