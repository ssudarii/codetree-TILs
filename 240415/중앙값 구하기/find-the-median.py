inp = input()
arr = inp.split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a > b and c > a :
    print(a)
elif b > a and c > b :
    print(b)
else :
    print(c)