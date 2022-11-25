num = int(input())

if num >= 0:
    print(num)

else:
    num = str(abs(num))
    num = [int(x) for x in str(num)]
    # print(num)
    num1 = num.copy()
    num2 = num.copy()
    # print(num1,num2)
    num1.pop(len(num1) - 1)
    # print(num1)
    num2.pop(len(num2) - 2)
    # print(num2)
    s1 = [str(i) for i in num1]
    s1 = int("".join(s1))
    s2 = [str(i) for i in num2]
    s2 = int("".join(s2))
    # print(s1,s2)
    if -s1 > -s2:
        print(-s1)
    else:
        print(-s2)
