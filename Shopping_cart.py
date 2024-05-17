print("welcome to the shopping cart program!")
print()
print("""
      please select one of the following:
      ----------------------------------
      1. Add item
      2. view cart
      3. Remove item
      4. Compute total
      5. Quit
      """)
shopping_cart = []
prices = []
option = int(input("Please enter an option"))

while option != 5 and option != "Quit":
    if option == 1:
        item = input("\nwhat item would you like to add?")
        shopping_cart.append(item)
        price = float(input(f"\nwhat is the price of '{item}'? "))
        prices.append(price)
        print(f"\n'{item}' has been added to the cart.")
        
    elif option == 2:
        print("\nThe contents of the shopping cart are: ")
        for item in range(len(shopping_cart)):
            print(f"\n{item+1}. {shopping_cart[item]} - ${prices[item]:.2f} ")
            
    elif option == 3:
        remove_item = int(input("\nPlease which item would you like to remove? ")) -1
        del(shopping_cart[remove_item] )
        del(prices[remove_item])
        print(f"\n{remove_item}. item removed")
        
    elif option == 4:
        sum = 0
        for number in prices:
            sum += number
            print(f"\nThe total price of the item in shopping cart is $ {sum:.2f}")
            
            option = int(input("\nPlease enter an action: "))
    else:
            print("\Thank you. Goodbye!")