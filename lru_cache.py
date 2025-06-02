class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add_to_front(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

def main():
    lru = None
    print("Enter your commands (type 'exit;' to quit):")

    while True:
        command = input().strip()

        if command.lower() == "exit;" or command.lower() == "exit":
            break

        # Handle initialization: LRUCache lru(2);
        if command.startswith("LRUCache"):
            # Extract capacity inside parentheses
            import re
            match = re.search(r"LRUCache\s+\w+\((\d+)\);", command)
            if match:
                capacity = int(match.group(1))
                lru = LRUCache(capacity)
                print(f"LRU Cache initialized with capacity = {capacity}")
            else:
                print("Invalid LRUCache initialization. Example: LRUCache lru(2);")
            continue

        if lru is None:
            print("Please initialize LRUCache first, e.g., LRUCache lru(2);")
            continue

        # Parse put commands like: lru.put(1, 1);
        if command.startswith("lru.put"):
            import re
            match = re.search(r"lru\.put\((\d+),\s*(\d+)\);", command)
            if match:
                key = int(match.group(1))
                value = int(match.group(2))
                lru.put(key, value)
                print(f"put({key}, {value})")
            else:
                print("Invalid put command. Example: lru.put(1, 1);")
            continue

        # Parse get commands like: lru.get(1);
        if command.startswith("lru.get"):
            import re
            match = re.search(r"lru\.get\((\d+)\);", command)
            if match:
                key = int(match.group(1))
                value = lru.get(key)
                print(f"get({key}) -> {value}")
            else:
                print("Invalid get command. Example: lru.get(1);")
            continue

        print("Unknown command or invalid syntax.")

if __name__ == "__main__":
    main()
