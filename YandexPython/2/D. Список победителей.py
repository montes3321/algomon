# https://new.contest.yandex.ru/41234/problem?id=149944/2022_10_12/zai536kBZM

pet = int(input())
vas = int(input())
tol = int(input())
names = {pet: "Петя", vas: "Вася", tol: "Толя"}
top = [pet, vas, tol]
top = sorted(top)
print(f"1. {names[top[2]]}")
print(f"2. {names[top[1]]}")
print(f"3. {names[top[0]]}")
