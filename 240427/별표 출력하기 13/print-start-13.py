n = int(input())
cnt_o = 1
cnt_e = n

for i in range(n*2):
    if i % 2 == 0:
        print("* " * cnt_e)
        cnt_e -= 1
    else:
        print("* " * cnt_o)
        cnt_o += 1