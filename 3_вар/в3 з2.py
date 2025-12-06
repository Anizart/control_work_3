import numpy as np

N = 4

# Матрица A
A = np.array([[i*j/(i+j+2) for j in range(1, N+1)] for i in range(1, N+1)])

# Вектор B
B = np.array([i/(i+1) + 1 for i in range(1, N+1)])

print("Матрица A:")
print(A)
print("\nВектор B:", B)

# 1. Матричное выражение
result = A.T @ A + 2 * (A @ B)
print("\n1. A^T * A + 2 * A * B:")
print(result)

# 2. Суммы
row_prod_sum = sum(np.prod(row) for row in A)
B_sum = sum(B)
print(f"\n2. Сумма произведений строк A: {row_prod_sum}")
print(f"   Сумма элементов B: {B_sum}")

# 3. Вектор C
C = np.array([(max(A[i])/sum(A[i])) * B[i] for i in range(N)])
print(f"\n3. Вектор C: {C}")

# 4. Скалярное произведение
scalar = np.dot(B, A[:, 2])
print(f"\n4. Скалярное произведение B и 3-го столбца A: {scalar}")

# 5. Нулевые элементы
zeros = np.count_nonzero(A == 0)
print(f"\n5. Нулевых элементов в A: {zeros}")
