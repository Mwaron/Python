import hashlib

s = "yzbqklnj"
szam = 1
result = 0
Value = False

while Value == False:
    code = s + str(szam)
    result = hashlib.md5(code.encode())
    hresult = result.hexdigest()
    hresult = str(hresult)
    if hresult[0] == "0" and hresult[1] == "0" and hresult[2] == "0" and hresult[3] == "0" and hresult[4] == "0" and hresult[5] == "0":
        Value = True
    else:
        szam = int(szam)
        szam += 1

print(hresult)
print(code)