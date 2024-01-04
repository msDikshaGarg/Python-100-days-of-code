import os
# Tip calculator
# Greeting

art = """
  ____ _                                               
 / ___| |__   ___  __ _ _   _  ___                     
| |   | '_ \ / _ \/ _` | | | |/ _ \                    
| |___| | | |  __/ (_| | |_| |  __/                    
 \____|_| |_|\___|\__, |\__,_|\___|                    
                 _   |_|   _             _             
 _ __ ___   __ _| |_| |__ (_)_ __   __ _| |_ ___  _ __ 
| '_ ` _ \ / _` | __| '_ \| | '_ \ / _` | __/ _ \| '__|
| | | | | | (_| | |_| | | | | | | | (_| | || (_) | |   
|_| |_| |_|\__,_|\__|_| |_|_|_| |_|\__,_|\__\___/|_|   
 ____   ___   ___   ___                                
|___ \ / _ \ / _ \ / _ \                               
  __) | | | | | | | | | |                              
 / __/| |_| | |_| | |_| |                              
|_____|\___/ \___/ \___/        \n\n
"""

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