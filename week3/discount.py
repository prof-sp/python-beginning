'''This script calculates the final price by applying a discount based on the given percentage.
It prompts the user for the original price and the discount percentage,
 and checks if the discount is applicable or not.'''
 
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

price = float(input('Enter the original price: '))
discount_percent = float(input('Enter the discount percentage: '))

final_price = calculate_discount(price, discount_percent)

if final_price != price:
    print(f"Discount applied! Final price: {final_price}")
else:
    print(f"No discount applied. Price remains: {price}")


