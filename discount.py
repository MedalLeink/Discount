from datetime import date

DISCOUNT_RATE = .1     #10% Discount
SALES_TAX_RATE = .06   #6% Sales Tax

discount = 0
today = date.today() #Get today's date from computer's operating system
day_of_the_week = 1 #today.weekday() #Return an int representing day of week (0 = Monday, 1 = Tuesday, ..., 7 = Sunday)


subtotal = float(input("Enter the subtotal: $"))
print("--------- Your Order --------")
print(f"Subtotal: ${subtotal}")

if day_of_the_week == 2 or day_of_the_week ==3:
    discount = subtotal * DISCOUNT_RATE
    print(f"Discount Received: ${discount}")

subtotal -= discount

tax = subtotal * SALES_TAX_RATE

total = subtotal + tax
print(f"Sales Tax: ${tax}")
print(f"Total Amount Due: ${total}")

