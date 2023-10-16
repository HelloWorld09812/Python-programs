n = int(input())

m = []
i = 2                      #  начинаем с 2
while (n > 1) and i <= n:
    print(f'В данный момент проверяется множитель: {i}')
    if n % i == 0:
        print(int(n), i)
        m.append(i)
        n = n / i
    else:                  #если появляется остаток увеличиваем множитель пока не сравняется с самим числом в сейчашнем состоянии
        i = i + 1

print(m)
product = 1
for i in m:
    product = product * i
print(product)
