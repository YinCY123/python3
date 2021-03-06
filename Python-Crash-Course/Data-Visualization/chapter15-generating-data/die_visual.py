from die import Die
import pygal

# create a D6
die_1 = Die()
die_2 = Die(num_sides = 10)

# make some rools, and store results in a list.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the results
max_result = die_1.num_sides + die_2.num_sides
frequencies = []
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = list(range(2, max_result + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add(title = "D6", values=frequencies)
hist.render_to_file(filename="die_visual.svg")

print(results)
print(frequencies)