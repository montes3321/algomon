# https://new.contest.yandex.ru/41233/problem?id=149944/2022_10_11/9RyTbOQjMP

a = int(input())
b = int(input())
h1 = ((a // 100 + b // 100) % 10) * 100
h2 = ((a // 10 % 10 + b // 10 % 10) % 10) * 10
h3 = (a % 10 + b % 10) % 10
print(h1 + h2 + h3)
