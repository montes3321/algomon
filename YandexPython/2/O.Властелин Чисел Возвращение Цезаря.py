# https://new.contest.yandex.ru/41234/problem?id=149944/2022_10_12/uZilCvBkHW

num1 = int(input())
num2 = int(input())

n1, n2, n3, n4 = num1 // 10, num1 % 10, num2 // 10, num2 % 10

num = max(n1, n2, n3, n4) * 100 + min(n1, n2, n3, n4) + (
            (n1 + n2 + n3 + n4 - max(n1, n2, n3, n4) - min(n1, n2, n3, n4)) % 10) * 10

print(num)