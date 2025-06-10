
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            sub = target - num
            if sub in hash_map:
                return [hash_map[sub], i]
            hash_map[num] = i
