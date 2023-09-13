# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        ne = range(1,n+1)
        first, last = 1, len(ne)
        while first < last:
            mid = int(first+(last-first)//2)
            fb = isBadVersion(mid)
            fa = isBadVersion(mid+1)
            if not fb and fa:
                return mid+1
            if not fb:
                first = mid+1
            else:
                last = mid
        return 1