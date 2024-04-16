N = int(input())
for i in range(N):
    inp = int(input())
    if inp % 3 == 0 and inp % 2 == 1:
        print(inp)