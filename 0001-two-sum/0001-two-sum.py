class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li = []
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]+nums[j] == target:
                    li = [i,j]
        return li

