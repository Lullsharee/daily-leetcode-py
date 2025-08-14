from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            target_diff = target - num
            if target_diff in dict:
                return [dict[target_diff], i]
            dict[num] = i
        return []
