from typing import List
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = defaultdict(int)
        for c in s:
            hash[c] += 1
        for i, c in enumerate(s):
            if hash[c] == 1:
                return i
        return -1
