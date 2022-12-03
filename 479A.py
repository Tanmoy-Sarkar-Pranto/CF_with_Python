a = int(input())
b = int(input())
c = int(input())

sum1 = (a + b + c)
sum2 = (a + b) * c
sum3 = (a * b) + c
sum4 = a * b * c
sum5 = a + (b * c)
sum6 = a * (b + c)

tsum = [sum1, sum2, sum3, sum4, sum5, sum6]
print(max(tsum))
