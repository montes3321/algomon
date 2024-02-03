# https://new.contest.yandex.ru/41233/problem?id=149944/2022_10_11/cpwScRzQ0S
h = int(input())
m = int(input())
timer = int(input())
total = h * 60 + m + timer
print(f"{str(total // 60 % 24).zfill(2)}:{str(total % 60).zfill(2)}")
