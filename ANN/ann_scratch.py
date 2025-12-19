import math
import random

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Initialize weights randomly
def init_matrix(rows, cols):
    return [[random.uniform(-1, 1) for _ in range(cols)] for _ in range(rows)]

# XOR dataset
X = [[0,0],[0,1],[1,0],[1,1]]
y = [[0],[1],[1],[0]]

# Network architecture
input_size = 2
hidden_size = 2
output_size = 1

# Initialize weights and biases
W1 = init_matrix(input_size, hidden_size)   # input -> hidden
b1 = [0]*hidden_size
W2 = init_matrix(hidden_size, output_size)  # hidden -> output
b2 = [0]*output_size

# Forward pass (no training yet)
for sample in X:
    # Hidden layer
    hidden = [0]*hidden_size
    for j in range(hidden_size):
        hidden[j] = sigmoid(sum(sample[i]*W1[i][j] for i in range(input_size)) + b1[j])
    
    # Output layer
    output = [0]*output_size
    for j in range(output_size):
        output[j] = sigmoid(sum(hidden[i]*W2[i][j] for i in range(hidden_size)) + b2[j])
    
    print(f"Input: {sample}, Output: {output}")
