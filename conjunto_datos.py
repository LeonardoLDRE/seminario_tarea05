import numpy as np, matplotlib.pyplot as plt

edades = [18, 11, 14, 22, 25, 30, 35, 40, 39, 30, 24, 28, 22, 30, 12]

media, mediana = np.mean(edades), np.median(edades)
varianza, desviacion = np.var(edades), np.std(edades)

edades.sort()
plt.plot(edades, marker='o', linestyle='-', color='blue', label='Edades')


plt.axhline(media, color='red', linestyle='dashed', label=f'Media: {media:.2f}')
plt.axhline(mediana, color='green', linestyle='dashed', label=f'Mediana: {mediana:.2f}')
plt.axhline(varianza, color="purple", linestyle='dashed', label=f'Varianza: {varianza:.2f}')
plt.axhline(desviacion, color="orange", linestyle='dashed', label=f'Desviación: {desviacion:.2f}')

plt.xlabel("Índice")
plt.ylabel("Edad")
plt.legend()
plt.show()


