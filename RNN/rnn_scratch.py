import math
import random

X = [0,1,0,1]

Wx = random.uniform(-1,1)
Wh = random.uniform(-1,1)
Wy = random.uniform(-1,1)
bh = 0
by = 0

h_prev = 0
for t in range(len(X)):
    h = math.tanh(Wx*X[t] + Wh*h_prev + bh)
    y_pred = Wy*h + by
    print(f"Input {X[t]} -> Hidden {h:.3f} -> Output {y_pred:.3f}")
    h_prev = h
