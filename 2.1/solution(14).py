n = int(input())
m = int(input())
t = int(input())
n += t // 60
m += t - t // 60 * 60
if m > 59:
    n += 1
    m -= 60
if len(str(m)) == 1:
    mm = '0' + str(m)
else:
    mm = str(m)
while n >= 24:
    n -= 24
if len(str(n)) == 1:
    nn = '0' + str(n)
else:
    nn = str(n)
print(nn + ':' + mm)