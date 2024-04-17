n = int(input())
sum_val = 0
cnt = 0

for i in range(n):
    inp = int(input())
    sum_val += inp
    cnt += 1

print(sum_val, end=" ")
print("%.1f" % (sum_val / cnt))