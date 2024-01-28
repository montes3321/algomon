def binary_search(list,item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return mid # значение найдено
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1

my_list = [1,3,5,6,7,9]

print( binary_search(my_list, 3))
print( binary_search(my_list, -3))
