a = input()
arr = a.split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a <= b and a <= c :
    print(a)
elif a <= b and a >= c :
    print(c)
else : 
    print(b)