from typing import List
class Solution:
  def hasDuplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
  

print(Solution().hasDuplicate([1, 2, 3, 3])) # true
print(Solution().hasDuplicate([1, 2, 3, 4])) # false