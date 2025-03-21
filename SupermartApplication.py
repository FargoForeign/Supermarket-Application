print("Welcome to My Supermarket!")
print("What do you want? Choose a category:")

categories = {
    1: "Beverages",
    2: "Liquor",
    3: "Cars",
    4: "Clothing & Accessories",
    5: "Kitchen Utensils"
}

items = {
    "Beverages": [("Bread", 2000), ("Tea", 1500), ("Coffee", 1000), ("Juice", 1000), ("Water", 500)],
    "Liquor": [("Beer", 800), ("Hennessy", 500), ("Martel", 1200), ("Red Label", 1500), ("Don Julio", 1000)],
    "Cars": [("KIA", 30000), ("Chevolet", 20000), ("Toyota", 25000), ("Mercedez Benz", 15000), ("Honda", 10000)],
    "Clothing & Accessories": [("Jeans", 1500), ("Shirt", 1500), ("Shoes", 1700), ("Skirt", 1000), ("Trousers", 1500)],
    "Kitchen Utensils": [("plate", 500), ("Pot", 300), ("Cup", 200), ("Spoon", 150), ("Fork", 100)]
}

cart = []
total_price = 0

while True:
    print("\nAvailable categories:")
    for key, category in categories.items():
        print(f"{key}: {category}")
    print("6: Show your cart")
    print("7: Checkout and Exit")

    try:
        choice = int(input("\nEnter the number of your category or option: "))

        if choice == 7:
            break
        elif choice == 6:
            if cart:
                print("\nYour current cart:")
                for item in cart:
                    print(f"- {item}")
                print(f"Total so far: ${total_price}")
            else:
                print("\nYour cart is empty.")
        elif choice in categories:
            selected_category = categories[choice]
            print(f"\nYou selected {selected_category}.")
            print("Available:")
            for idx, (item, price) in enumerate(items[selected_category], start=1):
                print(f"{idx}: {item} - ${price}")

            while True:
                item_choice = int(input("\nChoose an item by number (or 0 to go back to categories): "))

                if item_choice == 0:
                    break
                elif 1 <= item_choice <= len(items[selected_category]):
                    selected_item, item_price = items[selected_category][item_choice - 1]
                    cart.append(selected_item)
                    total_price += item_price
                    print(f"Added {selected_item} to your cart. Total: ${total_price}")
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid category or option. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if cart:
    print("\nYour final cart:")
    for item in cart:
        print(f"- {item}")
    print(f"Total price: ${total_price}")


    print("\nTo proceed with checkout, provide the following details.")
    email = input("Enter your email: ")
    card_number = input("Enter your credit card number: ")
    card_expiry = input("Enter your card expiry date (MM/YY): ")
    card_cvv = input("Enter your card CVV: ")

    print("\nProcessing your payment...")
    print("\nPayment successful!")
    print(f"A receipt has been sent to {email}.")
else:
    print("\nYour cart is empty.")

print("\nThank you for shopping with us!")
