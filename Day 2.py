# Tip calculator

print("Welcome to the tip calculator!")
total_bill = float(input("How much is the total bill ?\n$"))
tip_percentage = int(input("What percent tip would you like to give 10, 12 or 15%?\n%"))
no_of_people = int(input("Total number of people to split the bill?\n"))

total_bill += total_bill*tip_percentage/100
payment_person = round(total_bill/no_of_people,2)

print(f"Amount per person is ${payment_person}")
