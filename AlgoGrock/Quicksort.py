
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0] # опорный элемент
        # генераторы меньшего и большего случая от опорного
        less = [i for i in array[1:] if i < pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([3,8,1,45,0,43]))