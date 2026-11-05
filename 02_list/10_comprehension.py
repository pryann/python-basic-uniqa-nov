net_prices = [100, 1000, 2000, 500]
vat_rate = 1.27
# gross_prices = []

# for price in net_prices:
#     gross_prices.append(price * vat_rate)

# print(gross_prices)

gross_prices = [price * vat_rate for price in net_prices]
print(gross_prices)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd = [i for i in numbers if i % 2 != 0]
even = [i for i in numbers if i % 2 == 0]
print(even)
print(odd)

matrix = [[None for j in range(2)] for i in range(5)]
# for i in range(5):
#     row = []
#     for j in range(5):
#         row.append(j)
#     matrix.append(row)

print(matrix)

numbers = [i for i in range(100)]
print(numbers)
