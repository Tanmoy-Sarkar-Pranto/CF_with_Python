index = []
for row in range(5):
    a = list(map(int, input().split()))
    for num in a:
        if num == 1:
            i = a.index(num)
            index.append(row)
            index.append(i)
            break


print(abs(index[0] - 2) + abs(index[1] - 2))
