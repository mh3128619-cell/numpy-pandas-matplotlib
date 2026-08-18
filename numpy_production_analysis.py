import numpy as np

production = np.array([120, 150, 110, 90, 160, 180, 85, 140, 200, 95])

production_of_first_3days=production[0:3]
print(f"The production of first 3 days is: {production_of_first_3days}")

the_lose_days=[i for i in production if i<100]
print(f"The lose days is: {the_lose_days}")

for i in range(len(production)):
    if production[i] < 100:
        production[i] = 100

print(production)
