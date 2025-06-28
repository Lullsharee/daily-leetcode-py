from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Word Ladderの最短経路の長さを求める関数
        
        Args:
            beginWord: 開始単語
            endWord: 終了単語
            wordList: 使用可能な単語のリスト
        
        Returns:
            最短経路の長さ（変換できない場合は0）
        """
        # endWordがwordListに含まれていない場合は変換不可能
        if endWord not in wordList:
            return 0
        
        # wordListをsetに変換して高速な検索を可能にする
        word_set = set(wordList)
        
        # BFSのためのキュー（単語, 現在のステップ数）
        queue = deque([(beginWord, 1)])
        
        # 訪問済みの単語を記録
        visited = set([beginWord])
        
        while queue:
            current_word, steps = queue.popleft()
            
            # 目標の単語に到達した場合
            if current_word == endWord:
                return steps
            
            # 現在の単語の各文字を変更して隣接する単語を探す
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    # 同じ文字の場合はスキップ
                    if c == current_word[i]:
                        continue
                    
                    # 新しい単語を作成
                    new_word = current_word[:i] + c + current_word[i+1:]
                    
                    # 新しい単語がwordListに含まれ、まだ訪問していない場合
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, steps + 1))
        
        # 変換できない場合
        return 0

    def findLadder(beginWord, endWord, wordList):
        """
        Word Ladderの実際の経路を求める関数
        
        Args:
            beginWord: 開始単語
            endWord: 終了単語
            wordList: 使用可能な単語のリスト
        
        Returns:
            最短経路のリスト（変換できない場合は空のリスト）
        """
        if endWord not in wordList:
            return []
        
        word_set = set(wordList)
        
        # BFSのためのキュー（単語, 経路）
        queue = deque([(beginWord, [beginWord])])
        visited = set([beginWord])
        
        while queue:
            current_word, path = queue.popleft()
            
            if current_word == endWord:
                return path
            
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == current_word[i]:
                        continue
                    
                    new_word = current_word[:i] + c + current_word[i+1:]
                    
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, path + [new_word]))
        
        return []

# テスト実行
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    
    print(f"開始単語: {beginWord}")
    print(f"終了単語: {endWord}")
    print(f"使用可能な単語: {wordList}")
    print()
    
    # 最短経路の長さを求める
    length = ladderLength(beginWord, endWord, wordList)
    print(f"最短経路の長さ: {length}")
    
    # 実際の経路を求める
    path = findLadder(beginWord, endWord, wordList)
    if path:
        print(f"最短経路: {' -> '.join(path)}")
        print()
        print("変換過程:")
        for i in range(len(path) - 1):
            # どの文字が変更されたかを表示
            word1, word2 = path[i], path[i+1]
            for j in range(len(word1)):
                if word1[j] != word2[j]:
                    print(f"  {word1} -> {word2} (位置{j}: '{word1[j]}' -> '{word2[j]}')")
                    break
    else:
        print("変換経路が見つかりませんでした")
    
    print()
    print("=== 他のテストケース ===")
    
    # テストケース2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]  # "cog"を除外
    
    print(f"\nテスト2: {beginWord2} -> {endWord2}")
    print(f"使用可能な単語: {wordList2}")
    length2 = ladderLength(beginWord2, endWord2, wordList2)
    print(f"結果: {length2} (変換不可能)")
    
    # テストケース3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a","b","c"]
    
    print(f"\nテスト3: {beginWord3} -> {endWord3}")
    print(f"使用可能な単語: {wordList3}")
    length3 = ladderLength(beginWord3, endWord3, wordList3)
    path3 = findLadder(beginWord3, endWord3, wordList3)
    print(f"最短経路の長さ: {length3}")
    print(f"経路: {' -> '.join(path3)}")
