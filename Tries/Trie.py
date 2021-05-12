# Python program for insert and search operations in a Trie
  
class TrieNode:
      
    def __init__(self):

        # Creates an array of length 26 for each letter in the alphabet
        self.children = [None]*26
  
        # isEndOfWord is True if the node represents the end of the word
        self.isEndOfWord = False
  
class Trie:
      
    def __init__(self):
        self.root = self.getNode()
  
    def getNode(self):
      
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
  
    def _charToIndex(self,ch):
          
        # private helper function
        # Converts a key's current character into an index
        # using only 'a' through 'z' and lower case
          
        return ord(ch)-ord('a')
  
  
    def insert(self,key):
          
        # If a key is not present, insert it into the trie
        # If the key is prefix of an existing key, mark it as the
        # end of a word.
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
  
            # If the current character is not present
            if not pCrawl.children[index]:

                # Return a new trie node (initialized to NULLs)
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
  
        # mark the last node as a leaf node
        pCrawl.isEndOfWord = True
  
    def search(self, key):
          
        # Search for a key in the trie
        # Returns true if a key is present, and false otherwise 
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # If we can't find the child node we're looking for, return false
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
  
        # The final node of the word must be marked as such
        return pCrawl != None and pCrawl.isEndOfWord
  
# driver function
def main():
  
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","anaswe","any",
            "by","their"]
    output = ["Not present in trie",
              "Present in trie"]
  
    # Trie object
    t = Trie()
  
    # Construct trie
    for key in keys:
        t.insert(key)
  
    # Search for different keys
    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))
  
if __name__ == '__main__':
    main()

# Output :
# the --- Present in trie
# these --- Not present in trie
# their --- Present in trie
# thaw --- Not present in trie