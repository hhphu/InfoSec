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

- It then applies activation function

  ![image](https://github.com/user-attachments/assets/fe717aeb-fbe5-4638-9fe0-7cc6f1565cb4)
