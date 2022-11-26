x = int(input())
x = x * 45 + (x // 2) * 5 + ((x + 1) // 2 - 1) * 15
print(x // 60 + 9, x % 60)