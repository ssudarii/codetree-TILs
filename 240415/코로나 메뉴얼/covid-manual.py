p1 = input()
p2 = input()
p3 = input()

arr1 = p1.split()
arr2 = p2.split()
arr3 = p3.split()

s1, t1 = arr1[0], float(arr1[1])
s2, t2 = arr2[0], float(arr2[1])
s3, t3 = arr3[0], float(arr3[1])


if ( s1 == "Y" and t1 >= 37 ) and ( s2 == "Y" and t2 >= 37 ) or ( s2 == "Y" and t2 >= 37 ) and ( s3 == "Y" and t3 >= 37 ) or ( s1 == "Y" and t1 >= 37 ) and ( s3 == "Y" and t3 >= 37 ) or ( s1 == "Y" and t1 >= 37 ) and ( s2 == "Y" and t2 >= 37 ) and (s3 == "Y" and t3 >= 37) :
    print("E")
else :
    print("N")