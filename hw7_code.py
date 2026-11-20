import numpy as np
def jacobi(A, b, epsilon, max_iter=2000000): 
    n = len(b) 
    x = np.zeros(n)
    for k in range(1, max_iter + 1): 
        old_x = x.copy()
        for i in range(n):
            lower_sum = 0.0 
            for j in range(i): 
                lower_sum += A[i, j] * old_x[j]
            upper_sum = 0.0 
            for j in range(i + 1, n): 
                upper_sum += A[i, j] * old_x[j]
            x[i] = (b[i] - lower_sum - upper_sum) / A[i,i]
        change = np.max(np.abs(x - old_x))
        if change <= epsilon: 
            return x, k 
    return x, "iteration limit reached" 

def gauss_seidel(A, b, epsilon, max_iter=2000000): 
    n = len(b) 
    x = np.zeros(n) 
    for k in range(1, max_iter + 1): 
        old_x = x.copy() 
        for i in range(n): 
            lower_sum = 0.0 
            for j in range(i): 
                lower_sum += A[i,j] * x[j]
            upper_sum = 0.0 
            for j in range(i + 1, n): 
                upper_sum += A[i,j] * old_x[j]
            x[i] = (b[i] - lower_sum - upper_sum) / A[i,i] 
        change = np.max(np.abs(x - old_x))
        if change <= epsilon:
            return x, k 
    return x, "iteration limit reached"

def sor(A,b, omega, epsilon, max_iter=2000000): 
    n = len(b) 
    x = np.zeros(n) 
    for k in range(1, max_iter + 1): 
        old_x = x.copy() 
        for i in range(n): 
            lower_sum = 0.0 
            for j in range(i): 
                lower_sum += A[i,j] * x[j] 
            upper_sum = 0.0 
            for j in range(i + 1, n): 
                upper_sum += A[i,j] * old_x[j]
            gs_value = (b[i] - lower_sum - upper_sum) / A[i,i] 
            x[i] = (1 - omega) * old_x[i] + omega * gs_value 
        change = np.max(np.abs(x - old_x))
        if change <= epsilon:
            return x, k 
    return x, "iteration limit reached"

print("P1.") 
print("delta.     Jacobi.       Gauss-Seidel") 
deltas = [1.0, 0.1, 0.001, 0.00001]
epsilon = 0.00001 

for delta in deltas: 
    A = np.array([[1 + delta, -1, 0], [-1, 2 + delta, -1], [0, -1, 1+ delta]], dtype=float)
    b = np.array([-1,-1,2], dtype=float)
    x_jacobi, count_jacobi = jacobi(A, b, epsilon)
    x_gs, count_gs = gauss_seidel(A, b, epsilon)
    print(f"{delta:<12g}{count_jacobi:<13}{count_gs}")

print()
print("P2.")
print("epsilon.    omega.     iterations.")
A = np.array([[10,1,1],[1,-10,1],[0,1,10]], dtype=float) 
b = np.array([1,2,3], dtype=float) 
omegas = [1.1, 1.4, 1.6] 
epsilons = [1e-5, 1e-8, 1e-10]

for epsilon in epsilons: 
    for omega in omegas:
        x_sor, count_sor = sor(A, b, omega, epsilon)
        print(f"{epsilon:<12g}{omega:<12.1f}{count_sor}")