import numpy as np
import matplotlib.pyplot as plt


xi = np.float(input('x initial\n:'))
yi = np.float(input('y initial\n:'))

expression = ''
expression_valid = False
while not expression_valid:
    try:
        x = y = 0
        expression = input('enter dy/dx in terms of x, y =\n:')
        eval(expression)
        expression_valid = True
    except ZeroDivisionError:
        expression_valid = True
    except SyntaxError:
        print('error evaluating dy/dx\n')


x_ = np.float(input('end x value\n:'))

def dydx(x, y):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return np.nan

def euler(xi, yi, x_=0):

    x_step = 1
    step_drop_rate = 5
    dot_size = 20
    while x_step > 0.001:
        
        xs = [xi]
        ys = [yi]

        N = int(np.floor( step_drop_rate * (x_ - xi)/(x_step)) - step_drop_rate)
        for n in range(N):
            x = xs[n] + x_step
            y = ys[n] + (x_step*dydx(xs[n], ys[n]))

            xs.append(x)
            ys.append(y)
            if x > x_ + (x_ - xi):
                break
        dot_size = 25*x_step
        plot(xs, ys, label=('ΔX =', str(x_step)[:5]), size=dot_size)
        
        close_index = np.abs(np.asarray(xs) - x_).argmin()
        plt.scatter(xs[close_index], ys[close_index], c='r', s=50, marker='x')
        x_step /= step_drop_rate
        
        plt.pause(0.85)
    plt.show()

    # find closest value to x_ in xs and return y[closest] as guess
    closest = np.abs(np.asarray(xs) - x_).argmin()
    return ys[closest]
def plot(x_list, y_list, label=None, size=10):
    plt.scatter(x_list, y_list, s=size)
    plt.plot(x_list, y_list, label=label)
    plt.legend()
    plt.title(expression)

guess = euler(xi, yi, x_)
print('y(', x_, ') is approximately ', sep='', end='')
print(guess) 
