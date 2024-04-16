a = input()
arr = a.split()
c = arr[0]
n = int(arr[1])
p = 1

if c == 'A':
    for _ in range(1, n+1):
        print(p, end=" ")
        p += 1
else :
    for _ in range(1, n+1, -1):
        print(p, end=" ")
        p += 1