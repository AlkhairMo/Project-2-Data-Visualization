import matplotlib.pyplot as plt

numbers = [1, 2, 3, 4, 5]
cubes = [x**3 for x in numbers]

fig, ax = plt.subplots()
ax.plot(numbers, cubes, linewidth=3)

# Set chart title and label axis
ax.set_title("Cubes Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubes of Values", fontsize=14)

# Set size of tick label
ax.tick_params(axis='both', labelsize=14)

plt.show()
