a = input()
b = input()
arr1 = a.split()
arr2 = b.split()
am = int(arr1[0])
ae = int(arr1[1])
bm = int(arr2[0])
be = int(arr2[1])

if am > bm and ae > be :
    print("1")
else :
    print("0")