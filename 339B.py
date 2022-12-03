n, m = list(map(int, input().split()))[:2]

# print(n, m)
tasks = list(map(int, input().split()))[:m]
# print(tasks)
steps = 0
house_no = 1

for i in tasks:
    if house_no != i:
        if i > house_no:
            req = i - house_no
            steps += req
            house_no = i
            # print(f"i>house:{steps}, {house_no}")
        elif i < house_no:
            steps += n - house_no + 1
            req = i - 1
            steps += req
            house_no = i
            # print(f"i<house:{steps}, {house_no}")

print(steps)
