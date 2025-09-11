"""A simple program to calculate the final purchase amount with a discount."""

price = float(input("Enter product price: "))
discount = float(input("Enter discount (%): "))
quantity = float(input("Enter quantity: "))

total_price = price * quantity
discount_amount = total_price * discount / 100

if total_price > 10_000:
    print("Discount does not apply")
    print(f"{total_price:.2f}")
else:
    final_price = total_price - discount_amount
    print(f"{final_price:.2f}")
