import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)
y = x ** 2

plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', color='blue',
         linestyle='-', linewidth=2)

plt.title('Square Numbers Line Chart')
plt.xlabel('Number')
plt.ylabel('Square')
plt.grid(True)
plt.show()