N = int(input())

cnt = 0
a = 1

while True :
    a *= 2
    cnt += 1
    if a == N :
        break   

print(cnt)