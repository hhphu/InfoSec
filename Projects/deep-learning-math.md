## Scalar
- A scalar is a single quantity that you can think of as a number.

```
x=5
```

## vector
- Vectors are arrays of numbers

```
x = np.array([1,2,3])
```

## Matrix
- Grids of information with rows and columns. We can index a matrix just like an array

```
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
```

## Tensor
- Data structure used in deep learning.
- Allows flexibility with the type of data we're using

![image](https://github.com/user-attachments/assets/8b365b11-8ba1-4c01-b86c-22b70ce3a610)

## Matrix Algebra
### Matrix Addition

![image](https://static-assets.codecademy.com/Courses/deeplearning-with-tensorflow/deep-learning-math/Matrix_B_v2.gif)

### Scalar multiplication

![image](https://content.codecademy.com/courses/deeplearning-with-tensorflow/deep-learning-math/Matrix_A.gif)

### Matrix multiplication

![image](https://content.codecademy.com/courses/deeplearning-with-tensorflow/deep-learning-math/Matrix_C.gif)

## Neural Networks Concept Overview
- Input layer: data point from dataset, which is fed into the model for training.
- Hidden layser: come between the input layer and the output layer, introducing complexity into our neural network and help with the learning process.
- Output layer: the ifnal layer in the neural network, producing the final result.
- Each layer contains nodes.
- Nodes between each layer are connected by weights (learning parameters in neural network, which determines the strength of the connection between the nodes)
- The weighted sum between nodes and weights is calculated between each layer

![image](https://github.com/user-attachments/assets/4160ac1e-26c5-4980-91fd-7ddf7754e993)

- It then applies activation function, which decides what is fired to the next neuron based on its calculation for the weighted sums.

  ![image](https://github.com/user-attachments/assets/fe717aeb-fbe5-4638-9fe0-7cc6f1565cb4)

- Various types of activation functions can be applied at each layer. ReLU, sigmoid and softmax are the popular ones.

![image](https://github.com/user-attachments/assets/ba33501c-bd7a-4840-a2dc-b8e3ef8afcd3)

![image](https://github.com/user-attachments/assets/e35c7fd9-3f06-43b5-91f1-d404706e38af)

## Loss Functions
- used to calculate the error (the predicted values vs the actual values).
- Mean squared error: best used for linear regression
- Cross-entropy: best used for classifications.

## Forwardpropagation vs Backpropagation
- Forwardpropagation: feeding input values through hidden layers to the final output layer.
- Backpropagation: computation of gradients (the rate of change with respect to the parameters of our loss function) with an algorithm know as gradient descent, which continuously updates and refines the weights between neurons to minimize loss function.
    - Determine how much each weight contributes to the loss function -> update the weight accordingly to reduce the error.
- Variants of Gradient descent: 
  - Stochastic Gradient Descent: a variation of Gradient descent, developed to cut back on computation time while accurate results by perfomring calculations on random points of data for each iteration.
  - Adam optimization algorithm: adaptive learning algoritm that finds individual learning rates for each parameters.
  - Mini-batch: similar to SGD but perform calculation on an fix-sized batch instead of one random data point.
