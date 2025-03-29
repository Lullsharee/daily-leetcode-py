from typing import List
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = math.prod(nums)
        result = []
        for num in nums:
            if num == 0:
                if nums.count(0) > 1:
                    result.append(0)
                else:
                  result.append(math.prod([n for n in nums if n != 0]))
            else:
              result.append(total_prod // num)
        return result
    

sol = Solution().productExceptSelf([0,0])
print(sol) # [0, 0]