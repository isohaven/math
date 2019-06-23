import numpy as np
import matplotlib.pyplot as plt

# function we are aproximating
f = lambda x: np.sin(x)

# interval   min, max, step
x = np.arange(-10, 10, 0.1)

# find nth derivitive of function f at point 'c'
def nth_derive(f, c, n, h=1e-5):
    if n == 0:
        return f(c)
    elif n == 1:
        # symmetric derivitive to aproximate
        return (f(c+h) - f(c-h)) / (2*h)
    else:
        return (nth_derive(f, c+h, n-1, h) - nth_derive(f, c-h, n-1, h)) / (2*h)
# plot function
plt.plot(x, f(x))

# create taylor polynomial centered at 'a'
def taylor(f, degree, a=0):
    coeffs = []

factorial_cache = {}
def memoized_factorial(n):
    if n == 0:
        return 1
    elif n in factorial_cache:
        return factorial_cache[str(n)]
    else:
        ans = n * memoized_factorial(n-1)
        factorial_cache[str(n)] = ans
        return ans
print(nth_derive(f, np.pi/3, 4, h=1e-8))
print(nth_derive(f, np.pi/3, 1, h=1e-9))
