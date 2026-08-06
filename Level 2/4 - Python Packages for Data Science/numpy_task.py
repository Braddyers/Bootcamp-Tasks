# Import numpy package
import numpy as np

# Question 1
# Why doesn’t np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float) create 
# a two-dimensional (2D) array?

# Answer 1
# The above code doesn't create a 2D array because of the way the tuples 
# are passed to the np.array() function.   When you pass multiple arguments 
# to a function, they are treated as separate arguments, not as a 
# single argument.   So, in this case, you're passing four separate 
# arguments to the np.array() function: three tuples and a 
# dtype argument.   To create a 2D array, you need to pass a single 
# argument to the np.array() function.

# Here is the correct way:
x = np.array(((1, 0, 0), (0, 1, 0), (0, 0, 1)), dtype=float)
print(f"Answer 1: \n{x}\n")

# Question 2
# What is the difference between a = np.array([0, 0, 0]) 
# and a = np.array([[0, 0, 0]])?

# Answer 2
a = np.array([0, 0, 0])
print("\nAnswer 2 checks: \n")
print(f"a. Array: {a}")
print(f"Array shape: {a.shape}")
print(f"Array dimentions: {a.ndim}\n")
# Shape attribute is (3,), which indicates that there are three elements in 
# the array in one row.   ndim attribute is 1, which indicates that the 
# array is one-dimensional (1D).

a = np.array([[0, 0, 0]])
print(f"b. Array: {a}")
print(f"Array shape: {a.shape}")
print(f"Array dimentions: {a.ndim}\n")
# Shape attribute is (1, 3), which indicates two dimensions: 
# one row (with one element) and three columns.   ndim attribute is 2, which
# indicates that the array is 2D.

# Question 3
# A 3 by 4 by 4 array is created with
# arr = np.linspace(1, 48, 48).reshape(3, 4, 4).
# Index or slice this array to obtain the following:
# a. 20.0
# b. [ 9. 10. 11. 12.]
# c. [[33. 34. 35. 36.] [37. 38. 39. 40.] [41. 42. 43. 44.] [45. 46. 47. 48.]]
# d. [[5. 6.], [21. 22.] [37. 38.]]
# e. [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]
# f. [[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]
# g. [[1. 4.] [45. 48.]]
# h. [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], 
# [37. 38. 39. 40.]]

# Answer 3
arr = np.linspace(1, 48, 48).reshape(3, 4, 4)
print("\nAnswer 3 checks: \n")
print(f"Array in question:\n\n{arr}\n")

# a. 20.0
# Method 1:
# Select [second matrix, first row, fourth column].
answer = arr[1, 0, 3]
print(f"a. {answer}")
# Method 2:
# Flatten the array and selects value using new index number.
answer = arr.flatten()[19]
print(f"a. {answer}")

# b. [ 9. 10. 11. 12.]
# Method 1:
# Select [first matrix, third row].
answer = arr[0, 2]
print(f"\nb. {answer}")
# Method 2:
# Flattens array and selects relevant new indices.
answer = arr.flatten()[8:12]
print(f"b. {answer}")

# c. [[33. 34. 35. 36.] [37. 38. 39. 40.] [41. 42. 43. 44.] [45. 46. 47. 48.]]
# Method 1:
# Select [third matrix].
answer = arr[2]
print(f"\nc. {answer}")
# Method 2:
# Flatten array and reshape new indices into 4 by 4 array.
answer = arr.flatten()[32:48].reshape(4, 4)
print(f"c. {answer}")

# d. [[5. 6.], [21. 22.] [37. 38.]]
# Method 1:
# Select [all matrices, second row, first two columns].
answer = arr[:, 1, 0:2]
print(f"\nd. {answer}")
# Method 2:
# New indices of desired values of flattened array.
indices = [4, 5, 20, 21, 36, 37]
# Flatten array and reshape new indices into to a 3 by 2 array.
answer = arr.flatten()[indices].reshape(3, 2)
print(f"d. {answer}")

# e. [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]
# Method 1:
# Select [third matrix, all rows, last two columns in reverse].
answer = arr[2, :, -1:-3:-1]
print(f"\ne. {answer}")
# Method 2:
# New indices of desired values of flattened array.
indices = [35, 34, 39, 38, 43, 42, 47, 46]
# Flatten array and reshape it into a 4 by 2 array.
answer = arr.flatten()[indices].reshape(4, 2)
print(f"e. {answer}")

# f. [[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]
# Method 1:
answer = arr[:, :, 0][:, ::-1]
# [:, :, 0] means select [all matrices, all rows, first column].
# [:, ::-1] means select [all rows, (start at last column end, 
# end at last column, moving backwards by 1)].
print(f"\nf. {answer}")  
# Method 2:
# New indices of desired values of flattened array.
indices = [12, 8, 4, 0, 28, 24, 20, 16, 44, 40, 36, 32]
# Flatten array and reshape it into 3 by 4 array.
answer = arr.flatten()[indices].reshape(3, 4)
print(f"f. {answer}")         

# g. [[1. 4.] [45. 48.]]
# Method 1:
# New indices of desired values of flattened array.
indices = [0, 3, 44, 47]
# Flatten array and reshape it into 2 by 2 array.
answer = arr.flatten()[indices].reshape(2, 2)             
print(f"\ng. {answer}")
# Method 2:
indices = [arr[0, 0, 0], arr[0, 0, 3], arr[2, 3, 0], arr[2, 3, 3]]
answer = np.array(indices).reshape(2, 2)
print(f"g. {answer}")

# h. [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], 
# [37. 38. 39. 40.]]
# Method 1:
# Flatten array and reshape it into 4 by 4 array
answer = arr.flatten()[24:40].reshape(4, 4)
# Insert commas by tolist() function.
print(f"\nh. {answer.tolist()}")
# Method 2:
# Concatenate last two rows of matrix with index=1 and 
# first two rows of matrix with index=2.
answer = np.concatenate((arr[1, 2:4, :], arr[2, 0:2, :]))
print(f"h. {answer.tolist()}")