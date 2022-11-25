n = int(input())
x = 0
while n > 0:
    arr = input()
    if arr == "++X" or arr == "X++":
        x += 1
    elif arr == "--X" or arr == "X--":
        x -= 1
    n -= 1
print(x)
