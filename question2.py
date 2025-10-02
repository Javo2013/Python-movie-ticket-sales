#Question 2.py

#Menu & prices
menu = {
    1:("pizza",15.99),
    2:("burger",12.50),
    3:("salad",9.99),
    4:("pasta",13.75)
}

#Display menu
print("=== restaurant menu ===")
for num, (food,price) in menu.items():
  print(f"{num}. {food} - ${price: .2f}")


#user choice
choice = int(input("Enter your choice (1-4)"))
food, price = menu [choice]

#drink option
drink_choice = input("would you like a drink? (+$2.50) (yes/no):")
drink_price = 2.50 if drink_choice =="yes" else 0.00

#total & tax
subtotal = price + drink_price
tax = subtotal * 0.08
total = subtotal + tax

#bill

print ("\n=== Your Order Details===")
print (f"food: {food} - $ {price: .2f}")
print (f"drink: {'yes' if drink_choice == 'yes' else 'no'} - ${drink_price: .2f}")
print(f"subtotal: ${subtotal: .2f}")
print(f"tax (8%): ${tax:.2f}")
print(f"total: ${total:.2f}")
