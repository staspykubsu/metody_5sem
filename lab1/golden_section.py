def f(x):
    return x**2+4*x+6

print('----------------------------------------------')
l = 0.2
a_k = [-4]
b_k = [6]
k = 0
y_k = [a_k[0] + 0.38196 * (b_k[0] - a_k[0])]
z_k = [a_k[0] + b_k[0] - y_k[0]]
print('Начальные значения:')
print(f'l = {l}')
print(f'k = 0')
print(f'a{k} = {a_k[k]}')
print(f'b{k} = {b_k[k]}')
print(f'y{k} = {y_k[k]}')
print(f'z{k} = {z_k[k]}')
print('----------------------------------------------')

while True:
    # Шаг 4
    f_yk = f(y_k[k])
    f_zk = f(z_k[k])
    print(f'k = {k}. Итерация номер {k+1}')
    print('Шаг 4')
    print(f'f(y{k}) = {f_yk}')
    print(f'f(z{k}) = {f_zk}')
    print()
    
    # Шаг 5
    print('Шаг 5')
    if f_yk <= f_zk:
        print(f'f(y{k}) <= f(z{k})')
        a_k.append(a_k[k])
        b_k.append(z_k[k])
        y_k.append(a_k[k+1] + b_k[k+1] - y_k[k])
        z_k.append(y_k[k])
        print(f'a{k+1} = {a_k[k+1]}')
        print(f'b{k+1} = {b_k[k+1]}')
        print(f'y{k+1} = {y_k[k+1]}')
        print(f'z{k+1} = {z_k[k+1]}')
        print()
    
    else:
        print(f'f(y{k}) > f(z{k})')
        a_k.append(y_k[k])
        b_k.append(b_k[k])
        y_k.append(z_k[k])
        z_k.append(a_k[k+1] + b_k[k+1] - z_k[k])
        print(f'a{k+1} = {a_k[k+1]}')
        print(f'b{k+1} = {b_k[k+1]}')
        print(f'y{k+1} = {y_k[k+1]}')
        print(f'z{k+1} = {z_k[k+1]}')
        print()
    
    # Шаг 6
    delta = abs(a_k[k+1] - b_k[k+1])
    print('Шаг 6')
    print(f'Δ = {delta}')
    
    if delta <= l:
        ans = round((a_k[k+1] + b_k[k+1]) / 2)
        print('Заданная точность достигнута.')
        print('Ответ:', ans)
        print('----------------------------------------------')
        break
    else:
        print('Заданная точность еще не достигнута, продолжаем.')
        print('----------------------------------------------')
        k += 1
