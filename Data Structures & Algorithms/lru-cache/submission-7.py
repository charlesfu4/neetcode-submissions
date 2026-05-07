class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {}
        # dummy head = LRU end, dummy tail = MRU end
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        node = self.hmap[key]
        self.remove(node)
        self.insert_tail(node)  # mark as most recent
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.remove(self.hmap[key])
        node = Node(key, value)
        self.hmap[key] = node
        self.insert_tail(node)
        if len(self.hmap) > self.capacity:
            lru = self.head.next   # least recent is just after dummy head
            self.remove(lru)
            del self.hmap[lru.key]