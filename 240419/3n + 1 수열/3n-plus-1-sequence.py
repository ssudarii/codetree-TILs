N = int(input())
cnt = 0

while True:
    if N % 2 == 0:
        N = N // 2
        cnt += 1
        if N == 1:
            break
        
        
    elif N % 2 != 0:
        if N == 1:
            break
        N = N * 3 + 1
        cnt += 1

print(cnt)