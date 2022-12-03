import math
n = int(input())

tsum = 0
if n % 2 == 0:
    print(n//2)
else:
    a = math.ceil(n/2)
    print(-a)
