import numpy as np

orders = np.array([
    [500,  2, 4.5, 10],
    [1200, 1, 4.8,  5],
    [300,  5, 3.9, 15],
    [800,  3, 4.2,  0],
    [1500, 2, 4.9, 20],
    [250,  8, 3.5, 25],
    [950,  1, 4.6, 10],
    [2000, 1, 4.7, 30]
])

original_total = orders[:, 0] * orders[:, 1]
print("1. Original Totals:", original_total)
print("-" * 45)

discount_amount = orders[:, 0] * (orders[:, 3] / 100)
print("2. Discount Amounts:", discount_amount)
print("-" * 45)

final_total = original_total - discount_amount
print("3. Final Totals:", final_total)
print("-" * 45)

large_orders = orders[original_total > 2000]
print("4. Large Orders:\n", large_orders)
print("-" * 45)

big_discount_orders = orders[orders[:, 3] >= 20]
print("5. Big Discount Orders:\n", big_discount_orders)
print("-" * 45)

print("6. Average Rating:", orders[:, 2].mean())
print("-" * 45)

print("7. Max Original Order Value:", original_total.max())
print("   Max Order Index:", original_total.argmax())
print("-" * 45)

final_above_1500_indices = np.where(final_total > 1500)[0]
print("8. Indexes of Final Total > 1500:", final_above_1500_indices)
print("-" * 45)

high_value_orders = orders[(original_total > 1500) & (orders[:, 2] >= 4.5)]
print("9. High Value Customer Orders:\n", high_value_orders)
