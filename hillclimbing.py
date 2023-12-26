import matplotlib.pyplot as plt
import numpy as np

# Define the mathematical function
def function(x):
    return -x**2 + 4*x

# Hill climbing algorithm to find the maximum
def hill_climbing(starting_point, step_size, iterations):
    current_x = starting_point
    for _ in range(iterations):
        next_x = current_x + step_size
        if function(next_x) > function(current_x):
            current_x = next_x
        else:
            break
    return current_x

# Visualization of the function
x_values = np.linspace(-1, 5, 100)
y_values = function(x_values)

plt.plot(x_values, y_values, label="f(x) = -x^2 + 4x")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Hill Climbing Algorithm: Maximum of f(x)')
plt.legend()

# Run hill climbing algorithm
starting_point = 0.0
step_size = 0.1
iterations = 50
max_x = hill_climbing(starting_point, step_size, iterations)

# Mark the maximum point on the plot
plt.scatter(max_x, function(max_x), color='red', label=f'Maximum: x={max_x:.2f}, f(x)={function(max_x):.2f}')
plt.legend()

# Show the plot
plt.show()
