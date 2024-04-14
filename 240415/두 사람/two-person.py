a = input()
b = input()
arr1 = a.split()
arr2 = b.split()

aa, ag = int(arr1[0]), arr1[1]
ba, bg = int(arr2[0]), arr2[1]

if ( aa >= 19 and ag == "M" ) or ( ba >= 19 and bg == "M") :
    print("1")
else :
    print("0")