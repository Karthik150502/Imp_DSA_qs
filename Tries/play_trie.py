from Tries import Trie


trie = Trie()

trie.insert("karthikj")
trie.insert("kar")
trie.insert("apple")
trie.insert("maharaja")

trie.remove("apple")
trie.remove("kar")
trie.remove("maha")

word = "maha" 
res = trie.search(word)
print(res)
