class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left, self.right = Node(0, 0), Node(0, 0) # left = LRU, right = MRU
        self.left.next, self.right.prev = self.right, self.left

        self.cache = {} # Node pointer

    # Removes a node from the list
    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Inserts a node to the list on most right (MRU)
    def insert_right(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        self.cache[node.key] = node
    
    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.insert_right(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.insert_right(node)

        # Capcity check
        if len(self.cache) > self.cap:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)        
        
        
