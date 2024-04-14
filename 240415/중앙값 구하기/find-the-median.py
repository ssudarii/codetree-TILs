inp = input()
arr = inp.split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a > b :
    if b > c :
        print(b)
    elif c > a :
        print(a)
elif a > c :
    if c > b :
        print(c)