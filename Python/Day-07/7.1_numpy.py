import numpy as np
#1.create an array
numbers = np.array([10, 20, 30, 40, 50])

print(numbers)

#2.Array information
print("Shape:", numbers.shape)
print("Dimention:", numbers.ndim)
print("Size:", numbers.size)
print("Data Type:", numbers.dtype)

#3.2d Array
import numpy as np

matrix = np.array([[1, 2, 3],
                  [4, 5, 6]])
print(matrix)
print("Shape:", matrix.shape)

#4.Indexing
numbers = np.array([10, 20, 30, 40, 50])
print(numbers[0])
print(numbers[2])
print(numbers[-1])

#5.Mathematical operations
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))