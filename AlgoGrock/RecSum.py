def recursiveSumList(list):
    if list == []:
        return 0
    else:
        return list[0] + recursiveSumList(list[1:])

def recursiveCountList(list):
    if list==[]:
        return 0
    else:
        return 1 + recursiveCountList(list[1:])

def recursiveMax(list):
    if len(list)==2:
        return list[0] if list[0]>list[1] else list[1]
    sub_max = recursiveMax(list[1:])
    return list[0] if list[0] > sub_max else sub_max


a = [1,2,3,744,319,3,531,43]
print(recursiveSumList(a), recursiveCountList(a), recursiveMax(a))