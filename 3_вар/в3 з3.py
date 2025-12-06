import numpy as np
import matplotlib.pyplot as plt

# Данные
x = np.array([1.641, 3.03, 4.11, 5.6, 6.8, 8.261, 9.362, 10.49, 12.5, 13.287])
h = np.array([3.98, 5.04, 6.05, 6.64, 7.46, 8.04, 7.79, 8.243, 8.251, 7.779])

# Находим коэффициенты параболы (второй степени)
coef = np.polyfit(x, h, 2)
a, b, c = coef
print(f"Уравнение: h = {a:.3f}x² + {b:.3f}x + {c:.3f}")

# Высота броска (при x=0)
print(f"\nВысота броска: {c:.2f} м")

# Проверка попадания в корзину
x_k = 16.573
h_k = 3.05
r = 0.24
h_m = a * x_k**2 + b * x_k + c
print(f"\nВысота мяча в x={x_k}: {h_m:.2f} м")
print(f"Центр корзины на высоте: {h_k} м")

if abs(h_m - h_k) <= r:
    print("Мяч попадет в корзину")
else:
    print("Мяч не попадет в корзину")

# График
x_smooth = np.linspace(0, 17, 100)
h_smooth = a * x_smooth**2 + b * x_smooth + c

plt.figure(figsize=(8, 5))
plt.scatter(x, h, color='red', label='Точки измерений')
plt.plot(x_smooth, h_smooth, 'b-', label='Траектория')
plt.plot(0, c, 'go', label=f'Бросок (0, {c:.2f})')
plt.plot(x_k, h_m, 'mo', label=f'Мяч в x корзины ({h_m:.2f})')

# Область корзины
plt.axvline(x_k, linestyle='--', color='gray', alpha=0.5)
plt.axhspan(h_k - r, h_k + r, xmin=(x_k-0.5)/17, xmax=(x_k+0.5)/17, 
            alpha=0.3, color='yellow', label='Корзина')

plt.xlabel('x, м')
plt.ylabel('h, м')
plt.legend()
plt.grid(True)
plt.show()
