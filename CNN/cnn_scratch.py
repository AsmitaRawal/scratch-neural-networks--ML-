import random

X = [[random.random() for _ in range(5)] for _ in range(5)]
K = [[random.random() for _ in range(3)] for _ in range(3)]

def conv2d(X, K):
    h, w = len(X), len(X[0])
    kh, kw = len(K), len(K[0])
    out = [[0 for _ in range(w - kw + 1)] for _ in range(h - kh + 1)]
    for i in range(h - kh + 1):
        for j in range(w - kw + 1):
            s = sum(X[i+ki][j+kj]*K[ki][kj] for ki in range(kh) for kj in range(kw))
            out[i][j] = s
    return out

output = conv2d(X,K)
for row in output:
    print(row)
