# https://new.contest.yandex.ru/41233/problem?id=149944/2022_10_11/iEQ3yuirUx

name = input()
number = int(input())

print(f"Группа №{number // 100}.")
print(f"{number % 10}. {name}.")
print(f"Шкафчик: {number}.")
print(f"Кроватка: { (number // 10) % 10}.")