import numpy as np

production = np.array([420, 380, 510, 290, 460, 530, 350])

production_of_first_3days=production[0:3]
print(f"The production of first 3 days is: {production_of_first_3days}")

for i in production:
    if i <400:
        print(i)

for i in range(len(production)):
    if production[i]<400:
        production[i]=400

print(production)

print(production.sum())
print(production.max())
print(production.min())
print(production.sum()/len(production))
print(production.argmax() +1)
