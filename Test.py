def resztabla(num):
    if num <= 3:
        return 1
    elif num <= 6:
        return 2
    else:
        return 3


s = resztabla(3)
o = resztabla(5)

print((s-1)*3+o)