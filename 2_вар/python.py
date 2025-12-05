# Задача 1:
import numpy as np

x = np.array([-7.3, 2.7, -2.4, -6.0, -9.4, 8.9, -9.2, 3.4])
y = np.array([-8.9, -5.3, -4.8, -3.4, -6.4, 0.1, 5.3, 6.0])

# Расстояния до начала координат:
r = np.sqrt(x**2 + y**2)

# Углы в градусах:
a_deg = np.degrees(np.arctan2(y, x))

# Точки на макс. расстоянии:
max_r = np.max(r)
indices_max_r = np.where(np.isclose(r, max_r))[0] + 1

# Отрезок с минимальным углом к оси OX (по модулю):
min_angle_idx = np.argmin(np.abs(a_deg)) + 1

print("Расстояния до начала координат:", r)
print("Углы с осью OX (в градусах):", a_deg)
print("Точка на максимальном расстоянии: №", indices_max_r[0])
print("Отрезок с минимальным углом к OX: №", min_angle_idx)

# Задача 2:
import numpy as np

N = 4

# Создание матрицы:
A = np.zeros((N, N))
B = np.zeros(N)

for i in range(N):
    for j in range(N):
        A[i, j] = np.sqrt(abs(np.log((i + 2) / (j + 1))))
    B[i] = np.sin((i + 1) / 2) ** 2

# Матричное выражение:
A4 = np.linalg.matrix_power(A, 4)
A_inv = np.linalg.inv(A)
result = 0.5 * (A4 @ B) - (A_inv @ A_inv @ B)

# Сумма первых двух строк A и произведение элементов B:
sum_rows = np.sum(A[:2, :])
prod_B = np.prod(B)

# Вектор C:
C = np.array([
    B[i] + np.max(A[i, :]) + np.min(A[:, i])
    for i in range(N)
])

# Сумма векторов B и C:
sum_BC = B + C

# Количество минимальных элементов в A:
min_val = np.min(A)
count_min = np.sum(np.isclose(A, min_val))

print("Результат выражения (1/2)A⁴B − (A⁻¹)²B:", result)
print("Сумма первых двух строк A:", sum_rows)
print("Произведение элементов B:", prod_B)
print("Вектор C:", C)
print("Сумма B + C:", sum_BC)
print("Количество минимальных элементов в A:", count_min)

# Задача 3:
import numpy as np
import matplotlib.pyplot as plt

x_list = np.array([1.1,1.7,2.4,3.0,3.5,4.3,4.8,5.5,6.0,6.6,7.3,8.1])
h_list = np.array([10.8,10.7,10.4,10.5,9.7,10.2,9.4,9.4,8.3,8.2,7.8,7.1])

# Аппроксимация параболой:
coeffs = np.polyfit(x_list, h_list, 2)
poly = np.poly1d(coeffs)

# Начальная высота:
h0 = poly(0)

# Проверка попадания в мишень:
x_target = 7.1
h_target = poly(x_target)
hit = abs(h_target - 7.9) <= 0.29

print(f"Камень брошен с высоты: {h0:.2f} м")
print(f"Высота в точке x = 7.1: {h_target:.2f} м")
print(f"Попадёт ли в мишень? {'Да' if hit else 'Нет'}")

x_fit = np.linspace(0, 9, 200)
h_fit = poly(x_fit)

plt.figure(figsize=(8, 5))
plt.plot(x_list, h_list, 'go', label='Измерения')
plt.plot(x_fit, h_fit, 'b-', label='Траектория (парабола)')
plt.axvline(7.1, color='purple', linestyle='--', label='Мишень (x=7.1)')
plt.axhline(7.9, color='purple', linestyle=':')
plt.fill_betweenx([7.9 - 0.29, 7.9 + 0.29], 7.1 - 0.29, 7.1 + 0.29, color='purple', alpha=0.2, label='Область мишени')
plt.xlabel('x (м)')
plt.ylabel('h (м)')
plt.title('Траектория камня')
plt.legend()
plt.grid(True)
plt.show()