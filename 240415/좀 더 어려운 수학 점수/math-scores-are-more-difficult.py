a = input()
b = input()
arra = a.split()
arrb = b.split()
am = int(arra[0])
ae = int(arra[1])
bm = int(arrb[0])
be = int(arrb[1])

if am > bm :
    print("A")
elif am == bm and ae > be : 
    print("A")
elif am == bm and ae < be :
    print("B")
else :
    print("B")