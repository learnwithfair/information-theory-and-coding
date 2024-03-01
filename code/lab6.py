import heapq
import math
from collections import Counter


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


def compute_huffman_avg_length(freq, tree, length):
    huffman_avg_length = 0
    for pair in tree[1:]:
        print(pair)
        huffman_avg_length += (len(pair[1]) * (freq[pair[0]] / length))
        print(huffman_avg_length)
    return huffman_avg_length


def entropy(freq, length):
    H = 0
    P = [fre / length for _, fre in freq.items()]
    for x in P:
        H += -(x * math.log2(x))
    return H


# message = "aaabbbbbccccccddddee"
message = "aaaaaabbbccdd"
# freq = calculate_frequency(message)
freq = {'A': 6, 'B': 3, 'C': 2, 'D': 2}

heap = build_heap(freq)
tree = build_tree(heap)
# tree=[20, ['D', '0'], ['B', '01'], ['E', '100'], ['A', '101'], ['C', '11']] not optimal
huffman_avg_length = compute_huffman_avg_length(freq, tree, len(message))
H = entropy(freq, len(message))
print("Huffman : %.2f bits" % huffman_avg_length)
print('Entropy : %.2f bits' % H)
if huffman_avg_length >= H:
    print("Huffman code is optimal")
else:
    print("Code is not optimal")
