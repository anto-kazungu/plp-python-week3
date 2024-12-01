# Prompt the user for inputs
print("Welcome to the discount calculator!")

original_price_input = input("Enter the original price of the item: ")
discount_percentage_input = input("Enter the discount percentage: ")

#Function defination
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
    price: The original price of the item.
    discount_percent: The discount percentage to be applied.
    
    Returns:
    float: The final price after applying the discount, or the original price if no discount is applied.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Check if inputs are numeric
if original_price_input.isdigit() and discount_percentage_input.isdigit():
    original_price = float(original_price_input)
    discount_percentage = float(discount_percentage_input)

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if final_price < original_price:
        print(f"The final price after applying the discount is: Ksh.{final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: Ksh.{original_price:.2f}")
else:
    print("Please enter valid numbers for the price and discount percentage.")



