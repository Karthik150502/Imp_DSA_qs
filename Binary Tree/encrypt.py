import hashlib

hash1 = "468456848954"
hash2 = "468456848954"
res = hash1 + "-" + hash2
h = hashlib.new('sha-256')
h.update(b"Karthik J")
print(h.hexdigest())

"e0844408a127b88f7f9a97cc6be2a1f5511f494eba022df4e397159578e563dc"