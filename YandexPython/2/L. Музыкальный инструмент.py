# https://new.contest.yandex.ru/41234/problem?id=149944/2022_10_12/eWUZpmaeOr

l1 = int(input())
l2 = int(input())
l3 = int(input())

if max(l1, l2, l3) < (l1 + l2 + l3 - max(l1, l2, l3)):
    print("YES")
else:
    print("NO")
