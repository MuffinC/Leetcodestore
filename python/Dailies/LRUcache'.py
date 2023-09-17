class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        for x in range(capacity):
            self.store[x] = None
        # counter will be {0:0,1:0,2:0} for 3 elements, 0 being most recent

    def get(self, key: int) -> int:
        ans = -1
        for x, y in self.store.items():
            if y != None and y[0] == key:
                ans = y[1]

                hold = self.store[0]
                self.store[0] = (y[0], y[1])
                for x in range(1, len(self.store)):
                    cur = self.store[x]
                    self.store[x] = hold
                    hold = cur

        return ans

    def put(self, key: int, value: int) -> None:
        hold = self.store[0]
        self.store[0] = (key, value)

        for x in range(1, len(self.store)):
            cur = self.store[x]
            self.store[x] = hold
            hold = cur

