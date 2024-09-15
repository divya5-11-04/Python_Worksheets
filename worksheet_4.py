

#Work Sheet 4: NumPy Basics 

import numpy as np

# Question 1: Array Creation
# 1.1 Create a 1D array of integers from 5 to 25
array_1d = np.arange(5, 26)
print("1D array:", array_1d)

#1.2 Create a 2D array with 3 rows and 4 columns filled with random integers between 10 and 50. 

array_2d = np.random.randint(10, 50, size=(3, 4))
print("\n2D array:\n", array_2d)
#QuesƟon 2: Array AƩributes 
#2.1 For the 1D array created in QuesƟon 1.1, find, and print its:
# Shape 
# Size 
# Data type 
print("\n1D array shape:", array_1d.shape)
print("1D array size:", array_1d.size)
print("1D array data type:", array_1d.dtype)
#2.2 For the 2D array created in QuesƟon 1.2, find, and print its:
# Shape 
# Size 
# Data type 
print("\n2D array shape:", array_2d.shape)
print("2D array size:", array_2d.size)
print("2D array data type:", array_2d.dtype)

#QuesƟon 3: Array OperaƟons 
#3.1 Create two 1D arrays: 
# Array1: [2, 4, 6, 8, 10] 
# Array2: [1, 3, 5, 7, 9] 

array1 = np.array([2, 4, 6, 8, 10])
array2 = np.array([1, 3, 5, 7, 9])

#3.2 Perform the following operaƟons and print the results:
# AddiƟon
# SubtracƟon
# Element-wise mulƟplicaƟon
# Element-wise division 
print("\nAddition:", array1 + array2)
print("Subtraction:", array1 - array2)
print("Element-wise multiplication:", array1 * array2)
print("Element-wise division:", array1 / array2)

#QuesƟon 4: BroadcasƟng 
#4.1 Create a 2D array of shape (3, 3) with values starƟng from 1 to 9. 
#4.2 Using broadcasƟng, mulƟply this 2D array by a scalar value of 5. Print the result.

array_broadcast = np.arange(1, 10).reshape(3, 3)
print("\nOriginal 2D array:\n", array_broadcast)

#QuesƟon 5: 
# 5.1 Create a 2D array of shape (4, 4) with values ranging from 10 to 25
array_2d = np.arange(10, 26).reshape(4, 4)
print("Original 2D array:\n", array_2d)

# 5.2 Extract the second row and the last column of the array
second_row = array_2d[1, :]  # Index 1 for the second row
last_column = array_2d[:, -1]  # Index -1 for the last column

print("Second row:", second_row)
print("Last column:", last_column)

# 5.3 Replace the elements of the first row with zeros
array_2d[0, :] = 0  # Index 0 for the first row and set all elements to 0

print("Array after replacing the first row with zeros:\n", array_2d)

#QuesƟon 6: Boolean Indexing 

# 6.1 Create a 1D array with random integers between 20 and 40 (10 elements)
array_1d = np.random.randint(20, 40, size=10)
print("Original 1D array:", array_1d)

# 6.2 Use Boolean indexing to find all elements greater than 30
greater_than_30 = array_1d[array_1d > 30]
print("Elements greater than 30:", greater_than_30)

#QuesƟon 7: Reshaping 
# 7.1 Create a 1D array with 12 elements starting from 11
array_1d = np.arange(11, 23)  # Elements from 11 to 22
print("Original 1D array:", array_1d)

# 7.2 Reshape it into a 2D array of shape (3, 4)
array_reshaped = array_1d.reshape(3, 4)
print("Reshaped 2D array (3x4):\n", array_reshaped)

#QuesƟon 8: Matrix OperaƟons 
# 8.1 Create two 2x2 matrices: Matrix A and Matrix B
matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", matrix_A)
print("Matrix B:\n", matrix_B)

# 8.2 Perform Matrix multiplication
matrix_multiplication = np.dot(matrix_A, matrix_B)
print("Matrix Multiplication of A and B:\n", matrix_multiplication)

# 8.2 Transpose of Matrix A
transpose_A = np.transpose(matrix_A)
print("Transpose of Matrix A:\n", transpose_A)



#QuesƟon 9: StaƟsƟcal FuncƟons 
# 9.1 Create a 1D array with random integers between 10 and 60 (15 elements)
array_1d_random = np.random.randint(10, 60, size=15)
print("1D array with random integers:", array_1d_random)

# 9.2 Compute and print statistics: Mean, Median, and Standard Deviation
mean_value = np.mean(array_1d_random)
median_value = np.median(array_1d_random)
std_deviation = np.std(array_1d_random)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_deviation}")

#QuesƟon 10: Linear Algebra 

# 10.1 Create a 3x3 matrix A
matrix_A = np.array([[2, 1, 3],
                     [0, 5, 6],
                     [7, 8, 9]])

print("Matrix A:\n", matrix_A)

# 10.2 Find the determinant of matrix A
determinant = np.linalg.det(matrix_A)
print(f"Determinant of matrix A: {determinant:.2f}")

# 10.2 Compute the inverse of matrix A (if the determinant is non-zero)
if determinant != 0:
    inverse_A = np.linalg.inv(matrix_A)
    print("Inverse of matrix A:\n", inverse_A)
else:
    print("Matrix A is singular and cannot be inverted.")

# 10.2 Find the eigenvalues and eigenvectors of matrix A
eigenvalues, eigenvectors = np.linalg.eig(matrix_A)
print("Eigenvalues of matrix A:", eigenvalues)
print("Eigenvectors of matrix A:\n", eigenvectors)
