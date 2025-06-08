from typing import List

def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
    
# Test cases
print(binary_search([-1,0,2,4,6,8] ,4))
print(binary_search( [-1,0,2,4,6,8],3))
