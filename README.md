# Assignment (Roll no : 06)

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

## Daily Incremental Plan

Each network is implemented in a **Daily incremental style**, perfect for **daily commits**.

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

## Outputs
```text
Input Image:
 [[0.90822404 0.56461353 0.42628898 0.4719972  0.45229946]
 [0.05504475 0.8636851  0.09640296 0.25215308 0.18845811]
 [0.0179405  0.73995154 0.40918811 0.28526161 0.4869302 ]
 [0.84048067 0.7631993  0.27656566 0.71588113 0.00505578]
 [0.33560616 0.75012451 0.69424382 0.81154967 0.4159748 ]]
Convolved Output:
 [[2.61182371 2.52564036 1.98195118]
 [2.67027719 2.68046693 1.76663915]
 [2.40783623 3.41254427 2.72413848]]
ReLU Output:
 [[2.61182371 2.52564036 1.98195118]
 [2.67027719 2.68046693 1.76663915]
 [2.40783623 3.41254427 2.72413848]]
Pooled Output:
 [[2.68046693]]
 ```
 ```text
Epoch 1/100, Loss: 5.0044
Epoch 11/100, Loss: 4.2554
Epoch 21/100, Loss: 3.6406
Epoch 31/100, Loss: 3.1423
Epoch 41/100, Loss: 2.7415
Epoch 51/100, Loss: 2.4015
Epoch 61/100, Loss: 2.1209
Epoch 71/100, Loss: 1.8833
Epoch 81/100, Loss: 1.6893
Epoch 91/100, Loss: 1.5209
Epoch 100/100, Loss: 1.3933
```
**Training Plot** :

<img width="640" height="480" alt="image" src="https://github.com/AsmitaRawal/scratch-neural-networks--ML-/blob/main/CNN/images/cnn_forward_pass.png?raw=true" />


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

## Outputs
```text
Input: [[1, 0, 0], [0, 1, 0], [0, 0, 1]], Predicted: [[0.5163221]], Target: [1]
Input: [[0, 1, 0], [1, 0, 0], [0, 0, 1]], Predicted: [[0.51635021]], Target: [0]
```

```text
Epoch 1/200, Loss: 0.2549
Epoch 51/200, Loss: 0.2547
Epoch 101/200, Loss: 0.2546
Epoch 151/200, Loss: 0.2546
Epoch 200/200, Loss: 0.2546
```

```text
Predictions after training:
[[0.4954734]]
[[0.49549847]]
```
**Training Plot** :

<img width="640" height="480" alt="image" src="https://github.com/AsmitaRawal/scratch-neural-networks--ML-/blob/main/RNN/images/rnn_training_loss.png?raw=true" />



