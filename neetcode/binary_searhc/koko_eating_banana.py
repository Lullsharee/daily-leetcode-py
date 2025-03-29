from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(mid: int) -> bool:
            hours = 0
            for pile in piles:
                hours += (pile +mid - 1) // mid
            return hours <= h
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if canEatAll(mid):
                right = mid
            else:
                left = mid + 1
        return left
    

# test cases

print(Solution().minEatingSpeed([1,4,3,2], 9)) # 4