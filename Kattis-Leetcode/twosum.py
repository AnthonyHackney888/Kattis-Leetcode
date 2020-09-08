class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        test = {}
        for i, num in enumerate(nums):
            other = target - num
            if other in test:
                return [test[other], i]
            else:
                test[num] = i
        return []
                