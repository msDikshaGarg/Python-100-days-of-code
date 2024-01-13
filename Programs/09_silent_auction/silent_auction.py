# Importing relevant libraries and files
import os
from artwork import art, horse

# Empty dictionary to keep track of user bids, other bidder flag to keep check if further bidders exist
bids_dict = {}
other_bidder = True

# Function to loop through the bids and print the person with the highest bid
def find_max_bid(bids_dict):
    max_name = ''
    max_bid = 0 
    for key in bids_dict:
        if bids_dict[key] > max_bid:
            max_bid = bids_dict[key]
            max_name = key
    print(f"The winner of this bid is {max_name} with a bid of ${max_bid}.")

# While other bidders exist
while other_bidder != False:
    # Print greeting for each bidder
    print(art)
    print("Thank you for taking part in the silent auction for this exquisite rocking horse from the mid 18th century.")
    print(horse)
    print("Let's enter your bid in the system.")

    # Take bid and bidder info
    name = input("What's your name?\n")
    bid = int(input("What's your bid?\n$ "))
    
    # Add the bid to dictionary
    bids_dict[name] = bid

    # Asking if other bidders exist     
    more = input("Are there other bidders? Yes/No.\n").lower()

    # If invalid input then continue asking for proper inputs
    while more not in ['yes', 'no']:
        more = input("Sorry was that a yes or no?")
        # If no more bidders then change other bidder flag and exit the loop
    if more == 'no':
        other_bidder = False
    # Clear the screen 
    os.system('clear')
# Print the winner of auction via function
find_max_bid(bids_dict)
