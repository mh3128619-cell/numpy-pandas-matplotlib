import numpy as np


customers = np.array([
    [22, 5000, 12, 1],
    [35, 12000, 24, 0],
    [28, 8000, 18, 1],
    [45, 25000, 36, 0],
    [31, 15000, 12, 1],
    [52, 30000, 48, 0],
    [26, 7000, 24, 1],
    [40, 18000, 36, 0],
    [29, 9500, 18, 1],
    [60, 40000, 60, 0]
])


print(f"The ages of all customers are: {customers[:, 0]}")
print("-" * 45)

print(f"The monthly income of all customers is: {customers[:, 1]}")
print("-" * 45)

print(customers[:, 1] > 15000)
print("-" * 45)

print(customers[:, 3] == 1)
print("-" * 45)

print(customers[:, 1].mean())
print("-" * 45)

print(customers[:, 1].max())
print(customers[:, 1].argmax())
print("-" * 45)

risky_customers = customers[
    (customers[:, 3] == 1) & (customers[:, 1] < 10000)
]

print(risky_customers)
print("-" * 45)

VIP_customers = customers[
    (customers[:, 1] > 20000) & (customers[:, 0] >= 40)
]

print(VIP_customers)
print("-" * 45)

loan_customers_avg_income = customers[
    customers[:, 3] == 1, 1
].mean()

print(loan_customers_avg_income)
print("-" * 45)

not_loan_customers_avg_income = customers[
    customers[:, 3] == 0, 1
].mean()

print(not_loan_customers_avg_income)
