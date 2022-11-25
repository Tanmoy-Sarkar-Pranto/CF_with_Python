str1 = input()

new_str1 = list(str1.split('+'))
new_str1 = list(map(int, new_str1))
new_str1 = sorted(new_str1)

cou = len(new_str1)

for i in range(len(new_str1)):
    print(str(new_str1[i]), end='')
    cou -= 1
    if cou == 0:
        break
    print('+', end='')


# for i in range(len(str1)):
