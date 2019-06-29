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
  theta = np.linspace(0, 2*np.pi, 951)
  delta_theta = (2*np.pi - 0) / n


  f_arg = np.complex128(c + np.exp(1j*theta))
  factor = np.complex128(np.exp(-1j * n * theta))
  integrand = f(f_arg) * factor  
  _sum = delta_theta/3 * np.sum(integrand[0:-1:2] + 4*integrand[1::2] + integrand[2::2])
  return memoized_factorial(n) * _sum.real / (2*np.pi)
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
print(nth_derivitive(f, np.pi/3, 1))
