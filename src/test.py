import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
print(X)
print(Y1)

for x, y in zip(X, Y1):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')

plt.bar(X, Y1, facecolor='#9999ff', edgecolor='white')
plt.show()
