#Exercise 1
def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")

#Exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    return price * (1 - discount)


price = 200

print(f"gold:   ${apply_discount(price, 'gold'):.2f}")
print(f"silver: ${apply_discount(price, 'silver'):.2f}")
print(f"bronze: ${apply_discount(price, 'bronze'):.2f}")
print(f"none:   ${apply_discount(price, 'none'):.2f}")

#Exercise 3
def calculate_tax(price, rate):
    return price * rate
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    return price * (1 - discount)
def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    return discounted_price + calculate_tax(discounted_price, tax_rate)
# Apply gold discount, then add tax
discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")
taxed = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${taxed:.2f}")
print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

#Exercise 4
def calculate_tax(price, rate):
    return price * rate
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    return price * (1 - discount)
def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    return discounted_price + calculate_tax(discounted_price, tax_rate)
# Loop through orders and print the sales report
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

#Exercise 5
# My explanation: This variable might contain the wrong type of value.
# Fix: I will check where the variable is assigned and correct it.

#Exercise 6
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # prints 100
print(double_it()) # prints 1998
print(x)           # prints 100

# Scope determines where a variable can be accessed.
# The x inside double_it() is local to that function,
# so changing it does not change the global x.

#1. The first bug I spotted was by reading the traceback and checking the code. It helped me understand where the problem was happening. I learned that I should slow down and check my code carefully before asking for help.
#2. The apply_discount(price, tier) function takes a price and a discount tier, such as gold, silver, or bronze. It calculates the discount based on the tier and returns the new price. A colleague could use it without reading the body if they knew what inputs to give it and what it returns.
#3. I used AI to help explain and understand some of the code in this lab. AI helped me learn what the code was doing, but I still needed to understand the answers so I could use them myself. It was helpful as a learning tool as long as I did not just copy the answers without understanding them.