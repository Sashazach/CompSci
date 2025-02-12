# Imports the ball class from ball.py
from ballClass import ball

import matplotlib.pyplot as plt

iterations = 10

# Creates an instance of the ball class named oliverJohn
# The argument "blue" is passed to the "__init__" function
# No argument is needed for self
oliverJohn = ball("blue")

# Changes the color to "red" using the set color method
oliverJohn.setColor("red")

# generates a number of random steps equal to the number of iterations chosen above
for _ in range(iterations):
    oliverJohn.step()

# Creates an empty plot
fig, ax = plt.subplots()

# Plots the line
plt.plot(oliverJohn.Xs, oliverJohn.Ys, color=oliverJohn.color)

# Plots a dot at the end
plt.plot(oliverJohn.Xs[-1], oliverJohn.Ys[-1], marker="o", markersize=8, markeredgecolor=oliverJohn.color, markerfacecolor=oliverJohn.color)

# Formats the graph
# Use matplotlib documentation for other graph formatting options
plt.axis('equal')
plt.axis([-300, 300, -300, 300])

# Show the graph
plt.show()