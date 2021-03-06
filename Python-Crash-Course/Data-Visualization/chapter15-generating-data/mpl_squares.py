import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_value, squares, linewidth = 3)

# set chart title and label axes.
plt.title(label="Square Numbers", fontsize = 24)
plt.xlabel(xlabel="Value", fontsize = 14)
plt.ylabel(ylabel="Square of value", fontsize = 14)

# set size of tick labels.
plt.tick_params(axis = "both", labelsize = 14)

plt.show()