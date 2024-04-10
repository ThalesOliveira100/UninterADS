import statistics

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

contador = 0
for nota in notas:
    if nota == 7:
        contador += 1

print(contador)
print(notas.count(7))

notas[-1] = 4
print(notas)

print(max(notas))

notas.sort()
print(notas)

print(statistics.median(notas))
