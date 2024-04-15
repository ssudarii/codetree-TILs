a, b = map(int, input().split())

print("0.", end="")
a *= 10
print(int(a / b), end="")
for _ in range(19) :
    print("0", end="")