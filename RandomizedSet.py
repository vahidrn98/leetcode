from random import randint
class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.arr = []
        return None

    def insert(self, val: int) -> bool:
        try:
            if(self.set[val]):
                return False
            self.arr.append(val)
            return True
        except:
            self.set[val]=True
            return True
        

    def remove(self, val: int) -> bool:

        try:
            if(self.set[val]):
                return True
            return False
        except:
            return False

    def getRandom(self) -> int:
        keys = list(self.set.keys())
        return keys[randint(0,len(keys)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()