import numpy as np


def encode(msg, K, n):
    g, v = [], []
    for i in range(n):
        sub_g = list(map(int, input(f'Enter bits for generator {i}: ').split()))
        if len(sub_g) != K:
            raise ValueError(f'You entered {len(sub_g)} bits.\n need to enter {K} bits')
        g.append(sub_g)
    for i in range(n):
        res = list(np.poly1d(g[i]) * np.poly1d(msg)) # 1 1 0 0 0 0 1 1 and 1 1 1 0 1 0 0 1
        v.append(res)

    listMax = max(len(l) for l in v) # 1 1 0 0 0 0 1 1 = 8
    for i in range(n):
        if len(v[i]) != listMax:
            tmp = [0] * (listMax - len(v[i])) # Fill Up same len
            v[i] = tmp + v[i]
    
    # Print U1(x) and U2(x)
    print("Answer: ")
    print("-"*50)
    result = [[element % 2 for element in sublist] for sublist in v]
    print("u1(x) : ",result[0])
    print("u2(x) : ",result[1])
    
    res = []
    for i in range(listMax):
        res += [v[j][i] % 2 for j in range(n)]
    return res


message = list(map(int, input('Enter message: ').split()))
K = int(input('Constraints: '))
n = int(input('Number of output(generator): '))
print('Encoded Message', encode(message, K, n))

# message= 1 0 1 0 1
# K=4  = m+1 here, m = no of shift register
# n=2 n= no of modulo-2 adder
# g0= 1 1 1 1 Upper
# g1= 1 1 0 1 Lower
# Encoded Message: 1 1 1 1 0 1 0 0 0 1 0 0 1 0 1 1
