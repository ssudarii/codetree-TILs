n = int(input())

for i in range(n, 101):
    if n < 60 : 
        print("F", end=" ")
        n += 1
    elif 70 > n >= 60 :
        print("D", end=" ")
        n += 1
    elif 80 > n >= 70 :
        print("C", end=" ")
        n += 1
    elif 90 > n >= 80 :
        print("B", end=" ")
        n += 1
    else : 
        print("A", end=" ")
        n += 1