import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

measurements_microseconds = np.loadtxt("geiger.csv",
                 delimiter=",", dtype=int)

# a)
last_value = 0
time_delta = []
for i in range(len(measurements_microseconds)):
    time_delta.append(measurements_microseconds[i] - last_value)
    last_value = measurements_microseconds[i]

measurements_time_delta = np.array(time_delta)

# Para determinar la media, se promedian todas las realizaciones:
median_time = np.sum(measurements_time_delta)/len(measurements_time_delta)

print(f"La esperanza estimada es: {median_time}")

# Para determinar la varianza, estimamos la esperanza de las realizaciones al cuadrado,
# elevamos la estimacion previa al cuadrado y aplicamos la formula de varianza.

def power_of_two(x):
    return np.power(x, 2)

measurements_time_delta_squared = np.apply_along_axis(power_of_two, 0, measurements_time_delta)
median_time_delta_squared = np.sum(measurements_time_delta_squared)/len(measurements_time_delta_squared)
variance_time = median_time_delta_squared - np.power(median_time, 2)

print(f"La varianza estimada es: {variance_time}")

# b)
sns.histplot(measurements_time_delta)
plt.show()

# c)
def exponential_pdf(x, lambda_parameter):
    return lambda_parameter * np.exp(- lambda_parameter * x)

x_values = np.linspace(0, 7000000, 20000000)
y_values = exponential_pdf(x_values, 1/median_time)

plt.plot(x_values, y_values)
plt.show()