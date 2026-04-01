class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lmap = dict()
        self.linkCapacity = []
        self.current_capacity = 0

    def get(self, key: int) -> int:
        if key in self.lmap:
            # Move the accessed key to the end to show that it was recently used
            self.linkCapacity.remove(key)
            self.linkCapacity.append(key)
            return self.lmap[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lmap:
            self.lmap[key] = value
            # Move the updated key to the end to show that it was recently used
            self.linkCapacity.remove(key)
            self.linkCapacity.append(key)
        else:
            if self.current_capacity < self.capacity:
                self.lmap[key] = value
                self.linkCapacity.append(key)
                self.current_capacity += 1
            else:
                leastKey = self.linkCapacity.pop(0)
                self.lmap.pop(leastKey)
                self.lmap[key] = value
                self.linkCapacity.append(key)

