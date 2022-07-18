import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[0, 0, 1],
                            [0, 1, 1],
                            [1, 0, 1],
                            [1, 1, 1]])

training_outputs = np.array([[0, 0, 1, 1]]).T

np.random.seed(1)
synaptic_weights = 2 * np.random.random((3, 1)) - 1

print('Random starting synaptic weights: ')
print(synaptic_weights)

for iteration in range(20000000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    error = training_outputs - outputs

    adjustments = error * sigmoid(outputs * (1 - outputs))

    synaptic_weights += np.dot(input_layer.T, adjustments)

print('Synaptic weights after training: ')
print(synaptic_weights)


print('Output after training: ')
print(outputs)