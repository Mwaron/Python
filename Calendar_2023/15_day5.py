f = open('15_day5')
sz = f.readlines()
f.close()

i = 0
while i < len(sz):
    line = sz[i]
    sz[i] = line.replace('\n', '')
    i += 1


def maganh(line):
    mgh = 0
    for c in line:
        if c in 'aeiou':
            mgh += 1
        if mgh >= 3:
            return True
    return False


def twoLetters(line):
    if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
        return False
    else:
        return True

def similarLetters(line):
    x = 0
    while x < len(line)-1:
        if line[x] == line[x+1]:
            return True
        x += 1
    return False

def repeat(line):
    i = 0
    maxl = len(line)
    while i < maxl-1:
        hely = line[i + 2: maxl]
        letters = line[i] + line[i+1]
        if letters in hely:
            return True
        i += 1
    return False

    '''
    maxL = len(line)
    i = 0
    letters = line[i] + line[i + 1]
    c = str.count(letters[i+1[, maxL-1]])
    return c
    '''

def letterBetween(line):
    i = 0
    while i < len(line)-2:
        if line[i] == line[i+2]:
            return True
        i += 1
    return False


niceStrings = 0
for l in sz:
    cr = repeat(l)
    lB = letterBetween(l)
    mgh = maganh(l)
    twoL = twoLetters(l)
    similarL = similarLetters(l)

    if cr == True and lB == True:
        niceStrings += 1

print(niceStrings)
