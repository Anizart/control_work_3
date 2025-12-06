
import numpy as np

# Размер матрицы
N = 4

# Создаем матрицу A
A = np.array([[i*j/(i+j+2) for j in range(1, N+1)] for i in range(1, N+1)])

# Создаем вектор B
B = np.array([i/(i+1) + 1 for i in range(1, N+1)])

print("Матрица A:")
print(A)
print("\nВектор B:", B)

# 1. Матричное выражение
result = A.T @ A + 2 * (A @ B).reshape(-1, 1)
print("\n1. A^T * A + 2 * A * B:")
print(result)

# 2. Сумма первых трех столбцов A и произведение элементов B
sum_cols = np.sum(A[:, :3])
prod_B = np.prod(B)
print(f"\n2. Сумма первых трех столбцов A: {sum_cols:.4f}")
print(f"   Произведение элементов B: {prod_B:.4f}")

# 3. Вектор C
C = np.array([(np.min(A[i]) / np.sum(A[i])) * B[i] for i in range(N)])
print(f"\n3. Вектор C: {C}")

# 4. Скалярное произведение C и первого столбца A
scalar = np.dot(C, A[:, 0])
print(f"\n4. Скалярное произведение C и первого столбца A: {scalar:.4f}")

# 5. Номера минимальных элементов в B (индексы с 1)
min_val = np.min(B)
min_indices = np.where(B == min_val)[0] + 1
print(f"\n5. Номера минимальных элементов в B: {min_indices}")
