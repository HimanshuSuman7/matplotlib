import random
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation

plt.rcdefaults()

x_val = []
y_val = []
index = count()


def animate(i):
    x_val.append(next(index))
    y_val.append(random.randint(0, 5))

    plt.cla()
    plt.grid(True)
    plt.plot(x_val, y_val)


anim = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()
