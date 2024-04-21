
# US States Game

![US States](../../GIFs/giphy-squirtle-glasses.gif)

A fun game of Guessing the US States inspired by [Sporcle's, Can you name the US states?](https://www.sporcle.com/games/g/states) using pandas. 

### 50 States CSV
Contains the list of states with their coordinates, supplied by the Dr. Angela Yu.

### Blank States Image
A background image for turtle, supplied by Dr. Angela Yu.

### States Game
The blank US states image is displayed in the background when the game starts. The data is read from the 50 states CSV and the state names are stored in a list. Till all the states are guessed in the list, the game offers a pop up box with the score and a textbox to guess a state name. If the state name is correct it gets written at the appropriate place on the map and the score increases in the next pop up box. If the player guessed incorrectly they get the chance to guess again. 

On typing 'exit' the player can exit the game and the un-guessed states are stored in a new CSV. If the player guessed all the states, the game prints a win message on the screen.
