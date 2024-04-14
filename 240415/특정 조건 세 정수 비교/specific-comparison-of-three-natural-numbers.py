a = input()
arr = a.split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

print(int(a == min(a, b, c)), end = " ")
print(int(a == b == c))