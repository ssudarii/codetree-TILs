n = int(input())
a = 1

for i in range(1, 11):
    a *= i
    if i >= n:
        break
print(i)