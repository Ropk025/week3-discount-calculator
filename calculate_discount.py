def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If discount_percent is 20 or more, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Calculate and display the final price
    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"Discount applied! Final price: KES {final_price:.2f}")
    else:
        print(f"No discount applied. Original price: KES {original_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount.")