class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end = True            

    def search(self, word: str) -> bool:
        def dfs(i, node):
            cur = node
            for j in range(i, len(word)):
                if word[j] == '.':
                    for child in cur.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    if word[j] not in cur.children:
                        return False
                    cur = cur.children[word[j]]
            return cur.end
        return dfs(0, self.root)


                 
        
