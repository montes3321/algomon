# Смотрим на сумму всех чисел, вычитаем из неё все числа - получаем ответ
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res += i+1-nums[i]
        return res
