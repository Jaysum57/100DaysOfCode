print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10%, 12%, or 15%? ")) / 100
people = int(input("How many people to split the bill? "))

payment = (bill * (1 + tip))/people
rounded_payment = "{:.2f}".format(payment)

print(f"Each person should pay: ${rounded_payment}")