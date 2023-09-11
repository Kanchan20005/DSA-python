class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums)
        while first < last:
            mid = int(first+(last-first)//2)
            if nums[mid] ==  target:
                return mid
            elif nums[mid] < target:
                first = mid+1
            else:
                last = mid
        return -1
