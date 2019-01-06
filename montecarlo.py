# AZR monte carlo integration, iso
import numpy as np
# mean(f) = integral|a <-> b| of f divided by b-a

# function
f = lambda x: np.sin(x)

# interval
a = 0
b = np.pi/2

# calculate aritmatic mean of function
def f_mean(sample_size=1000, a=0, b=1):
    xs = np.random.uniform(a, b, sample_size)
    f_xs = f(xs)
    return(np.sum(f_xs) / sample_size)

def integral(a, b):
    return f_mean(a=a, b=b)*(b-a)
print(integral(a, b))
