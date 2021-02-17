import numpy as np

def id(x):
	# This function returns the memory block address of an array. 
	return x.__array_interface__['data'][0]

# 1. Numpy exercises
# a) 
null_vector = np.zeros(shape = 10)
null_vector[4] = 1
print(null_vector)
print()

# b)
v_1 = 10
v_2 = 49 
ranged_vector = np.arange(start = v_1, stop = v_2 + 1 ) # exclusive end so add 1 to include 49
print(ranged_vector)
print()

# c)
random_vector = np.random.randint(low = 0, high = 10 + 1 , size = 5)
print("Before reversing random_vector:", random_vector)
random_vector = random_vector[::-1]
print("After reversing random_vector:", random_vector)
print()

# d) 
matrix_3_3 = np.arange(start = 0, stop = 8 + 1).reshape(3, 3)
print(matrix_3_3)
print()
# e)

input_vec = [1, 2, 0, 0, 4, 0]
input_vec_numpy = np.array(input_vec)
non_zeroes = np.where(input_vec_numpy != 0)
print("Non-zero indices:", non_zeroes)
print()

# f)
rand_vec = np.random.random(size = 30)
mean_rand_vec = np.mean(rand_vec)
print("Mean of random vector is:", mean_rand_vec)
print()

# g)
num_row = 4; num_col = 4
multi_arr = np.zeros(shape = (num_row, num_col))
multi_arr[:, 0] = 1; multi_arr[:, num_col - 1] = 1
multi_arr[0 , (0 + 1) : (num_col - 1)] = 1; multi_arr[num_row - 1, (0 + 1) : (num_col - 1)] = 1
print(multi_arr) 

# h) 
matrix_8_8 = np.zeros(shape = (8, 8) , dtype = np.int)
mat_1 = matrix_8_8.copy()
mat_1[1::2, ::2] = 1 
mat_1[::2, 1::2] = 1 
print("Checkerboard:\n", mat_1)
print()

# i)
mat_2 = np.array([[0, 1, 0, 1], [1, 0, 1, 0]])
mat_2_checkered = np.tile(mat_2, (8 // 2, 8 // 4))
print("Checkerboard using np.tile():\n", mat_2_checkered)
print()

# j)
Z = np.arange(11)
Z[np.where((Z > 3) & (Z < 8))] *= -1
print(Z)
print()

# k) Assuming we want to sort from low-to-high.... 
Z_2 = np.random.random(10)
Z_2 = np.sort(Z_2)
print("Sorted array:", Z_2)

# l)
A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
equal = np.array_equal(A, B)
print("A:\n", A)
print()
print("B:\n", B)
print()
print("A and B are equal:", equal)
print() 

# m) ID function taken day3.pdf lecture notes 
Z_3  = np.arange(10, dtype = np.int32)
print("ID before conversion:", id(Z_3))
print("Z_3 dtype:", Z_3.dtype)
Z_3 = Z_3.view(dtype = np.float32)
print("ID after in-place conversion:", id(Z_3))
print("Z_3 dtype after in-place conversion:", Z_3.dtype)
print()

# n)
A_2 = np.arange(9).reshape(3, 3)
B_2 = A_2 + 1
C = np.dot(A_2, B_2)
print(C)
D = np.diag(C) # Numpy built-in solution 
print(D)