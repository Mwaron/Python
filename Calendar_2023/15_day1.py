f = open('15_day1')
sz = f.readline()
f.close()

x = 0
floor = 0

while x < len(sz):
    if sz[x] == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(x)
    x += 1

print(floor)