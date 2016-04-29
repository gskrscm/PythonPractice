
a = 5

try:
    print(a)
except Exception:
    print("exception")
    # raise an error also 
else:
    print(a)
finally:
    print("finally executed")