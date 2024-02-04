# https://new.contest.yandex.ru/41234/problem?id=149944/2022_10_12/EAxwf5ePS0

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("YES")
else:
    print("NO")
