## Code for the maze 

# Function to make a right turn
def turn_right():
    turn_left()
    turn_left()
    turn_left()
# Counter for right turns and forward steps
countr = 0
countf = 0
# While the robot Reeborg didn't reach goal
while at_goal() != True:
    # If there have been more than 2 right turns and no forward turns yet that means the Reeborg is stuck in a loop
    if countr > 2 and countf == 0:
        # If Reeborg is stick check if front is clear, then move
        if front_is_clear():
            move()
        else: 
            # Make a left turn and follow the next steps
            turn_left()
    # If right is clear then move right, the logic is to follow along the right edge of the maze till Reeborg reaches the goal
    if right_is_clear():
        turn_right()
        move()
        countr +=1
    # If front is clear then move front
    elif front_is_clear():
        move()
        countf +=1
    else: 
        # Else turn left when no other choice
        turn_left()