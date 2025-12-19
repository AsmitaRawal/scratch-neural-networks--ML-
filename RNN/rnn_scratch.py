import math
import random

# Input sequence
X = [0, 1, 0, 1]

# Initialize simple RNN weights
Wx = random.uniform(-1,1)  # input to hidden
Wh = random.uniform(-1,1)  # hidden to hidden
Wy = random.uniform(-1,1)  # hidden to output
bh = 0
by = 0

# Forward pass
h_prev = 0
for t in range(len(X)):
    h = math.tanh(Wx*X[t] + Wh*h_prev + bh)
    y = Wy*h + by
    print(f"Input {X[t]}, Hidden {h:.3f}, Output {y:.3f}")
    h_prev = h
