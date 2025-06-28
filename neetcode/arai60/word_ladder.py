from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        word_set = set(wordList)

        queue = deque([(beginWord, 1)])

        visited = set([beginWord])

        while queue:
            current_word, steps = queue.popleft()

            if current_word == endWord:
                return steps

            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == current_word[i]:
                        continue

                    new_word = current_word[:i] + c + current_word[i+1:]

                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, steps + 1))
        return 0

