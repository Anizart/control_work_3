import numpy as np
from math import cos, log, sqrt

N = 4

# 1. Создание матрицы A и вектора B
A = np.zeros((N, N))
B = np.zeros(N)

for i in range(N):
    for j in range(N):
        # a_ij = ln( (i+j+3)^(1/3) ) = (1/3) * ln(i+j+3)
        A[i, j] = (1/3) * log(i + j + 3)
    # b_i = cos(i^2 / sqrt(3))
    B[i] = cos(i**2 / sqrt(3))

print("Матрица A:")
print(A)
print("\nВектор B:")
print(B)

# 2. Вычисление A^2 * B - 3 * (A^{-1})^2 * B
try:
    A_inv = np.linalg.inv(A)
    # A^2 * B
    term1 = np.dot(np.dot(A, A), B)
    # (A^{-1})^2 * B
    term2 = np.dot(np.dot(A_inv, A_inv), B)
    result_vector = term1 - 3 * term2
    
    print("\n1. A²·B - 3·(A⁻¹)²·B:")
    print(result_vector)
except np.linalg.LinAlgError:
    print("\n1. Ошибка: матрица A вырожденная, нельзя вычислить обратную")

# 3. Сумма элементов первых трех строк матрицы A
sum_first_three_rows = np.sum(A[0:3, :])
print(f"\n2. Сумма элементов первых трех строк матрицы A: {sum_first_three_rows}")

# Произведение элементов вектора B
product_B = np.prod(B)
print(f"   Произведение элементов вектора B: {product_B}")

# 4. Вектор C: c_i = cos|b_i| + max_j(a_ij)
C = np.zeros(N)
for i in range(N):
    C[i] = cos(abs(B[i])) + np.max(A[i, :])
print(f"\n3. Вектор C: {C}")

# 5. Скалярное произведение вектора C на первый столбец матрицы A
dot_product = np.dot(C, A[:, 0])
print(f"\n4. Скалярное произведение C на первый столбец A: {dot_product}")

# 6. Количество элементов вектора B, равных минимальному элементу матрицы A
min_A = np.min(A)
# Для сравнения вещественных чисел используем допуск
tolerance = 1e-10
count = np.sum(np.abs(B - min_A) < tolerance)
print(f"\n5. Минимальный элемент матрицы A: {min_A}")
print(f"   Количество элементов вектора B, равных минимальному элементу A: {count}")
