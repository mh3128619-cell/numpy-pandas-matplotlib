import numpy as np

sales = np.array([
    [120,  80, 150, 200,  90],
    [100,  95, 130, 180, 110],
    [160,  70, 170, 210, 100],
    [ 90,  60, 120, 150,  80],
    [180, 110, 190, 220, 130],
    [200, 100, 210, 250, 140],
    [170,  85, 180, 230, 120]
])

first_3_days = sales[:3, :]
print(first_3_days)

chicken_sales = sales[:, 3]
print(chicken_sales)

weak_chicken = chicken_sales[chicken_sales < 200]
print(weak_chicken)

daily_totals = np.sum(sales, axis=1)
print(daily_totals)

product_totals = np.sum(sales, axis=0)
print(product_totals)

best_product_index = np.argmax(product_totals)
print(best_product_index)

weak_days_indices = np.where(daily_totals < 600)[0]
print(weak_days_indices)
