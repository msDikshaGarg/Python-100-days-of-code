def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() != True:
    if front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()