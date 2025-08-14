from collections import defaultdict
from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        set_hash = defaultdict(set)

        for email in emails:
            local, domain = email.split('@')
            extract_local = local.split('+').replace('.', '')
            set_hash[domain].add(extract_local)
        return sum(len(s) for s in set_hash.values())
