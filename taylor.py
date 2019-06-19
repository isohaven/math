import numpy as np
import matplotlib.pyplot as plt

# function we are aproximating
f = lambda x: np.sin(x)

# interval   min, max, step
x = np.arange(-10, 10, 0.1)

# symmetric derivitive to aproximate
# derivitive at point 'c'
def derive(f, c, h=1e-5):
    return (f(c+h) - f(c-h)) / (2*h)

# plot function
plt.plot(x, f(x))

def taylor(f, degree):
    coeffs = []


plt.show()
