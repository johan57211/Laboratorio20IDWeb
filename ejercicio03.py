while True:
    N = int(input("Ingresa N (>= 3): "))
    if N >= 3:
        break
    print("N debe ser mayor o igual a 3.")

matriz = [[0 for _ in range(N)] for _ in range(N)]

top = 0
bottom = N - 1
left = 0
right = N - 1

num = 1

while left <= right and top <= bottom:
    for col in range(left, right + 1):
        matriz[top][col] = num
        num += 1
    top += 1

    for fila in range(top, bottom + 1):
        matriz[fila][right] = num
        num += 1
    right -= 1

    if top <= bottom:
        for col in range(right, left - 1, -1):
            matriz[bottom][col] = num
            num += 1
        bottom -= 1

    if left <= right:
        for fila in range(bottom, top - 1, -1):
            matriz[fila][left] = num
            num += 1
        left += 1

for fila in matriz:
    print(fila)