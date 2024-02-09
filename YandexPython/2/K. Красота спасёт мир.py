# https://new.contest.yandex.ru/41234/problem?id=149944/2022_10_12/PyEGwcX6zO

num = int(input())

ch3 = num % 10
ch2 = num // 10 % 10
ch1 = num // 100 % 100

if min(ch3, ch2, ch1) + max(ch3, ch2, ch1) == (ch3 + ch2 + ch1 - min(ch3, ch2, ch1) - max(ch3, ch2, ch1)) * 2:
    print("YES")
else:
    print("NO")
