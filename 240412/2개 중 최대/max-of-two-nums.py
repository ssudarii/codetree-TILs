a = input()
arr = a.split()
a = int(arr[0])
b = int(arr[1])
c = a if a > b else b
print(c)