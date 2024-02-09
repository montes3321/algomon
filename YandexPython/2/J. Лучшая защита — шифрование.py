# https://new.contest.yandex.ru/41234/problem?id=149944/2022_10_12/3QAUeGXx5F

inf = int(input())

part1 = inf % 10
part2 = (inf // 10) % 10
part3 = inf // 100 % 10
ch1 = part1 + part2
ch2 = part3 + part2

if ch1 > ch2:
    print(ch1, ch2, sep="")
else:
    print(ch2, ch1, sep="")
