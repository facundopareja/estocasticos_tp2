import numpy as np
import matplotlib.pyplot as plt

TOTAL_TIME = 27 * 60 * 1000000 # paso 27 min a microsegundos

measurements_microseconds = np.loadtxt("geiger.csv",
                 delimiter=",", dtype=int)

# a)
def convert_microseconds_to_seconds(x):
    return x/1000000

measurements_seconds = np.apply_along_axis(convert_microseconds_to_seconds, 0, measurements_microseconds)

# Para determinar la media, se promedian todas las realizaciones:
median_time = np.sum(measurements_seconds)/len(measurements_seconds)

print(f"La esperanza estimada es: {median_time}")

# Para determinar la varianza, estimamos la esperanza de las realizaciones al cuadrado,
# elevamos la estimacion previa al cuadrado y aplicamos la formula de varianza.

def power_of_two(x):
    return np.power(x, 2)

measurements_seconds_squared = np.apply_along_axis(power_of_two, 0, measurements_seconds)
median_time_squared = np.sum(measurements_seconds_squared)/len(measurements_seconds_squared)
variance_time = median_time_squared - np.power(median_time, 2)

print(f"La varianza estimada es: {variance_time}")

# b)
BINS = 20
plt.hist(measurements_seconds, bins=BINS, density=True)
plt.show()

# c)
def exponential_pdf(x, lambda_parameter):
    return lambda_parameter * np.exp(- lambda_parameter * x)

x_values = np.linspace(0, 10000, 50000)
y_values = exponential_pdf(x_values, 1/median_time)

plt.plot(x_values, y_values)
plt.show()