a = input()
b = input()
a = float(a)
b = float(b)

if a >= 1.0 and b >= 1.0 :
    print("High")
elif 1.0 >= a >= 0.5 and 1.0 >= b >= 0.5 :
    print("Middle")
else :
    print("Low")