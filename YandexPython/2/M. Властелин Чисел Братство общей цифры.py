# https://new.contest.yandex.ru/41234/problem?id=149944/2022_10_12/KtQaUtVqTY

elf = int(input())
gnom = int(input())
human = int(input())

if (elf % 10 == gnom % 10 and elf % 10 == human % 10):
    print(elf % 10)
else:
    print(elf // 10)
