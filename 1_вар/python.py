# Задача 1:
import numpy as np

# Дано:
r = np.array([0.7, 0.6, 1.0, 0.7, 1.1, 1.5, 1.6, 1.2]) # сопротивления
I = 3.3 # сила тока

# Напряжение на каждом резисторе:
u = I * r

# Общее сопротивление цепи:
R_total = np.sum(r)

# Общее напряжение в цепи:
U_total = np.sum(u)

# Новое условие: резисторы 1–5, ток = 4.1 А
r_new = r[:5] 
I_new = 4.1
U_new = I_new * np.sum(r_new)

print("Напряжения на резисторах:", u)
print("Общее сопротивление R =", R_total, "Ом")
print("Общее напряжение U =", U_total, "В")
print("Напряжение на новой цепи (резисторы 1–5):", U_new, "В")

# Задача 2:
import numpy as np

N = 4
pi = np.pi
sqrt2 = np.sqrt(2)

# Создание матрицы A и вектора B:
A = np.zeros((N, N))
B = np.zeros(N)

for i in range(N):
    for j in range(N):
        A[i, j] = np.sin((sqrt2 * pi * (j + 1)) / 2 + 1) * np.log(np.sqrt(i + 1 + 2))
    B[i] = np.sin((i + 1)**2 - pi / sqrt2)

# Вычисление выражения: A^3 * B + 5 * A^(-1) * B
A3 = np.linalg.matrix_power(A, 3)
A_inv = np.linalg.inv(A)
result_expr = A3 @ B + 5 * (A_inv @ B)

# Суммы:
sum_A = np.sum(A)
sum_B = np.sum(B)

# Вектор C:
C = np.array([B[i] * np.max(A[i, :]) for i in range(N)])

# Скалярное произведение B и C:
dot_BC = np.dot(B, C)

# Индексы максимальных элементов матрицы A:
max_val = np.max(A)
max_indices = np.where(A == max_val)

print("Результат выражения A^3*B + 5*A^(-1)*B:\n", result_expr)
print("Сумма элементов A:", sum_A)
print("Сумма элементов B:", sum_B)
print("Вектор C:", C)
print("Скалярное произведение B·C:", dot_BC)
print("Индексы максимальных элементов A:", list(zip(max_indices[0], max_indices[1])))

# Задача 3:
import numpy as np
import matplotlib.pyplot as plt

# Данные:
x_list = np.array([1.3, 1.9, 2.7, 3.2, 4.0, 4.6, 5.3, 5.9, 6.6, 7.5])
h_list = np.array([3.2, 4.0, 4.5, 4.8, 4.8, 5.0, 4.9, 4.7, 4.5, 4.2])

# Полином второй степени:
coeffs = np.polyfit(x_list, h_list, 2)
poly = np.poly1d(coeffs)

# Высота броска:
h_start = poly(0)

# Проверка попадания в корзину:
x_hoop = 8.0
h_hoop_center = 3.0
hoop_radius = 0.27
h_at_hoop = poly(x_hoop)
in_hoop = abs(h_at_hoop - h_hoop_center) <= hoop_radius

print(f"Мяч брошен с высоты: {h_start:.2f} м")
print(f"Высота мяча над корзиной (x=8.0): {h_at_hoop:.2f} м")
print(f"Попадёт ли в корзину? {'Да' if in_hoop else 'Нет'}")

# График:
x_plot = np.linspace(0, 9, 200)
h_plot = poly(x_plot)

plt.figure(figsize=(8, 5))
plt.plot(x_list, h_list, 'ro', label='Измеренные точки')
plt.plot(x_plot, h_plot, 'b-', label='Траектория (полином 2-й степени)')
plt.axvline(x=8.0, color='green', linestyle='--', label='Позиция корзины')
plt.axhline(y=3.0, color='green', linestyle=':')
plt.fill_betweenx([3.0 - hoop_radius, 3.0 + hoop_radius],
                  8.0 - hoop_radius, 8.0 + hoop_radius,
                  color='green', alpha=0.2, label='Корзина (±0.27 м)')
plt.xlabel('x (м)')
plt.ylabel('h (м)')
plt.title('Траектория броска мяча')
plt.legend()
plt.grid(True)
plt.show()