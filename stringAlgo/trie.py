# trie algorithm (트라이 알고리즘)
# https://www.acmicpc.net/problem/14725 (개미굴)

## info
# https://rebro.kr/86
# https://cotak.tistory.com/3
# https://art-coding3.tistory.com/69
# https://www.geeksforgeeks.org/trie-insert-and-search/

"""
    트라이(Trie)란? : "트라이(Trie)"는 "retrieval"에서 나온 용어로, 주로 문자열 검색 트리로 사용된다.
"""

############################################################################################
############################################################################################
# https://www.acmicpc.net/problem/14725
class Trie:
    def __init__(self):
        self.root = {}
    
    def add(self, words):
        cur = self.root
        for word in words:
            if word not in cur:
                cur[word] = {}
            cur = cur[word]
        cur[0] = True
        
    def search(self, level, cur):
        if 0 in cur:
            return True
        cur_child = sorted(cur)
        
        for child in cur_child:
            print('--'*level + child)
            self.search(level+1, cur[child])
            
############################################################################################
############################################################################################
# GPT-4
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """Search for a word in the trie. Returns True if word exists."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """Returns True if there is any word in the trie that starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
############################################################################################
############################################################################################
    
if __name__ == '__main__':
    
    ########################################################################
    # 백준 14725번 개미굴
    n = int(input())
    trie = Trie()
    for i in range(n):
        data = list(input().split())[1:]
        trie.add(data)
    trie.search(0, trie.root)
    
    ########################################################################
    # GPT-4
    # 사용 예제:
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # True
    print(trie.search("app"))    # False
    print(trie.starts_with("app"))  # True
    trie.insert("app")
    print(trie.search("app"))    # True