n = int(input())

for i in range(1, n+1):
    if i % 3 == 0 or 30 <= i < 40 or 60 <= i < 70 or 90 <= i < 100 or i % 10 == 3 or i % 10 == 6 or i % 10 == 9 : 
        print("0", end=" ")
        i += 1
    else :
        print(i, end=" ")
        i += 1