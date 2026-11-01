# Reflection 1:
# The most surprising thing about lists is how easily they can be changed
# after they are created. I didn't realize Python had so many ways to add,
# remove, organize, and access items without rewriting the entire list.

# Reflection 2:
# At the US Open, a Python list could have helped keep track of equipment
# and supplies used across different courts. Instead of manually updating
# an Excel spreadsheet, I could use a list to organize items and find
# what was needed more quickly.


# EXERCISE 1 - Build the list

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))


# EXERCISE 2 - Index practice

print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])


# EXERCISE 3 - Slicing

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# EXERCISE 4 - Modify

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# EXERCISE 5 - Tuple comparison

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples are useful for coordinates because their values cannot be changed.")

print(coords)


# EXERCISE 6 - Average of a list of sales

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# EXERCISE 7 - Accumulator pattern

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print(prices)
print(discounted)


# EXERCISE 8 - Filter above threshold

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))