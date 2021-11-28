class MyHashSet:

    def __init__(self):
        self.buckets = []
    
    def hash(self, key: int) -> str:
        return chr(key)

    def add(self, key: int) -> None:
        val = self.hash(key)
        if val not in self.buckets:
            self.buckets.append(val)

    def remove(self, key: int) -> None:
        val = self.hash(key)
        if val in self.buckets:
            self.buckets.remove(val)

    def contains(self, key: int) -> bool:
        return self.hash(key) in self.buckets


class MyHashMap:

    def __init__(self):
        self.buckets = []
    
    @property
    def keys(self) -> list:
        return [x[0] for x in self.buckets]

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            index = 0
            for bucket in self.buckets:
                if bucket[0] == key:
                    self.buckets[index] = (key, value)
                    break
                index += 1
        else:
            self.buckets.append((key, value))

    def get(self, key: int) -> int:
        if key in self.keys:
            for bucket in self.buckets:
                if bucket[0] == key:
                    return bucket[1]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.keys:
            for bucket in self.buckets:
                if bucket[0] == key:
                    val = (bucket[0], bucket[1])
                    break
            self.buckets.remove(val)