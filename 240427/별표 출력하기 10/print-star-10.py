n = int(input())
cnt_o = n
cnt_e = 0

for i in range(n*2):
    if i % 2 == 0:
        cnt_e += 1
        print("* " * cnt_e)
    else:
        print("* " * cnt_o)
        cnt_o -= 1