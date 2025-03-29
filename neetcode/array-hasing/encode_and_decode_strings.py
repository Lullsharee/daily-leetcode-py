from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(s)) + '#' + s for s in strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j + 1:i])
        return strs