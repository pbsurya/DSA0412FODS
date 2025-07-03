# Example item prices and quantities
prices = [50, 30, 20]         # Price of each item
quantities = [2, 1, 3]        # Quantity of each item

# Discount and tax rates (in percentages)
discount_rate = 10            # 10% discount
tax_rate = 5                  # 5% tax

# Step 1: Calculate subtotal (price * quantity)
subtotal = sum(p * q for p, q in zip(prices, quantities))

# Step 2: Apply discount
discount_amount = (discount_rate / 100) * subtotal
total_after_discount = subtotal - discount_amount

# Step 3: Apply tax
tax_amount = (tax_rate / 100) * total_after_discount
final_total = total_after_discount + tax_amount

print("Subtotal:", subtotal)
print("After Discount:", total_after_discount)
print("Final Total (with Tax):", final_total)
