from ballClass import ball

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


trail = False

oliverJohn = ball("green")


# Animations function
# Runs every time the screen needs to be updated
# You need one argument for the function to operate properly
def animate(i):
    # Begins by clearing all previous information from the graph
    plt.cla()
    # Generate one random step for the ball class
    oliverJohn.step()
    # if trail is true draw the previous trail values
    if trail:
        plt.plot(oliverJohn.Xs, oliverJohn.Ys, color=oliverJohn.color)
    plt.plot(oliverJohn.Xs[-1], oliverJohn.Ys[-1], marker="o", markersize=8, markeredgecolor=oliverJohn.color, markerfacecolor=oliverJohn.color)
    plt.axis('equal')
    plt.axis([-300, 300, -300, 300])


fig, ax = plt.subplots()


# sets up the animation object
# plt.gcf() uses the current figure
# animate is the function that updates the data and graph
# interval is the time in milliseconds between frames
ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.show()