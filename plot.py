import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pyModbusTCP.client import ModbusClient
import os
import sys

reg1 = []
reg2 = []
index = []

c = ModbusClient(host="127.0.0.1", auto_open=True, auto_close=True)
c.open()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def animate(i):
    # Add x and y to lists
    regs = c.read_holding_registers(0, 2)
    reg1.append(regs[0])
    reg2.append(regs[1])
    index.append(i)

    # Draw x and y lists
    ax.clear()
    ax.plot(index, reg1, index, reg2)

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()

c.close()