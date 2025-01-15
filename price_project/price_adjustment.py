from data import product
import copy

# 1. Increase the prices of the product by 10%
new_products = copy.deepcopy(product)  # Deep copy
for product in new_products:
    # Increase the price by 10% and round to 2 decimals
    product['price'] = round(product['price'] * 1.10, 2)


# 3. Sort the product by price in ascending order
products_sorted_by_price = copy.deepcopy(new_products)  # Deep copy
products_sorted_by_price.sort(key=lambda x: x['price'])

# Display the results
print("New product (prices increased by 10%):")
for product in new_products:
    print(f"Name: {product['name']}, Price: ${product['price']:.2f}")

print("\nProducts sorted by price (ascending):")
for product in products_sorted_by_price:
    print(f"Name: {product['name']}, Price: ${product['price']:.2f}")
