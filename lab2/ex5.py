a = input()
lens = len(a)
dec = 0
for i in range(0, lens):
    dec = dec + int(a[i]) * (2**(lens-i-1))
print(dec)


