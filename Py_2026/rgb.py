"""1. Olvassa be a kep.txt állomány tartalmát, és tárolja el a 640×360 képpont színét! """
sz = []
with open('kep', 'r') as f:
    for line in f:
        line = line.replace('\n', '').split(' ')
        for t in line:
            t = int(t)
        sz.append(line)
print(line)