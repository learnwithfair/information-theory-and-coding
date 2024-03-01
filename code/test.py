import numpy as np


def encode(msg, K, n):
    g, v = [], []
    for i in range(n):
        sub_g = list(map(int, input(f'Enter bits for generator {i}: ').split()))
        if len(sub_g) != K:
            raise ValueError(f'You entered {len(sub_g)} bits.\n need to enter {K} bits')
        g.append(sub_g)
    for i in range(n):
        res = list(np.poly1d(g[i]) * np.poly1d(msg))
        print 
        print("res",res)
        v.append(res)
        print(v)

    listMax = max(len(l) for l in v)
    print("listMax",listMax)
    for i in range(n):
        if len(v[i]) != listMax:
            tmp = [0] * (listMax - len(v[i]))
            v[i] = tmp + v[i]
    res = []
    for i in range(listMax):
        res += [v[j][i] % 2 for j in range(n)]
        print("res",res)
    return res


message = list(map(int, "1 0 1 0 1".split()))
K = 4
n = 2
print('Encoded Message', encode(message, K, n))

# message= 1 0 1 0 1
# K=4  = m+1 here, m = no of shift register
# n=2 n= no of modulo-2 adder
# g0= 1 1 1 1 Upper
# g1= 1 1 0 1 Lower
# Encoded Message: 1 1 1 1 0 1 0 0 0 1 0 0 1 0 1 1
