T = int(input())
while T > 0:
    S1 = input()
    S2 = input()
    minn = maxx = 0
    for i in range(0, len(S1)):
        if S1[i] != S2[i] or S1[i] == '?' or S2[i] == '?':
            maxx += 1
        if S1[i] != S2[i] and S1[i] != '?' and S2[i] != '?':
            minn += 1
    print(minn, " ", maxx, '\n')
    T -= 1
    print("DONE!!!")
