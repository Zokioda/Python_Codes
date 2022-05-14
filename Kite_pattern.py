# n denotes size of upper triangle
n = 3
# b gives space in lower triangle
b = 1
# For lower triangle
m = n + 2
# The loop runs 5 times so as to print 5 rows from 0... to ... 5
for i in range(1, n + 3):
    if i <= 3:
        for j in range(n - i):
            print(' ', end='')
        for k in range(2 * i - 1):
            print('*', end='')
        print()
    else:
        for x in range(b):
            print(' ', end='')
        b = b + 1
        for y in range(m - 2):
            print('*', end='')
        m = m - 2
        print()
