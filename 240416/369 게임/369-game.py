n = int(input())

for i in range(1, n+1):
    if i % 3 == 0 or ((i % 10) % 3 == 0) : 
        print("0", end=" ")
        i += 1
    else :
        print(i, end=" ")
        i += 1