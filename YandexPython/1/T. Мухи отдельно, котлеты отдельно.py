# https://new.contest.yandex.ru/41233/problem?id=149944/2022_10_13/Kh8Awf5qUi

N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())
# x*K1 + y*K2 = N*M
# x + y = N

x = (N * M - N * K2) / (K1 - K2)
y = N - x
print(int(x), int(y))
