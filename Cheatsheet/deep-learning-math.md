# Deep Learning Math

- Scalars, vectors, matrices, and tensors- A scalar is a singular quantity like a number.
  - A vector is an array of numbers (scalar values).
  - A matrix is a grid of information with rows and columns.
  - A tensor is a multidimensional array and is a generalized version of a vector and matrix.

- Matrix Algebra
  - In scalar multiplication, every entry of the matrix is multiplied by a scalar value.
  - In matrix addition, corresponding matrix entries are added together.
  - In matrix multiplication, the dot product between the corresponding rows of the first matrix and columns of the second matrix is calculated.
  - A matrix transpose turns the rows of a matrix into columns.

- In forward propagation, data is sent through a neural network to get initial outputs and error values.
  - Weights are the learning parameters of a deep learning model that determine the strength of the connection between two nodes.
  - A bias node shifts the activation function either left or right to create the best fit for the given data in a deep learning model.
  - Activation Functions are used in each layer of a neural network and determine whether neurons should be “fired” or not based on output from a weighted sum.
  - Loss functions are used to calculate the error between the predicted values and actual values of our training set in a learning model.

- In backpropagation, the gradient of the loss function is calculated with respect to the weight parameters within a neural network.
  - Gradient descent updates our weight parameters by iteratively minimizing our loss function to increase our model’s accuracy.
  - Stochastic gradient descent is a variant of gradient descent, where instead of using all data points to update parameters, a random data point is selected.
  - Adam optimization is a variant of SGD that allows for adaptive learning rates.
  - Mini-batch gradient descent is a variant of GD that uses random batches of data to update parameters instead of a random datapoint.
