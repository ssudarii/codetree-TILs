a = input()
arr = a.split()
h = int(arr[0])
w = int(arr[1])
b = w / (h/100)**2
print(int(b))
if b >= 25 :
    print("Obesity")