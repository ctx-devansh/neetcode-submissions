class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.next = None

CAPACITY = 10000

class MyHashMap:

    def __init__(self):
        self.hash_map = [Node() for _ in range(CAPACITY)]

    def put(self, key: int, value: int) -> None:
        curr_head = self.hash_map[self.hash(key)]

        while curr_head.next:
            if curr_head.key == key:
                curr_head.value = value
                return
            curr_head = curr_head.next

        curr_head.key = key
        curr_head.value = value
        curr_head.next = Node()

    def get(self, key: int) -> int:
        curr_head = self.hash_map[self.hash(key)]

        while curr_head.next:
            if curr_head.key == key:
                return curr_head.value
            curr_head = curr_head.next
        return -1

    def remove(self, key: int) -> None:
        curr_head = self.hash_map[self.hash(key)]

        # If we need to change head
        if curr_head and curr_head.key == key:
            self.hash_map[self.hash(key)] = curr_head.next
            return


        # If something after head
        while curr_head.next:
            prev = curr_head
            curr_head = curr_head.next
            # if it is not the last element in linked list
            if curr_head.next is not None and curr_head.key == key:
                prev.next = curr_head.next
                return
            elif curr_head.next is None and curr_head.key == key:
                prev.next = None
                return
            

    
    def hash(self, key: int) -> int:
        return key % CAPACITY


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)