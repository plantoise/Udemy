print("Welcome to the top calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
total_with_tip = tip / 100 * bill + bill
bill_each_person = total_with_tip / split
final_amount = round(bill_each_person, 2)
final_amount = "{:.2f}".format(bill_each_person)
print(total_with_tip)
print(f"Each person should pay {final_amount}$")