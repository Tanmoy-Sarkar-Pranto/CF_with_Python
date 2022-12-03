n, m = list(map(int, input().split()))[:2]

la_words = []

for i in range(m):
    a = list(map(str, input().split()))[:2]
    la_words.append(a)

# print(la_words)
le_words = list(map(str, input().split()))[:n]

# print(le_words)

for i in range(len(le_words)):
    for l in la_words:
        if l[0] == le_words[i]:
            if len(l[1]) < len(le_words[i]):
                # print("Changed")
                # print(l[1])
                le_words[i] = l[1]

for i in le_words:
    print(i,end=' ')
