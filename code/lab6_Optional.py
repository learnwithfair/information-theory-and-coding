import heapq
import math


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
       # L = sum (p(xi)*li) ; p(xi) = self/tolal; li=> codeword Length
        huffman_avg_length += (len(pair[1]) * (freq[pair[0]] / length))        
    return huffman_avg_length


def entropy(freq, length):
    H = 0
    P = [fre / length for _, fre in freq.items()]
    # P = [1/2,1/4,1/8,1/8]   
    for x in P:
        H += -(x * math.log2(x))
    return H



# freq = {'A': 6, 'B': 3, 'C': 2, 'D': 2}
freq = {'A': 5, 'B': 9, 'C': 12, 'D': 13,'E': 16,'F': 45}
lenght = sum(freq.values())
heap = build_heap(freq)
tree = build_tree(heap)
# tree=[20, ['D', '0'], ['B', '01'], ['E', '100'], ['A', '101'], ['C', '11']] not optimal
huffman_avg_length = compute_huffman_avg_length(freq, tree, lenght)
H = entropy(freq, lenght)
print("The average codeword length, L : %.2f bits" % huffman_avg_length)
print('Entropy : %.2f bits' % H)
if huffman_avg_length >= H:
    print("Huffman code is optimal. i.e (L>=H(x))")
else:
    print("Code is not optimal")

# Sort the list of lists based on the first element of each sublist
sorted_data = sorted(tree[1:], key=lambda x: x[0])
print("Code word correspoding to symbols: ")
for pair in sorted_data:
    print(pair[0], '->', pair[1])