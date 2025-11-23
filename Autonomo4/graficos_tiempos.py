import matplotlib.pyplot as plt

tiempos = [15.10, 0.40]  
labels = ['Código Original', 'Código Optimizado']

plt.bar(labels, tiempos, color=['#F7C6D9', '#D9C6F7'])
plt.ylabel("Segundos")
plt.title("Comparación de tiempos")
plt.show()
