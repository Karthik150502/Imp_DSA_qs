class Trie():
    def __init__(self):
        self.children = [''] * 26
        self.isEndOfWord = False

    

    def insert(self,  word: str)-> None:
        currNode = self
        for i in range(len(word)):
            if not currNode.children[ord(word[i]) - ord('a')]:
                currNode.children[ord(word[i]) - ord('a')] = Trie()
            currNode = currNode.children[ord(word[i]) - ord('a')]
        currNode.isEndOfWord = True


    def search(self, word: str) -> bool:
        currNode = self
        for i in range(len(word)):
            if not currNode.children[ord(word[i]) - ord('a')]:
                return False
            currNode = currNode.children[ord(word[i]) - ord('a')]
        return currNode.isEndOfWord
    
    def startsWith(self, word)-> bool:
        currNode = self
        for i in range(len(word)):
            if not currNode.children[ord(word[i]) - ord('a')]: return False
            currNode = currNode.children[ord(word[i]) - ord('a')]
        

        return True

        

    def remove(self, key):
        
        curr = self

        
        for i in range(len(key)):
            curr = curr.children[ord(key[i]) - ord('a')]
            if not curr: 
                return False

        curr.isEndOfWord = False            
        return True