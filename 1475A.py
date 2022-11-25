n = int(input())
nums = []
for i in range(n):
    a = int(input())
    nums.append(a)

for num in nums:
    while num % 2 == 0:
        num = num // 2
    if num == 1:
        print("NO")
    else:
        print("YES")
