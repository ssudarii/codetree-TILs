a, b = map(int, input().split())
sum_val = 0 

if a % 2 == 0:
    for i in range(a, b+1, 2):
        sum_val += i
else : 
    for i in range(a+1, b+1, 2):
        sum_val += i
    
print(sum_val)