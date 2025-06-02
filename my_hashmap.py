class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 10007
        self.buckets = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = Node(key, value)
            return
        curr = self.buckets[index]
        while True:
            if curr.key == key:
                curr.value = value
                return
            if curr.next is None:
                break
            curr = curr.next
        curr.next = Node(key, value)

    def get(self, key):
        index = self._hash(key)
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key):
        index = self._hash(key)
        curr = self.buckets[index]
        prev = None
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.buckets[index] = curr.next
                return
            prev = curr
            curr = curr.next

def main():
    import re
    hashmap = None
    print("Enter commands (type 'exit;' to quit):")

    while True:
        line = input().strip()
        if line.lower() == "exit;" or line.lower() == "exit":
            break
        if not line:
            continue

        # Initialization line: MyHashMap obj;
        if hashmap is None:
            if re.match(r"MyHashMap\s+\w+;", line):
                hashmap = MyHashMap()
                print("MyHashMap initialized.")
                continue
            else:
                print("Please initialize MyHashMap first, e.g. 'MyHashMap obj;'")
                continue

        # Remove trailing semicolon
        if line.endswith(";"):
            line = line[:-1]

        # Match put: obj.put(1, 10)
        m_put = re.match(r"\w+\.put\((\d+),\s*(\d+)\)", line)
        if m_put:
            key = int(m_put.group(1))
            value = int(m_put.group(2))
            hashmap.put(key, value)
            continue

        # Match get: obj.get(1)
        m_get = re.match(r"\w+\.get\((\d+)\)", line)
        if m_get:
            key = int(m_get.group(1))
            val = hashmap.get(key)
            print(val)
            continue

        # Match remove: obj.remove(2)
        m_remove = re.match(r"\w+\.remove\((\d+)\)", line)
        if m_remove:
            key = int(m_remove.group(1))
            hashmap.remove(key)
            continue

        print("Invalid command or syntax.")

if __name__ == "__main__":
    main()
