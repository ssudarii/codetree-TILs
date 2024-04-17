sum_val = 0
cnt = 0

for i in range(10):
    inp = int(input())
    if 0 <= inp <= 200 :
        sum_val += inp
        cnt += 1 

print(sum_val, end=" ")
print("%.1f" % (sum_val / cnt))