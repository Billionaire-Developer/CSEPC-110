#Compute the price of a meal as follows by asking for the price of child and adult meals, the number of each, and then the sales tax rate.
#Use these values to determine the total price of the meal.
#Then, ask for the payment amount and compute the amount of change to give back to the customer.


#Define variable
Child_meal = float(input("what is the price of a child's meal?: "))
adult_meal = float(input("what is the price of an adults meal?: "))
number_of_children = int(input("How many children are there?: "))
number_of_adult = int(input("how many adults are there?: "))

#Calculate subtotal
sub_total = ((number_of_children) * (Child_meal) + (number_of_adult) * (adult_meal))

#Ask for task rate
tax_rate = float(input("What is the sales tax rate?: "))

#Calculate sales task
sales_tax = sub_total * tax_rate / 100

#Calculate total
total = sub_total + sales_tax

#Ask for payment
payment_amount = float(input("What is the payment amount?: "))

#Calculate change
change = payment_amount - total

#Display result
print("subtotal: ${:.2f}".format(sub_total))
print("sales tax: ${:.2f}".format(sales_tax))
print("Total: ${:.2f}".format(total))
print("change: ${:.2f}".format(change))