N = int(input("Введите количество вершин: "))
M = int(input("Введите количество ребер: "))

matrix_incidence = []

print("Введите матрицу инцедентности:")
for i in range(1, N + 1):
    matrix_incidence.append(list(map(int, input().split())))
print()

matrix_adjacency = [[0] * N for i in range(N)]

for i in range(N):
    for j in range(M):
        if matrix_incidence[i][j] == 1:
            for k in range(i + 1, N):
                if matrix_incidence[k][j] == 1:
                    matrix_adjacency[i][k] = 1
                    matrix_adjacency[k][i] = 1

print("Матрица смежности:")
for i in range(N):
    print(*matrix_adjacency[i])
