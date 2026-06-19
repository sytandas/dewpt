import math

temperature = float(input("Enter temperature (°C): "))
humidity = float(input("Enter relative humidity (%): "))

a = 17.27
b = 237.7

alpha = ((a * temperature) / (b + temperature)) + math.log(humidity / 100.0)
dew_point = (b * alpha) / (a - alpha)

print(f"Dew Point: {dew_point:.2f} °C")
