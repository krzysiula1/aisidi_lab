from re import L
from heap import Heap
import random

def test_heap_2():
    values = random.sample(range(30_000), 10_001)
    heap = Heap(2)
    for value in values:
        heap.insert(value)

    for i in range(10_000, 1, -1):
        assert(heap.values[i] < heap.values[(i-1)//2])

def test_heap_3():
    values = random.sample(range(30_000), 10_001)
    heap = Heap(3)
    for value in values:
        heap.insert(value)

    for i in range(10_000, 1, -1):
        assert(heap.values[i] < heap.values[(i-1)//3])

def test_heap_4():
    values = random.sample(range(30_000), 10_001)
    heap = Heap(4)
    for value in values:
        heap.insert(value)

    for i in range(10_000, 1, -1):
        assert(heap.values[i] < heap.values[(i-1)//4])


def test_heap_remove_2():
    values = random.sample(range(30_000), 10_001)
    heap = Heap(2)
    for value in values:
        heap.insert(value)
    for i in range(5_000):
        heap.remove_top()
    for i in range(5_000, 1, -1):
        assert(heap.values[i] < heap.values[(i-1)//2])

def test_heap_remove_3():
    values = random.sample(range(30_000), 10_001)
    heap = Heap(3)
    for value in values:
        heap.insert(value)
    for i in range(5_000):
        heap.remove_top()
    for i in range(5_000, 1, -1):
        assert(heap.values[i] < heap.values[(i-1)//3])

def test_heap__remove_4():
    values = random.sample(range(30_000), 10_001)
    heap = Heap(4)
    for value in values:
        heap.insert(value)
    for i in range(5_000):
        heap.remove_top()
    for i in range(5_000, 1, -1):
        assert(heap.values[i] < heap.values[(i-1)//4])
    

