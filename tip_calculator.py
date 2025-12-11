print("Tip Calculator\n")
bill = int(input("Enter your bill: \n"))
tip = int(input("Enter tip: \n"))
people = int(input("How many person do you want to split the bill?\n"))

total_amount = (tip/100 * bill) + bill
after_split = total_amount/people

print(f"Your total amount is ${total_amount} and each person owes ${after_split}")
#