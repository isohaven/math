import numpy as np
import matplotlib.pyplot as plt

def integrate(f, a=-1, b=1, n=100):
    # implementation from
    # https://www.math.ubc.ca/~pwalls/math-python/integration/simpsons-rule/
    if n % 2 != 0:
        n += 1
    delta_x = (b-a)/n
    x = np.linspace(a, b, n+1)
    y = f(x)
    _sum = delta_x/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return _sum


f = lambda x: np.sin(x)

x = np.linspace(0, 2*np.pi, 150)
y = f(x)
_sum = integrate(f, 0, np.pi/2)

interval = np.linspace(0, np.pi/2, 50)
plt.fill_between(interval,f(interval))
plt.plot(x, y, label=f'integrel = {round(_sum)}')
plt.legend()


plt.show()
