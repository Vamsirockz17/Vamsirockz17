import matplotlib.pyplot as plt
import numpy as np

file_path = "weather_parameters.txt"

try:
    with open(file_path, "r") as file:
        days, temp_coeff, rain_coeff, init_temp, init_rain = map(float, file.read().splitlines())
except FileNotFoundError:
    print(f"File not found: {file_path}")
    days, temp_coeff, rain_coeff, init_temp, init_rain = 0, 0, 0, 0, 0
except ValueError as e:
    print(f"Error reading values from the file: {e}")
    days, temp_coeff, rain_coeff, init_temp, init_rain = 0, 0, 0, 0, 0

days_array = np.arange(1, int(days) + 1)
temperature = init_temp - temp_coeff * (days_array - 1) ** 2
rainfall = init_rain + rain_coeff * (days_array - 1) ** 2

plt.plot(days_array, temperature, label='Temperature')
plt.plot(days_array, rainfall, label='Rainfall')

plt.xlabel('Days')
plt.ylabel('Value')
plt.title('Weather Modeling with Quadratic Solution')
plt.legend()

plt.show()
