class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        # Set a pointer to point to the root of the trie
        curr = self.root

        # Iterate over each of the characters in the word
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode()
            
            curr = curr.children[word[i]]   
        curr.end = True 

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word: 
            if c not in curr.children:
                return False

            curr = curr.children[c]

        return curr.end
         
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            
            curr = curr.children[c]
        
        return True
        