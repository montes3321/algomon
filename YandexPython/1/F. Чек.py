# https://new.contest.yandex.ru/41233/problem?id=149944/2022_10_11/4rIMUQ1ZZQ
#alt+ctrl+l
name = input()
price = int(input())
mass = int(input())
money = int(input())
antiprice = int(money - mass * price)

print("Чек")
print(f"{name} - {mass}кг - {price}руб/кг")
print(f"Итого: {mass * price}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {antiprice}руб")
