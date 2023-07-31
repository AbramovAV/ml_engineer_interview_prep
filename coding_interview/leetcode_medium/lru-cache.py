class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.data = {}
        self.capacity = capacity
        self.start_node = ListNode(0, 0)
        self.end_node = ListNode(-1, -1)
        self.start_node.next = self.end_node
        self.end_node.prev = self.start_node

    def get(self, key: int) -> int:
        if key in self.data:
            value = self.data[key].val
            self.removeNode(self.data[key])
            self.addToEnd(self.data[key])
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.removeNode(self.data[key])
            self.data[key].val = value
            self.addToEnd(self.data[key])
        else:
            if len(self.data) == self.capacity:
                node = self.removeFromStart()
                del self.data[node.key]
            self.data[key] = ListNode(key, value)
            self.addToEnd(self.data[key])

    def addToEnd(self, node):
        node.prev = self.end_node.prev
        node.next = self.end_node
        self.end_node.prev.next = node
        self.end_node.prev = node

    def removeFromStart(self) -> ListNode:
        node = self.start_node.next
        self.start_node.next = node.next
        node.next.prev = self.start_node
        return node
    
    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)