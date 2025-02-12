from ballClass import ball

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

trail = False

# Creates an array of ball objects
# This array could be of any size
ballArray = [ball("blue", 0.02, 5, 2, 5, 0)]

def animate(i):
    plt.cla()

    # Iterates through each ball object and graphs each object individually
    # For each ball object, new positional data is generated and then the ball is replotted with that data
    for b in ballArray:
        b.step()
        if trail:
            plt.plot(b.Xs, b.Ys, color=b.color)
        plt.plot(b.Xs[-1], b.Ys[-1], marker="o", markersize=8, markeredgecolor=b.color, markerfacecolor=b.color)
    
    plt.axis('equal')
    plt.axis([0, 120, -15, 15])

# Creates the plot and the animation object
fig, ax = plt.subplots()
ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.show()