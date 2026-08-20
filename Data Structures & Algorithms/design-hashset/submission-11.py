class MyHashSet:

    hash_list = None

    def __init__(self):
        self.hash_list = [[] for _ in range(10)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hash_list[key%10].append(key)

    def remove(self, key: int) -> None:
        i = 0
        print(key%10)
        print(self.hash_list)
        while self.hash_list[key%10] and i < len(self.hash_list[key%10]):
            if self.hash_list[key%10][i] == key:
                self.hash_list[key%10].pop(i)
            i += 1

    def contains(self, key: int) -> bool:
        if self.hash_list[key%10]:
            for num in self.hash_list[key%10]:
                if num == key:
                    return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)