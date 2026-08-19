import numpy as np

sales = np.array([
    [10, 15, 20],
    [12, 10, 25],
    [15, 20, 15],
    [10, 20, 30]
])

print("Sales for each day:", sales.sum(axis=1))
print("Sales for each product:", sales.sum(axis=0))

best_day = sales.sum(axis=1).argmax() 
print("Best day number (starts from 0):", best_day)