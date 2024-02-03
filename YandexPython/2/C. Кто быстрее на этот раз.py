# https://new.contest.yandex.ru/41234/problem?id=149944/2022_10_12/A0SckMR7Fl

pet = int(input())
vas = int(input())
tol = int(input())

if pet > vas and pet > tol:
    print("Петя")
elif vas > pet and vas > tol:
    print("Вася")
elif tol > pet and tol > vas:
    print("Толя")