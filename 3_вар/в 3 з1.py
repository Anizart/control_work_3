import numpy as np

# Данные
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([71, 79, 12, 45, 88, 53, 43])

m = 4
radius = 100

# Координаты всех точек (матрица 7×2)
points = np.column_stack([x, y])

# Координаты точки m
xm, ym = points[m-1]

# Расстояния до всех точек
distances = np.sqrt((x - xm)**2 + (y - ym)**2)

# Результаты
print("Расстояния:")
for i, d in enumerate(distances):
    if i+1 != m:
        print(f"  до пункта {i+1}: {d:.2f} км")

in_radius = [i+1 for i in range(7) if i+1 != m and distances[i] <= radius]
max_dist = max(dist for i, dist in enumerate(distances) if i+1 != m)
max_points = [i+1 for i, dist in enumerate(distances) if abs(dist - max_dist) < 0.001 and i+1 != m]

print(f"\nВ радиусе: {in_radius}")
print(f"Макс.расстояние: {max_dist:.2f} км (пункты {max_points})")
print(f"Количество: {len(in_radius)}")
