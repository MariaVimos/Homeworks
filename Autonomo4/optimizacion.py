import time
import math

# Función optimizada 
def es_primo_rapido(n):
    if n < 2:
        return False
    limite = int(math.sqrt(n)) + 1  # revisamos hasta la raíz cuadrada
    for i in range(2, limite):
        if n % i == 0:
            return False
    return True

inicio = time.time()
# Usamos list comprehension para hacerlo más rápido
primos = [num for num in range(1, 100000) if es_primo_rapido(num)]

fin = time.time()

print("Tiempo de Optimizacion:", fin - inicio, "segundos")
