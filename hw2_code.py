# import math 
# def f(x):
#     return x * math.exp(x)

# def derivative_exact(x): 
#     return (x + 1) * math.exp(x) 

# def derivative_approx(a, h): 
#     return (f(a - 2*h)- 8*f(a - h) + 8*f(a+h) - f(a + 2 * h))/(12*h)

# a = 0.5 
# h_val = [0.1, 0.05, 0.025, 0.0125, 0.00625]
# exact = derivative_exact(a)
# previous_error = None
# for h in h_val: 
#     approx = derivative_approx(a, h)
#     error = abs(approx - exact) 
#     if previous_error is None: 
#         order = "N/A"
#         print(f"h: {h}, approx: {approx:.4f} error: {error:.4e} order {order}") 
#     else:
#         order = math.log(previous_error / error) / math.log(2)
#         print(f"h: {h}, approx: {approx:.4f} error: {error:.4e} order {order:.4f}") 
#     previous_error = error

import numpy as np  #used for linear algebra 
import math

def f1(x):
    return math.cos(x)

def f2(x): 
    return 1 / (1 + x**2)

def naive_coefficients(x_vals, y_vals): 
    A = np.vander(x_vals, increasing=True) 
    return np.linalg.solve(A, y_vals)

def naive_eval(coeff, x):
    result=0
    for i in range(len(coeff)):
        result += coeff[i] * x**i
    return result 

def lagrange_interpolation(x_vals, y_vals, x): 
    result = 0 
    for i in range(len(x_vals)):
        term = y_vals[i]
        for j in range(len(x_vals)): 
            if i != j: 
                term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        result += term 
    return result 

def error_norm (approx, exact):
    total = 0 
    for i in range(len(approx)): 
        total += (approx[i] - exact[i]) ** 2
    return math.sqrt(total)

def error(f,n): 
    x_vals = np.linspace(-1, 1, n + 1)
    y_vals = [] 
    for x in x_vals: 
        y_vals.append(f(x))

    y_vals = np.array(y_vals)
    coeff = naive_coefficients(x_vals, y_vals) 
    grid = np.linspace(-1, 1, 1000)
    
    naive_vals = [] 
    lagrange_vals = []
    exact_vals = [] 
    for x in grid: 
        naive_vals.append(naive_eval(coeff, x))
        lagrange_vals.append(lagrange_interpolation(x_vals, y_vals, x))
        exact_vals.append(f(x))
    naive_vals = np.array(naive_vals)
    lagrange_vals = np.array(lagrange_vals)
    exact_vals = np.array(exact_vals)

    naive_error = error_norm(naive_vals, exact_vals)
    lagrange_error = error_norm(lagrange_vals, exact_vals)

    return naive_error, lagrange_error


for n in [5, 10, 20, 40]:
    f1_naive, f1_lagrange = error(f1, n)
    f2_naive, f2_lagrange = error(f2, n)

    print(f"n = {n}")
    print(f"f1 naive: {f1_naive:.4e}, lagrange: {f1_lagrange:.4e}")
    print(f"f2 naive: {f2_naive:.4e}, lagrange: {f2_lagrange:.4e}")
    print()