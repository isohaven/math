import numpy as np
import matplotlib.pyplot as plt

# function we are aproximating
f = lambda x: np.sin(x)

# interval   min, max, step
x = np.arange(-10, 10, 0.1)

# find nth derivitive of function 'f' at point 'c'
#TODO use Cauchy's integral formula to accurately compute
# higher order derivitives
def nth_derivitive(f, c, n, dtheta=1e-3, contour_radius=6):
    _sum = 0
    theta = 0
    while theta < 2*np.pi:
        f_arg= np.complex128(c + contour_radius*np.exp(1j*theta))
        factor = (1/contour_radius)**n * np.complex128(np.exp(-1j * n * theta))
        _sum += f(f_arg) * factor * dtheta
        theta += dtheta
    return memoized_factorial(n) * _sum.real / (2*np.pi)
# use simpson's rule to integrate a function 'f'
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
print(nth_derivitive(f, np.pi/3, 10))
