a, b = map(int, input().split())
cnt = 0
sum_val = 0
avg_val = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i 
        cnt += 1

avg_val = sum_val / cnt

print(sum_val, end=" ")
print("%.1f" % (avg_val))