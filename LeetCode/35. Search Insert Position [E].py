class Solution:
    def searchInsert(self, list: List[int], item: int) -> int:
            low = 0
            high = len(list) - 1

            while low <= high:
                mid = (low + high) // 2
                guess = list[mid]
                if guess == item:
                    return mid  # значение найдено
                if guess > item:
                    high = mid - 1
                else:
                    low = mid + 1
            if item > list[mid]:
                mid+=1
            return mid