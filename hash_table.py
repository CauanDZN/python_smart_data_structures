class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if not self.table[index]:
            self.table[index] = []
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        if self.table[index]:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

hash_table = HashTable(size=10)
hash_table.insert("name", "Alice")
hash_table.insert("age", 25)
hash_table.insert("city", "New York")

print("Name:", hash_table.get("name"))
print("Age:", hash_table.get("age"))
print("City:", hash_table.get("city"))
print("Country:", hash_table.get("country"))
