# Python Data Structures – LRU Cache & Custom HashMap

This repository contains Python solutions for two classic data structure design problems.

---

## 📌 Question 1 – LRU Cache

**Problem**:  
Design and implement a Least Recently Used (LRU) Cache. A cache has a fixed capacity, and when it exceeds that capacity, it must evict the least recently used item to make space for the new one.

**Required Operations**:
- `get(key)`: Return the value of the key if it exists, otherwise -1.
- `put(key, value)`: Insert or update the key. Evict if the cache exceeds capacity.

**Constraints**:
- All operations must run in O(1) time.
- 1 ≤ capacity ≤ 3000
- 0 ≤ key, value ≤ 10⁴

🗂️ Code: [`lru_cache.py`](./lru_cache.py)

---

## 📌 Question 2 – Custom HashMap

**Problem**:  
Implement a simplified version of a HashMap without using built-in hash tables (`dict`, `unordered_map`, etc).

**Required Operations**:
- `put(key, value)`: Insert or update the value.
- `get(key)`: Return the value if exists, otherwise -1.
- `remove(key)`: Delete the key from map.

**Constraints**:
- 0 ≤ key, value ≤ 10⁶
- Up to 10⁵ operations

🗂️ Code: [`my_hashmap.py`](./my_hashmap.py)
