
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Исходные данные
x_list = np.array([1.35, 3.75, 6.33, 9.17, 11.16, 13.85, 15.96, 18.26, 20.12])
h_list = np.array([22.14, 21.25, 21.13, 18.72, 18.49, 15.38, 12.41, 10.17, 7.6])

# 1. Аппроксимация полиномом второй степени
coeffs = np.polyfit(x_list, h_list, 2)  # коэффициенты полинома 2-й степени
poly_func = np.poly1d(coeffs)  # функция полинома

# Выводим уравнение траектории
print(f"Уравнение траектории: h(x) = {coeffs[0]:.4f}x² + {coeffs[1]:.4f}x + {coeffs[2]:.4f}")

# 2. Начальная высота (при x=0)
initial_height = poly_func(0)
print(f"\n1. Начальная высота (x=0): {initial_height:.2f} м")

# 3. Проверка попадания в мишень
target_x = 18.292
target_h = 10.111
radius = 0.21

# Вычисляем высоту траектории в точке target_x
h_at_target_x = poly_func(target_x)
distance = abs(h_at_target_x - target_h)

print(f"\n2. Проверка попадания в мишень:")
print(f"   Центр мишени: ({target_x}, {target_h})")
print(f"   Высота траектории при x={target_x}: {h_at_target_x:.3f} м")
print(f"   Расстояние от центра мишени: {distance:.3f} м")
print(f"   Радиус мишени: {radius} м")

if distance <= radius:
    print("   Результат: КАМЕНЬ ПОПАЛ В МИШЕНЬ!")
else:
    print("   Результат: камень промахнулся")

# 4. Построение графика
x_fit = np.linspace(0, 22, 200)
h_fit = poly_func(x_fit)

plt.figure(figsize=(10, 6))

# Исходные точки
plt.scatter(x_list, h_list, color='red', s=50, label='Измеренные точки', zorder=5)

# Линия тренда
plt.plot(x_fit, h_fit, 'b-', linewidth=2, label='Аппроксимация полиномом 2-й степени')

# Мишень
target_circle = Circle((target_x, target_h), radius, color='green', alpha=0.3, 
                       label=f'Мишень (радиус={radius})')
plt.gca().add_patch(target_circle)
plt.scatter(target_x, target_h, color='green', s=30, zorder=5)

# Начальная точка (x=0)
plt.scatter(0, initial_height, color='orange', s=80, label=f'Начало броска (0, {initial_height:.1f})')

# Оформление графика
plt.xlabel('Расстояние, x (м)', fontsize=12)
plt.ylabel('Высота, h (м)', fontsize=12)
plt.title('Траектория движения камня', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()
plt.axis([0, 22, 0, 25])  # Устанавливаем границы осей

# Отображаем уравнение на графике
equation_text = f'h(x) = {coeffs[0]:.4f}x² + {coeffs[1]:.4f}x + {coeffs[2]:.4f}'
plt.text(0.5, 23, equation_text, fontsize=11, 
         bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

plt.tight_layout()
plt.show()


