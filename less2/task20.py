from scipy.optimize import minimize

def f(xy, a, b):
    x, y = xy
    return (x + y)**2 - 2*x*(y + a) - 2*a*b + a + b
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
initial_guess = (0, 0)
result = minimize(f, initial_guess, args=(a, b))
x_min, y_min = result.x
print(f'Координаты локального минимума вблизи точки (0,0): ({x_min:.2f}, {y_min:.2f})')