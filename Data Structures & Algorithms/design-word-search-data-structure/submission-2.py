"""
Understand:
    Input: add a word, search a word
    Ouput: None for adding a word, True if a word is in the datastructure, False

    - There will be all lowercase words, including .
    - There will be at most two dots .. 
    - A dot can be matched to any letter
    - The most number or characters in a word is 25

Match:
    - Tries - Hash tables

Planning:
    - Create a Trie Node class to store a dict of children and a end of word
    - To initialise the dict, create a single node as the root

    - To add words: 
        - Initialise a pointer to point to root
        - For each character in the string
            - If the character is not in the Trie:
                - Create a node for it
                - Add node as the value and the character as a key in the pionters hashmap
            - Advance the pointer to point to the charcter's node
        - Mark the end of the word here

    - Search: 
    - Initialize curr to point to the root node
    - For each character in the word to be searched: 
        - When we have a normal character   
            - Is the character a key in the children? No -> Return False
        - When we have a dot character
            - If the children dictionary is emtpy: return False
            - Generate a list of keys that this dict has
            - Index into a random number and set that as the next node
        - Advance the curr to point to child node 
    - Retrun the value of the end word value that marks the end of a word    

"""
class TrieNode:
    
    def __init__(self):
        self.end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word: 
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        
        def dfs(start, node):
            curr = node

            for i in range(start, len(word)):
                c = word[i] 
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else: 
                    if c not in curr.children:
                        return False

                    curr = curr.children[c]

            return curr.end

        return dfs(0, self.root)  

