inp = input()
arr = inp.split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if ( a > b and b > c ) or ( c > b and b > a ) : 
    print(b)
elif ( c > a and a > b ) or ( b > a and a > c ) : 
    print(a)
elif ( a > c and c > b ) or ( b > c and c > a ) : 
    print(c)