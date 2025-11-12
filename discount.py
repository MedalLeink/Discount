DISCOUNT_RATE = .1     #10% Discount
SALES_TAX_RATE = .06   #6% Sales Tax

subtotal = float(input("Enter the subtotal: $"))

discount = subtotal * DISCOUNT_RATE

subtotal -= discount

tax = subtotal * SALES_TAX_RATE

total = subtotal * SALES_TAX_RATE

print("--------- Your Order --------")
print(f"Subtotal: ${subtotal}")
print(f"Discount Received: ${discount}")
print(f"Sales Tax: ${tax}")
print(f"Total Amount Due: ${total}")

