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
        v.append(res)

    listMax = max(len(l) for l in v)
    for i in range(n):
        if len(v[i]) != listMax:
            tmp = [0] * (listMax - len(v[i]))
            v[i] = tmp + v[i]
    res = []
    for i in range(listMax):
        res += [v[j][i] % 2 for j in range(n)]
    return res


message = list(map(int, input('Enter message: ').split()))
K = int(input('Constraints: '))
n = int(input('Number of output(generator): '))
print('Encoded Message', encode(message, K, n))

# message= 1 0 1 0 1
# K=4
# n=2
# g0= 1 1 1 1
# g1= 1 1 0 1
# Encoded Message: 1 1 1 1 0 1 0 0 0 1 0 0 1 0 1 1
