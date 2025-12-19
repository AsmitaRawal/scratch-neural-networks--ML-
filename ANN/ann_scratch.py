import math
import random

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def init_matrix(rows, cols):
    return [[random.uniform(-1,1) for _ in range(cols)] for _ in range(rows)]

X = [[0,0],[0,1],[1,0],[1,1]]
y = [[0],[1],[1],[0]]

input_size = 2
hidden_size = 2
output_size = 1

W1 = init_matrix(input_size, hidden_size)
b1 = [0]*hidden_size
W2 = init_matrix(hidden_size, output_size)
b2 = [0]*output_size

def forward_pass(x):
    hidden = [0]*hidden_size
    for i in range(hidden_size):
        s = sum(x[j] * W1[j][i] for j in range(input_size)) + b1[i]
        hidden[i] = sigmoid(s)
    out = [0]*output_size
    for i in range(output_size):
        s = sum(hidden[j] * W2[j][i] for j in range(hidden_size)) + b2[i]
        out[i] = sigmoid(s)
    return out

for sample in X:
    print(f"Input: {sample} -> Output: {forward_pass(sample)}")
