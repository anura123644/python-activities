import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Creating a basic line plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Matplotlib Visualization')
plt.legend()
plt.show()

