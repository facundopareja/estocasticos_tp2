import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import poisson


TWO_SECONDS_IN_MICROSECONDS = 2 * 1000000

measurements_microseconds = np.loadtxt("geiger.csv", delimiter=",", dtype=int)

# a)
# Para cada intervalo de dos segundos se cuentan cuantas particulas ocurren

interval_number = 0
occurrences = 0
occurrence_list = []
for particle_time in measurements_microseconds:
    if interval_number * TWO_SECONDS_IN_MICROSECONDS < particle_time < (interval_number + 1) * TWO_SECONDS_IN_MICROSECONDS:
        occurrences += 1
    else:
        occurrence_list.append(occurrences)
        interval_number += 1
        occurrences = 0
        if interval_number * TWO_SECONDS_IN_MICROSECONDS < particle_time < (
                interval_number + 1) * TWO_SECONDS_IN_MICROSECONDS:
            occurrences += 1

occurrence_array = np.array(occurrence_list)

# Para determinar la media, se promedian todas las realizaciones:
median_ocurrences = np.sum(occurrence_array)/len(occurrence_array)

print(f"La esperanza estimada es: {median_ocurrences}")

# Para determinar la varianza, estimamos la esperanza de las realizaciones al cuadrado,
# elevamos la estimacion previa al cuadrado y aplicamos la formula de varianza.

def power_of_two(x):
    return np.power(x, 2)

occurrences_squared = np.apply_along_axis(power_of_two, 0, occurrence_array)
median_occurrences_squared = np.sum(occurrences_squared)/len(occurrences_squared)
variance = median_occurrences_squared - np.power(median_ocurrences, 2)

print(f"La varianza estimada es: {variance}")

# b)
sns.histplot(occurrence_array, discrete=True, stat='probability')
plt.show()

# c)
x = np.arange(0, 9)
pmf_values = poisson.pmf(x, median_ocurrences)
plt.stem(x, pmf_values, basefmt=" ")
plt.title(f'Distribucion Poisson (λ = {median_ocurrences})')
plt.xlabel('Cantidad de ocurrencias (k)')
plt.ylabel('Probabilidad')
plt.show()