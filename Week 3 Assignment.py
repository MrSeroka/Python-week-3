def calculate_discount(price: float, discount_percent: float) -> float:
   
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    else:
        final_price = price
    return final_price

def main():
    # Prompt the user for the original price
    price_input = input("Enter the original price of the item: ")
    # Prompt the user for the discount percentage
    discount_percent_input = input("Enter the discount percentage: ")
    
    try:
        # Convert inputs to float
        price = float(price_input)
        discount_percent = float(discount_percent_input)
        
        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)
        
        # Print the final price
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")

# Run the main function
if __name__ == "__main__":
    main()


