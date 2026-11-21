"""Task 9 (Hard): Least Recently Used Cache

Implement an LRU cache with a positive capacity.
get(key) returns its value, or -1 if missing. A successful get marks the
key as most recently used. A missing get does not change usage order.
put(key, value) inserts or updates a value and marks it most recently used.
If insertion exceeds capacity, evict the least recently used key.

Example for capacity=2:
    put(1, 10), put(2, 20), get(1) -> 10
    put(3, 30) evicts key 2; get(2) -> -1

Constraints: capacity >= 1; integer keys; values >= 0; up to 100_000 calls.
Target: O(1) average time per get/put and O(capacity) space.
Do not use OrderedDict or a third-party cache implementation.
"""


class LRUCache:
    def __init__(self, capacity: int):...

    def get(self, key: int) -> int:...

    def put(self, key: int, value: int) -> None:...


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    assert cache.get(1) == 10
    cache.put(3, 30)
    assert cache.get(2) == -1
    cache.put(1, 15)
    cache.put(4, 40)
    assert cache.get(3) == -1
    assert cache.get(1) == 15
    assert cache.get(4) == 40

    single = LRUCache(1)
    assert single.get(99) == -1
    single.put(5, 0)
    assert single.get(5) == 0
    single.put(6, 60)
    assert single.get(5) == -1
    assert single.get(6) == 60
    print("All sample checks passed!")
