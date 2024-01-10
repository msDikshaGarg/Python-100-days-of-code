import os
from artwork import art
# Tip calculator
# Greeting

print(art)

# Bill amount
print("What's the total bill?")
bill = float(input("$ "))

# Split
print("How many people are paying today?")
split = int(input())

# Tip
print("What '%' do you want to tip today? 15 18 20 22")
tip = int(input())

# Total per person
total = round((bill + (bill*tip)/100) / split, 2)
print(f"Your total per person is ${total}.")