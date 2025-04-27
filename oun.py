import numpy as np
arr = np.array([1, 2, 3, 4, 5])
arr + 10  # Add 10 to each element
arr * 2   # Multiply each element by 2
np.mean(arr)  # Calculate mean
np.max(arr)   # Find maximum value
np.sum(arr)   # Sum all elements
arr.reshape(5, 1)  # Change the shape of an array
arr[0]    # Access the first element
arr[1:4]  # Get elements from index 1 to 3
arr[arr > 2]  # Get elements greater than 2
