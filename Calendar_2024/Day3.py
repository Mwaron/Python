import re


f = open('Day3')
sz = f.readlines()
f.close()


pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

row = []
i = 0
while i < len(sz):
    match = re.findall(pattern, sz[i])

    j = 0
    while j < len(match):
        if match[j] != "do()" and match[j] != "don't()":
            row.append(match[j][4:-1].split(','))
        else:
            row.append(match[j])
        j += 1
    i += 1

i = 0
osszes = 0

logic = True
while i < len(row):
    if row[i] == "do()":
        logic = True
        print(row[i])
    elif row[i] == "don't()":
        logic = False

    if logic and row[i] != "do()":
        num1 = int(row[i][0])
        num2 = int(row[i][1])
        osszes += num1 * num2
    i += 1

print(osszes)
