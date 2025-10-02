# question1.py

name= input("enter your name:")

age = int(input("enter your age:"))

quantity = int(input("How many tickets do you want?:"))

#ticket pricing

if age < 13: 
    ticket_type = "child"
    price = 8.00

elif age <= 64:
    ticket_type = "adult"
    price = 12.00
else:
    ticket_type = "senior"
    price = 9.00

    #how to calculate
total_cost = price * quantity

#print receipt
print("===Movie Ticket Receipt ===")

print(f"customer: {name}")jay
print(f"ticket type: {ticket_type} (${price: .2f} each)")
print(f"'quantity: {quantity}")
print(f"total_cost: ${total_cost: .2f}")
print("Thasnk you for your purchase!")