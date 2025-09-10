# f(x) = x² + 4x + 6, x ∈ [-4, 6]



# Функция из условия
def f(x):
    return x**2 + 4 * x + 6


# Шаг 1
a, b, eps, l = [-4], [6], 0.2, 0.5

# Шаг 2
k = 0

while True:
    # Шаг 3
    yk = (a[k] + b[k] - eps) / 2
    f_yk = f(yk)

    zk = (a[k] + b[k] + eps) / 2
    f_zk = f(zk)

    # Шаг 4
    if f_yk < f_zk:
        a.append(a[k])
        b.append(zk)

    else:
        a.append(yk)
        b.append(b[k])

    # Шаг 5
    L = abs(b[k + 1] - a[k + 1])
    if L < l:
        print(f"Процесс поиска завершен на {k + 1}-й итерации.")
        print(f"Интервал, содержащий точку минимума: [{a[k + 1]}, {b[k + 1]}]")
        print(f'Найдем приблизительно точку минимума по формуле (a+b)/2: {(a[k+1] + b[k+1]) / 2}')
        print(f'Округлим полученное значение: {round((a[k+1] + b[k+1]) / 2)}')
        break

    else:
        k = k + 1
