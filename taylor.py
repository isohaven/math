import numpy as np
import matplotlib.pyplot as plt

# function we are aproximating
f = lambda x: np.sin(x)

# interval   min, max, step
x = np.arange(-10, 10, 0.1)

# find nth derivitive of function 'f' at point 'c'
#TODO use Cauchy's integral formula to accurately compute
# higher order derivitives
def nth_derivitive(f, c, n, ):
    pass
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
