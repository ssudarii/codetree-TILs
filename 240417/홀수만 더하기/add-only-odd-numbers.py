n = int(input())
sum_val = 0 

for i in range(n): 
    inp = int(input())
    if inp % 2 == 1 and inp % 3 == 0:
        sum_val += inp

print(sum_val)