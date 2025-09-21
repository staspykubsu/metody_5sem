def f(x):
    return x**2+4*x+6

# Шаг 1
a = [-4]
b = [6]
l = 0.2
eps = 0.01
y = []
z = []

# Шаг 2
L0 = abs(b[0] - a[0])
F = [1, 1]  # F0, F1
n = 1
while F[n] < (L0 / l):
    n += 1
    F.append(F[n-1] + F[n-2])

N = n

# Шаг 3
k = 0

# Шаг 4
y.append(a[k] + (F[N-2] / F[N]) * (b[k] - a[k]))
z.append(a[k] + (F[N-1] / F[N]) * (b[k] - a[k]))

for i in range(N-2):
    # Шаг 5
    fy = f(y[k])
    fz = f(z[k])

    # Шаг 6
    if fy <= fz:
        a.append(a[k])
        b.append(z[k])
        y.append(a[k+1] + (F[N-k-3] / F[N-k-1]) * (b[k+1] - a[k+1]))
        z.append(y[k])
    elif fy > fz:
        a.append(y[k])
        b.append(b[k])
        y.append(z[k])
        z.append(a[k+1] + (F[N-k-2] / F[N-k-1]) * (b[k+1] - a[k+1]))
    
    k += 1

y.append(y[k])
z.append(y[k+1] + eps)
fy_final = f(y[k+1])
fz_final = f(z[k+1])
if fz_final >= fy_final:
    a.append(a[k])
    b.append(z[k+1])
else:
    a.append(y[k+1])
    b.append(b[k])

print(f'Итоговый интервал: [{a[-1]}, {b[-1]}]')
print('Точка минимума:', round((a[-1] + b[-1]) / 2))
    
