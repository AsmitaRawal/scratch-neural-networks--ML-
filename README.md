# Scratch Implementation of Neural Networks (ANN, CNN, RNN)

This repository contains **from-scratch implementations of three neural network types** using only **Python built-ins** and optionally `matplotlib` for visualization:

- **Artificial Neural Network (ANN)**  
- **Convolutional Neural Network (CNN)**  
- **Recurrent Neural Network (RNN)**  

---

## Project Structure
scratch-neural-networks/
```
├── ann_scratch.py # ANN scratch implementation (XOR)
├── cnn_scratch.py # CNN scratch implementation
├── rnn_scratch.py # RNN scratch implementation
├── README.md # Project documentation
└── .gitignore
```
---

## 10-Day Incremental Plan

Each network is implemented in a **10-day incremental style**, perfect for **daily commits**.

### ANN (XOR Example)

| Day | Task |
|-----|------|
| 1   | Forward pass (compute hidden layer and output) |
| 2   | Training loop using backpropagation |
| 3   | Predictions after training |
| 4   | Add comments and explanations |
| 5   | Modularize training and forward functions |
| 6   | Implement loss computation function |
| 7   | Hyperparameter experiments |
| 8   | Visualization of training loss |
| 9   | Refactor code for clarity |
| 10  | Documentation & final README |

## Outputs
```text
Predictions after training
Input: [0, 0], Output: [0.019434699622773954]
Input: [0, 1], Output: [0.9833341290947769]
Input: [1, 0], Output: [0.983174959517643]
Input: [1, 1], Output: [0.017416279474971152]
```
**Training Plot** :

<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/1cdf5ca8-f8fa-4d45-b7bc-cf751c1b63fd" />


### CNN

| Day | Task |
|-----|------|
| 1   | Forward convolution on input |
| 2   | Apply ReLU activation |
| 3   | Apply max pooling |
| 4   | Add comments/explanations |
| 5   | Modularize CNN forward pass |
| 6   | Implement padding/stride helpers |
| 7   | Experiment with different kernel sizes |
| 8   | Visualize feature maps |
| 9   | Refactor code for clarity |
| 10  | Documentation & final README |

### RNN

| Day | Task |
|-----|------|
| 1   | Forward pass (compute hidden states & output) |
| 2   | Training loop using simple BPTT |
| 3   | Predictions after training |
| 4   | Add comments and explanations |
| 5   | Modularize training and forward functions |
| 6   | Implement loss computation function |
| 7   | Hyperparameter experiments |
| 8   | Visualization of training loss |
| 9   | Refactor code for clarity |
| 10  | Documentation & final README |

---


