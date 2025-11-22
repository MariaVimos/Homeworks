import time

# Función de un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):  # Recorre los números desde 2 hasta n-1
        if n % i == 0:     # Si es divisible
            return False
    return True

inicio = time.time()  # Guarda el tiempo inicial
primos = []           # guarda los numeros primos encontrados

# Recorremos del 1 al 100000 para buscar primos
for num in range(1, 100000):
    if es_primo(num):
        primos.append(num)

fin = time.time()  # Tiempo final

print("Tiempo de ejecucion:", fin - inicio, "segundos")
