class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # methods for dll
    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToTail(self, node: Node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key not in self.hmap:
            return -1
        node = self.hmap[key]
        self.remove(node)
        self.addToTail(node)
        return node.v

    def put(self, key, value):
        if key in self.hmap:
            self.remove(self.hmap[key])
        node = Node(key, value)
        self.hmap[key] = node
        self.addToTail(node)
        if len(self.hmap) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.hmap[lru.k]
            
    

