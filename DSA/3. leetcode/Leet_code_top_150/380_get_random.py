import random
class RandomizedSet(object):

    def __init__(self):
        self.my_set = []

    def insert(self, val):
        if val not in self.my_set:
            self.my_set.append(val)
            return True
        else:
            return False

    def remove(self, val):
        if val in self.my_set:
            self.my_set.remove(val)
            return True
        else:
            return False
        
    def getRandom(self):
        if len(self.my_set) == 1:
            return self.my_set[0]
        else:
            return random.choice(self.my_set)

        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()