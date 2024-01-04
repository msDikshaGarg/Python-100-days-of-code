# Printing greetings and art
art = """
                      __   __                 _                                     
 {}           {}      \ \ / /__  _   _ _ __  | |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
   \  _---_  /         \ V / _ \| | | | '__| | __| '__/ _ \/ _` / __| | | | '__/ _ \\
    \/     \/           | | (_) | |_| | |    | |_| | |  __/ (_| \__ \ |_| | | |  __/
     |() ()|            |_|\___/ \__,_|_|  _ _\__|_|  \___|\__,_|___/\__,_|_|  \___|
      \ + /                 __ ___      ____ _(_) |_ ___   _   _  ___  _   _            
     / HHH  \             / _` \ \ /\ / / _` | | __/ __| | | | |/ _ \| | | |           
    /  \_/   \           | (_| |\ V  V / (_| | | |_\__ \ | |_| | (_) | |_| |           
  {}          {}          \__,_| \_/\_/ \__,_|_|\__|___/  \__, |\___/ \__,_|       
                                                          |___/          \n\n          
"""
play_again = True

def try_again():
    again = input("Type 'yes' to try again and 'no' to quit.\n")
    while again not in ['yes', 'no']:
        again = input("Please enter a valid input.\n").lower()
    if again == 'yes':
        return True
    else:
        return False

# Taking choices as inputs and choosing the next steps based on user choices
while play_again != False:
    #print(art)
    print(art)
    print("Welcome to treasure island. We have hidden a secret treasure somewhere on this island, your task is to find the treasure.")
    ch1 = input("You come across a fork in the road, do you go left or right?\n").lower()
    while ch1 not in ['left', 'right']:
        ch1 = input("Please enter a valid input.\n").lower()
    if ch1 != "left": 
        print("You fell into a hole and died. Try again.")
        play_again = try_again()
    else: 
        ch2 = input("You come across an algae lake, do you wait or swim across?\n").lower()
        while ch2 not in ['swim', 'wait']:
            ch2 = input("Please enter a valid input.\n").lower()
        if ch2 != "wait":
            print("Sorry, the piranhas got to you. Try again.")
            play_again = try_again()
        else:
            ch3 = input("Now there are the doors of truth upon you. Choose wisely. Do you choose red, blue or the yellow door?\n")
            while ch3 not in ['red', 'blue', 'yellow']:
                ch3 = input("Please enter a valid input.\n").lower()
            if ch3 == "red":
                print("You were incinerated by fire. Better luck next time!")
                play_again = try_again()
            elif ch3 == "blue":
                print("Today, you filled up a beast's belly. The beast thanks you. Try again.")
                play_again = try_again()
            elif ch3 == "yellow":
                print("Congratulations! You are now a million dollars richer!")
                play_again = False
         