# https://new.contest.yandex.ru/41233/problem?id=149944/2022_10_11/A8l7ygW6KL

# abcd -> badc

number = int(input())
a = number // 1000 % 10
b = number // 100 % 10
c = number // 10 % 10
d = number % 10

print(b * 1000 + a * 100 + d * 10 + c)