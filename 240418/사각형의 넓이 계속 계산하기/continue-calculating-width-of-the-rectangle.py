while True:
    arr = input().split()
    a, b, d = int(arr[0]), int(arr[1]), arr[2]
    print(a * b)
    if d == "C":
        break
    else : 
        continue