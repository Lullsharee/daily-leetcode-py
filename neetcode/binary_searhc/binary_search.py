from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        left, right = 0 , len(sorted_nums) - 1
        while left <= right:
            mid = left + (right -left) // 2
            if sorted_nums[mid] == target:
                return mid
            elif sorted_nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    # Test cases
print(Solution().search([-1,0,2,4,6,8] ,4))
print(Solution().search( [-1,0,2,4,6,8],3))

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0 , len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1