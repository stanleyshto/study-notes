import numpy as np

#define array
array_a = np.array([1,3,5])
array_b = np.array([2,4,6])
array_c = np.array([[3,3,3],[4,4,4]])
array_d = np.array([[1,1,1],[2,5,6]])

# arithmatic operation +, -, * ,/
print(array_a + array_b) # [3 7 11]
print(array_a - array_b) # [-1 -1 -1]
print(array_a * array_b) # [2 12 30]
print(array_a / array_b) # [0.5 0.75 0.83333333]
print(array_c + array_d) # [[ 4  4  4] [ 6  9 10]]
print(array_a + 2) # [3 5 7]

# get dimension
print(f"Dimension of array_a : {array_a.ndim}") # Dimension of array_a : 1
print(f"Dimension of array_c : {array_c.ndim}") # Dimension of array_c : 2

# get shape
print(f"Shape of array_a : {array_a.shape}") # Shape of array_a : (3,)
print(f"Shape of array_c : {array_c.shape}") # Shape of array_c : (2, 3)

# get type
print(f"Data type of array_c : {array_c.dtype}") # Data type of array_c : int32

# get item size
print(f"item size of array_c : {array_c.itemsize} bytes") # item size of array_c : 4 bytes

# get total number of elements
print(f"Number of elements in array_c : {array_c.size}") # Number of elements in array_c : 6

# get a specific element. Use the convention [row, column]
array_e = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(array_e[1,5]) # 13  It is because row and column are counted from 0
print(array_e[1,-2]) # 13  negative number means counting from the back. column -2 = column 5 = 13
# get a specific row
print(array_e[1,:]) # [ 8  9 10 11 12 13 14], ':' stands for all entries
# get a specific column
print(array_e[:,2]) # [ 3 10]

# assign values to array
print(np.zeros((3,2))) # array 3 * 2 fill with all zeros
print(np.ones((5,2,2))) # array 5 * 2 * 2 fill with all ones
print(np.full((2,2),99)) # array 2 * 2 fill with a specific number, say 99
print(np.full_like(array_e, 4)) # array with shape the same as array_e, all entries value = 4
print(np.random.rand(4,2)) # array 4 * 2 fill with random value between 0 to 1
print(np.random.randint(2, 10, (4,2))) # array 4 * 2 with randam integer between 2 (inclusive) to 10 (exclusive)
print(np.identity(5)) # identity matrix of a 5 * 5 array 

# copy array
array_X1 = np.ones((3,3))
array_X1_content = array_X1.copy()  # Copy the content
array_X1_addr = array_X1            # Copy the address
array_X1[1,1] = 0
print(f"Value of array_X1 :\n {array_X1}")
print(f"Value of array_X1_content :\n {array_X1_content}")
print(f"Value of array_X1_addr :\n {array_X1_addr}")

# Linear Algebra
a = np.array([[1,3,4],[2,4,3]])
b = np.array([[5,4],[2,3],[1,9]])
print(f"Matrix Multiplication : \n{np.matmul(a,b)}")

# Reorganize Array
a = np.ones((4,4))
b = a.reshape(2,8)
print(b)

