import heapq
from collections import defaultdict, Counter
import random


def calculate_frequency(my_text):
    my_text = my_text.upper().replace(' ', '')
    frequency = dict(Counter(my_text)) # Count Letter and convert to dictionary i.e {'A': 3, 'B': 5, 'C': 6, 'D': 4, 'E': 2}
    return frequency


def build_heap(freq):
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap) # [[2, ['E', '']], [3, ['A', '']], [6, ['C', '']], [4, ['D', '']], [5, ['B', '']]]
    return heap


def build_tree(heap):
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0]


# freq = calculate_frequency("aaabbbbbccccccddddee")
freq = calculate_frequency("aaaaaabbbccdd")
heap = build_heap(freq)
tree = build_tree(heap)
sorted_data = sorted(tree[1:], key=lambda x: x[0])
print("Code word correspoding to symbols: ")
for pair in sorted_data:
    print(pair[0], '->', pair[1])
