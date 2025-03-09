import datetime

sz = []
m = []
i = 1
with open("lista.txt", 'r') as f:
    for line in f:
        line = line.replace('\n', '').split(' ')
        if i % 5 != 0:
            m.append(line)

        else:
            sz.append(m)
            m = []
        i += 1
print(sz)

