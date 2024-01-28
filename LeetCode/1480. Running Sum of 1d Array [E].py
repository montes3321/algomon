# https://leetcode.com/problems/running-sum-of-1d-array/solutions/
#Array
#Prefix Sum

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            out.append(sum)
        return out
