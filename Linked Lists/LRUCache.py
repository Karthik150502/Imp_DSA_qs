class Dll():    
    def __init__(self, key, val):
        self.val, self.key = val, key
        self.prev = self.next = None

class LRUCache:
    def __init__(self, cap):
        self.cap = cap
        self.store = {}
        self.left, self.right = Dll(0,0), Dll(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev
        # Optional line of code
        node.prev = node.next = None

    def add(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt


    def get(self, key):
        if key in self.store:
            self.remove(self.store[key])
            self.add(self.store[key])
            return self.store[key].val     
        return -1
    

    def put(self, key, val):
        if key in self.store:
            self.remove(self.store[key])
        self.store[key] = Dll(key, val)
        self.add(self.store[key])


        if len(self.store) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.store[lru.key]





if __name__ == "__main__":


    obj = LRUCache(2)
    obj.put(1,1)
    obj.put(2,2)
    print(obj.get(1))
    obj.put(3,3)
    print(obj.get(2))
    obj.put(4,4)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))


