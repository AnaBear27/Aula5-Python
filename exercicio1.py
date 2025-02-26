#REMOVER ELEMENTOS IGUAIS.

numeros = [2, 4, 6, 8, 4, 10, 6, 12, 14, 8]
print("lista original", numeros)

numeros_sem_repeticoes = []

for numero in numeros:
    if numero not in numeros_sem_repeticoes:
        numeros_sem_repeticoes.append(numero)

print("Lista sem repetição", numeros_sem_repeticoes)