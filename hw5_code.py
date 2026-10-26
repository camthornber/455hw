import numpy as np 

def back_sub(a,b): 
    n = len(b)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        total = 0.0 
        for j in range(i + 1, n): 
            total = total + a[i,j] * x[j]
        x[i] = (b[i] - total) / a[i,i]
    return x

def naive_gaussian(a,b):
    a = np.array(a, dtype=float, copy=True)
    b = np.array(b, dtype=float, copy=True)
    n = len(b)
    for k in range(n - 1):
        for i in range(k + 1, n):
            multi = a[i,k] / a[k,k]
            for j in range(k + 1, n):
                a[i,j] = a[i,j] - multi * a[k,j]
            b[i] = b[i] - multi * b[k]
            a[i,k] = 0.0 
    return back_sub(a,b)


def gaussian_partial(a,b):
    a = np.array(a, dtype=float, copy=True)
    b = np.array(b, dtype=float, copy=True)
    n = len(b)
    for k in range(n - 1):
        pivoter = k
        for i in range(k + 1, n):
            if abs(a[i,k]) > abs(a[pivoter, k]): 
                pivoter = i
        if pivoter != k: 
            temp = a[k].copy() 
            a[k] = a[pivoter]
            a[pivoter] = temp 
            temp = b[k]
            b[k] = b[pivoter]
            b[pivoter] = temp 
        for i in range(k + 1, n): 
            multi = a[i,k] / a[k,k]
            for j in range(k + 1, n): 
                a[i,j] = a[i,j] - multi * a[k,j]
            b[i] = b[i] - multi * b[k]
            a[i,k] = 0.0 
    return back_sub(a,b)

def gaussian_scaled(a,b):
    a = np.array(a, dtype=float, copy=True)
    b = np.array(b, dtype=float, copy=True)
    n = len(b)
    scales = np.zeros(n)
    for i in range(n):
        for j in range(n): 
            if abs(a[i,j]) > scales[i]: 
                scales[i] = abs(a[i,j])
    for k in range(n - 1): 
        pivoter = k 
        big_ratio = abs(a[k,k]) / scales[k] 
        for i in range(k + 1, n): 
            ratio = abs(a[i,k]) / scales[i]
            if ratio > big_ratio:
                big_ratio = ratio 
                pivoter = i 
        if pivoter != k:
            temp = a[k].copy() 
            a[k] = a[pivoter]
            a[pivoter] = temp 
            temp = b[k]
            b[k] = b[pivoter]
            b[pivoter] = temp 
            temp = scales[k]
            scales[k] = scales[pivoter]
            scales[pivoter] = temp 
        for i in range(k + 1, n): 
            multi = a[i,k] / a[k,k]
            for j in range(k + 1, n): 
                a[i,j] = a[i,j] - multi * a[k,j]
            b[i] = b[i] - multi * b[k]
            a[i,k] = 0.0 
    return back_sub(a,b)

methods = [naive_gaussian, gaussian_partial, gaussian_scaled]
method_names = ["No pivoting", "Partial pivoting", "Scaled partial pivoting"]

#Problem 1 
thetas = [1e-5, 1e-10, 1e-15]
print("Problem 1")
for theta in thetas:
    a = np.array([[theta, -1.0], [1.0, 2.0]])
    b = np.array([-1.0, 3.0])
    print(f"\n theta = {theta:.0e}") 
    for k in range(len(methods)): 
        x = methods[k](a,b)
        residual = b - a @ x 
        residual_norm = np.sqrt(np.sum(residual ** 2))
        print(method_names[k]) 
        print("Sol:", x)
        print(f"Residual norm: {residual_norm:.8e}")

#Problem 2 
n = 10 
nodes = np.zeros(n)
b = np.zeros(n)
v = np.zeros((n,n))

for i in range(n): 
    nodes[i] = i + 1 
    b[i] = nodes[i] + 1 
    for j in range(n): 
        v[i,j] = nodes[i] ** (9 - j)

a_exact = np.zeros(n)
a_exact[8] = 1.0 
a_exact[9] = 1.0 
print("Problem 2")
for k in range(len(methods)): 
    a = methods[k](v,b) 
    difference = a - a_exact
    coeff_error = np.sqrt(np.sum(difference ** 2))
    residual = b - v @ a 
    residual_norm = np.sqrt(np.sum(residual ** 2))
    print("\n" + method_names[k]) 
    print(f"CoefficientsL {a}. Coefficent error: {coeff_error:.8e}. Residual norm: {residual_norm:.8e}")