import matplotlib.pyplot as plt
import numpy as np

fact = lambda x: 1 if x in [0, 1] else x * fact(x - 1)
exp_n = lambda x, n: sum([(x**k)/fact(k) for k in range(n)])

x = np.linspace(-4, 4, 100)
ys = [np.exp(x)] + [exp_n(x, k) for k in range(5, 7)]

for y in ys:
    plt.plot(x, y)

plt.show()