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
def nth_derive(f, c, n, h=1e-5):
    pro = memoized_factorial(n) * (1 / (h**n))
    summation = 0
    for m in range(n+1):
        summation +=  ( (-1)**(m+n) ) * (1/(memoized_factorial(m) * memoized_factorial(n-m) )) * f(c + m*h)
    return pro*summation
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
print(derive(f, np.pi/3))
print(nth_derive(f, np.pi/3, 4, h=1e-6))
