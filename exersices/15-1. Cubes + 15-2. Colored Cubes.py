import matplotlib.pyplot as plt

numbers = range(1, 5001)
cubes = [x**3 for x in numbers]

fig, ax = plt.subplots()
ax.scatter(numbers, cubes, s=3, c=cubes, cmap=plt.cm.Reds)

# Set chart title and label axis
ax.set_title("Cubes Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubes of Values", fontsize=14)

# Set size of tick label and axis' rang
ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 5100, 0, 130000000000])

plt.show()
