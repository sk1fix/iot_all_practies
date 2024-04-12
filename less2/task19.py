from scipy.optimize import minimize
import numpy as np

def f(x):
    return x**2 * (x - 4)**2 * 2 * np.exp(-x**2)

x0 = float(input("Введите начальное предположение x0: "))

dx = 0.001
x = np.arange(-4, 4, dx)

def negative_f(x):
    return -f(x)

result = minimize(negative_f, x0, method='BFGS')

x_max = round(result.x[0], 2)

print(f"Координата x локального максимума вблизи x0: {x_max}")