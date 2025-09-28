from math import sqrt

def f(x1, x2):
    return 7 * x1**2 + x2**2 - x1 * x2 + x1

def gradient(x1, x2):
    df_dx1 = 14 * x1 - x2 + 1
    df_dx2 = 2 * x2 - x1
    return (df_dx1, df_dx2)

# шаг 1
x0 = (1, 2)
eps1 = 0.1
eps2 = 0.15
M = 10

# шаг 2
k = 0
x_current = x0
x_min = None

for i in range(M):
    # шаг 3
    g1, g2 = gradient(x_current[0], x_current[1])
    
    # шаг 4
    norm_grad = sqrt(g1**2 + g2**2)
    if norm_grad < eps1:
        x_min = x_current
        break
    
    # шаг 6
    x1, x2 = x_current
    
    A = 7*g1**2 + g2**2 - g1*g2
    B = -14*x1*g1 - 2*x2*g2 + x1*g2 + x2*g1 - g1
    
    if A > 0:
        t_k = -B / (2 * A)
    else:
        t_k = 0.1

    # шаг 7
    x1_next = x1 - t_k * g1
    x2_next = x2 - t_k * g2
    x_next = (x1_next, x2_next)
    
    norm_diff = sqrt((x1_next - x1)**2 + (x2_next - x2)**2)
    func_diff = abs(f(x_next[0], x_next[1]) - f(x_current[0], x_current[1]))
    
    # шаг 8
    if norm_diff < eps2 and func_diff < eps2:
        x_min = x_next
        break
    
    x_current = x_next

if x_min is None:
    x_min = x_current

print(f"Найденная точка: x = ({x_min[0]}, {x_min[1]})")
