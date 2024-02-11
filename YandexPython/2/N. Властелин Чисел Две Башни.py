# https://new.contest.yandex.ru/41234/problem?id=149944/2022_10_12/gfPvJGE4si

n = input()
a = int(n[0] + n[1])
b = int(n[0] + n[2])
c = int(n[1] + n[0])
d = int(n[1] + n[2])
e = int(n[2] + n[0])
f = int(n[2] + n[1])
spis = []
for i in (a, b, c, d, e, f):
    if i >= 10:
        spis.append(i)
print(f'{min(spis)} {max(spis)}')
