# https://new.contest.yandex.ru/41233/problem?id=149944/2022_10_11/U5mhQZQkQh

name = input()
price = int(input())
mass = int(input())
money = int(input())

print("================Чек================")
print(f"Товар:{name.rjust(29)}")
print(f"Цена:" + f"{str(mass)}кг * {price}руб/кг".rjust(30))
print(f"Итого:{str(price * mass).rjust(26)}руб")
print(f"Внесено:{str(money).rjust(24)}руб")
print(f"Сдача:{str(money - mass * price).rjust(26)}руб")
print("===================================")
