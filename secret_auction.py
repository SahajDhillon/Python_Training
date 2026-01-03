auction = True
bids = {}
while auction:
    name = input("What is your name: ")
    bid = input("How much will you bid: $")
    bids[name] = bid
    user = input("Are there another bidders? ")
    if user.lower() == 'yes':
        print("\n" * 20)
    else:
        auction = False

highest_value = max(bids.values())
winner = [k for k, v in bids.items() if v == highest_value][0]
print(f"The winner is {winner}")

