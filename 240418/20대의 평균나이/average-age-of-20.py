sum_val = 0
cnt = 0

while True:
    n = int(input())
    sum_val += n 
    cnt += 1
    if n < 20 or n > 30:
        break
    else :
        continue

print("%.2f" % (sum_val / cnt))