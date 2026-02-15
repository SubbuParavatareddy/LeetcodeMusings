import random
class RandomizedSet:

    def __init__(self):
        self.indices_dict = {}
        self.val_arr = []

    def insert(self, val: int) -> bool:
        if val in self.indices_dict: return False
        self.val_arr.append(val)
        self.indices_dict[val] = len(self.val_arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices_dict: return False
        i = self.indices_dict[val]
        self.indices_dict[self.val_arr[-1]] = i
        self.val_arr[i] = self.val_arr[-1]
        self.indices_dict.pop(val)
        self.val_arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.val_arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()