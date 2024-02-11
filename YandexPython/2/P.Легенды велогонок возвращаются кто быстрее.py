# https://new.contest.yandex.ru/41234/problem?id=149944/2022_10_12/YgmbeuRvZE

pet = int(input())
vas = int(input())
tol = int(input())
names = {pet: "Петя", vas: "Вася", tol: "Толя"}
top = [pet, vas, tol]
top = sorted(top)
print(f"          {names[top[2]]}")
print(f"  {names[top[1]]}")
print(f"                  {names[top[0]]}")
print("   II      I      III ")
