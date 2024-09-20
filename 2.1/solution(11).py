x = input()
y = input()
if len(y) < 3:
    y = '0' + y
print(str(int(x[0]) + int(y[0]))[-1] + str(int(x[1]) + int(y[1]))[-1] + str(int(x[2]) + int(y[2]))[-1])