import random

# Example input image 5x5
X = [[random.random() for _ in range(5)] for _ in range(5)]

# Simple 3x3 kernel
K = [[random.uniform(-1,1) for _ in range(3)] for _ in range(3)]

# Convolution function
def conv2d(X, K):
    h, w = len(X), len(X[0])
    kh, kw = len(K), len(K[0])
    out = [[0 for _ in range(w - kw + 1)] for _ in range(h - kh + 1)]
    for i in range(h - kh + 1):
        for j in range(w - kw + 1):
            out[i][j] = sum(X[i+ki][j+kj]*K[ki][kj] for ki in range(kh) for kj in range(kw))
    return out

conv_out = conv2d(X, K)

print("Input Image:")
for row in X: print(row)
print("\nConvolved Output:")
for row in conv_out: print(row)
