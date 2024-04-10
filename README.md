# Ultimate Battleships

Ultimate Battleships is a Python terminal game. Users can try to beat the computer by finding all of the computer's battleships before the computer find the player's. Each battleship occupies one square on the board.

Battleship (also known as Battleships or Sea Battle) is a strategy type guessing game for two players. It is played on ruled grids (paper or board) on which each player's fleet of warships are marked. The locations of the fleets are concealed from the other player. Players alternate turns calling "shots" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.

(Here is the Live version of my project.)[]

<img src = >

## How to play:

Ultimate battleship game is based on the classic pen-and-pencil game. Here is link for it to read more about it on (Wikipedia)[https://en.m.wikipedia.org/wiki/Paper-and-pencil_game]

In this version of the game, the player enters their name and two boards are randomley generated.

The player can see where their ships are, indicated by an @ sign, but cannot see where the computer's ships are.

Guesses are marked by an X on the board and Hits are marked by a *.

The player and computer takes turns to make guesses and try to sink each other's battleships.

The target is to sink 4 battleships first and whoever does so wins the game. 


## Features:

• Random board generation
• Ships are randomley placed on both the player and computer boards
• The player cannot see where the computer's ships are

<img src = >

• The player and computer then takes gueses by entering coordinate's on the board.
• A guess is maked by an X, and a Hit by *.
• After each hit the scoreboard is updated.

<img src = >

• The target is to sink all four ships in the fleet.
• First to hit four ships wins the game and is declared winner on the board.
• After the game ends, the computer asks the player if they want to play again. When yes is selected, the player enters their name and play. If the player chooses no, a message of "Thankyou for playing!" is displayed.

<img src = >

• Input validation and error checking.
You cannot enter coordinates outside the size of the grid
You must enter numbers
You cannot enter the same gues twice

<img src = >

## Future Featres:

• Allow player to select the board size and numberof ships.
• Allow player to position ships themselves.
• Allow selection of a larger fleet.

## Data Model:

I decided to use a Board class as my model. The game creates two instances of the Board class to hold the player's and the computer's board.

The Board class stores the board size, the number of ships, the position of the ships, the guesses against that board, and details such as board type (player's board or computer) and the player's name.

The class also has methods to help play the game, such as "print" method to print out the current board, an "add_ships" method to add ships to the board and an "add_guess" method to add a guess and return the result.


## Testing

I have manually tested this project by doing the following:

• Passed the code through a PEP8 linter and confirmed there are were some indentation errors that i corrected and there were no other problems.

• Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice

• Tested in my local terminal and the code institute Heroku terminal.

## Bugs 

### Solved bugs

• Indentation errors were reported when put through PEP3 and fixed immediately

• I was getting an Attribute error every time i entered a guess because the board guesses was treated as a list instead of a set. I fixed this by changing the self guess in the Board class to be used as a set. 

• I was getting index errors because the list were zero indexed. i fixed it by adding "size - 1" where necessary

## Remaining Bugs

• No bugs remaining

## Validator Testing 

• PEP8

No errors were returned from PEP8online.com

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

• Steps for deployment:

Fork or clone this repository
Create a new Heroku app
Set the buildbacks to Python and NodeJS in that order
Link the Heroku app to the repository
Click on Deploy

## Credits

• Code Institute for deployment terminal 

• Wikipedia for the details of the Battleships game
