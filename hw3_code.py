import math
print("8a. Bisection and fixed-point iteration")

def f(x):
    return x - math.cos(x) 

def bisection(epsilon): 
    a = 0.0 
    b = 1.0 
    iterations = 0 

    while b - a > epsilon: 
        midpoint = (a + b)/2
        if f(a) * f(midpoint) <= 0: 
            b = midpoint 
        else: 
            a = midpoint 
        iterations += 1
    root = (a + b)/2
    return iterations, root

def fixed_point(epsilon): 
    x = 0.5 
    iterations = 0
    while True: 
        x_new = math.cos(x)
        iterations += 1 
        if abs(x_new -x) <= epsilon: 
            break 
        x = x_new 
    return iterations, x_new 

tolerance = [1e-5, 1e-6, 1e-8, 1e-10]
for epsilon in tolerance: 
    bi_it, bi_root = bisection(epsilon)
    fp_it, fp_root = fixed_point(epsilon)
    print("epsilon =", epsilon)
    print("bisection:", bi_it, bi_root)
    print("fixed point:", fp_it, fp_root)
    print() 

print("8b. Newton's method") 

def f1(x):
    return x - math.cos(x)

def df1(x):
    return 1 + math.sin(x)

def f2(x): 
    return (x - math.cos(x)) ** 2

def df2(x): 
    return 2 * (x - math.cos(x)) * (1 + math.sin(x))

def newton(f, df, epsilon): 
    x = 0.5 
    iterations = 0 
    while True: 
        x_new = x - f(x) / df(x)
        iterations += 1
        if abs(x_new - x) <= epsilon: 
            break
        x = x_new
    return iterations, x_new

tolerance = [1e-5, 1e-6, 1e-8, 1e-10] 
for epsilon in tolerance: 
    f1_it, f1_root = newton(f1, df1, epsilon)
    f2_it, f2_root = newton(f2, df2, epsilon)
    print("epsilon =", epsilon) 
    print("f1:", f1_it, f1_root)
    print("f2:", f2_it, f2_root)
