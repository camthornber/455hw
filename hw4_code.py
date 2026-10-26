import math 
import matplotlib.pyplot as plt 

def Simpson(fun, a, b, n): 
    h = (b - a) / (2 * n) 
    total = fun(a) + fun(b)
    for i in range(1,2 * n): 
        x = a + i * h 
        if i % 2 == 1: 
            total = total + 4 * fun(x) 
        else: 
            total = total + 2 * fun(x) 
    return (h/3) * total 

def f(x):
    return math.exp(-x)

a = 0.0 
b = 0.8 
exact = 1 - math.exp(-0.8)
n_values = [2,4,8,16,32,128]
errors = [] 

print("Integral =", format(exact, ".8e"))
print("n | Sn | En | p")
for i in range(len(n_values)):
    n = n_values[i]
    approx = Simpson(f,a,b,n)
    error = abs(approx - exact) 
    errors.append(error)
    if i == 0: 
        print(f"{n} {approx:.8f} {error:.8e} ---") 
    else: 
        old_n = n_values[i-1]
        old_error = errors[i-1]
        order = math.log(old_error / error) / math.log(n / old_n)
        print(f"{n} {approx:.8f} {error:.8e} {order:.8f}") 

plt.figure(figsize=(7,5))
plt.loglog(n_values, errors, "o-", label="Simpson error")
plt.xlabel("n")
plt.ylabel(r"E_n") 
plt.savefig("HW05_error_plot.pdf")