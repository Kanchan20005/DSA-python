class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        sets = set(nums)
        # print(sets)
        for i in sets:
            dict[i] = nums.count(i)
            if dict[i] > len(nums)/2:
                return i