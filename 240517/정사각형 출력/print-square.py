n = int(input())
cnt = 0

for i in range(n):
    for j in range(1, n+1):
        print(cnt+j, end=" ")
    cnt += n
    print()