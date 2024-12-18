# [Battleships Seacode]

* Battleships Seacode is a Python Terminal Game, which runs on Heroku.
* Battleships Seacode is a simple Battleships game using python, which allows the user to play a game of Battleships against the computer.


## Screenshots

Below is a screenshot of Battleships Seacode created using the "Am I Responsive" website.

| Screenshot |

At the moment no screenshot because of problem with deployment...


## How to Play

* When the game is run, the player will be prompted to choose the size of the grid. For example, a 5x5 grid or a 10x10 grid.
* After the grid is displayed, the player will be asked to make a guess as to where they think the computers ship is located.
The players guess should be entered as two numbers seperated by a comma, representing the row and column, for example: (2,3)
* If the guess is correct, the player will be congratulated, and the game will end.
* If the player misses, the grid will be updated with and X at location of your guess to show you missed.
* The player has limited number of attempts to guess the ships location. If the player runs out of of attempts without hitting the ship, the game ends. After that, the location of the ship will be revealed.
* The game ends when the player hits the ship or runs out attempts. Once the player hits the ship, the player will be shown how many attempts it took to hit the ship.


## Features

* (Customizable Grid Size) The player can choose the grid size to adjust the difficulty of the game.
* (Random Ship Placement) The computer randomly place its ship on the grid at the start of each game.
* (User Friendly Interface) The game presents a simple grid where the player can track their guesses. Misses are marked with an X so the player can see their progress.
* (Limited Number of Attempts) The player has limited number of attempts adding and element of challenge.
* (Clear Instructions) The game provides clear feedback on weather your guess was a hit or a miss and prompts you to try again if your guess is off the grid or invalid.


### Features left to implement

* Due to time constraints, in the future I would like to add these further features.
* (Multiple Ships) Add the ability of the computer to place multiple ships on the grid, adding complexity.
* (Tracking Hits and Misses) Provide feedback on the number of hits and misses, show the the grid with missed and hit locations.
* (Score System) Keep track of the players score based on their performance.
* (Replay Feature) Add a feature to allow the player to replay the game after finishing, with either the same grid size or a new one. Add a prompt to ask if the player wants to play again.


## Data Model

* I have used a grid model, where the ship is hidden and the player has to guess its location. Misses are marked, and the game tracks the number of guesses, with a limit on attempts. 

* The print_grid shows the grid, create_grid creates the grid, place_computer_ship places the ship randomly, get_user_guess gets the players guess and main() runs the game, mangaging hits and misses.


## Testing

* Testing was conducted using PEP8.
* [PEP8](https://pep8ci.herokuapp.com/)


## Deployment

* (Steps for Deployment)
* Fork or clone this repository
* Create a new Heroku app
* Set the buildbacks to Python and NodeJS in that order
* Link the Heroku app to the reposistory
* Click on Deploy


## Tools & Technologies Used

* [W3Schools Python](https://www.w3schools.com/python/)


## Credits

* [For an Idea of how to Structure the game](https://www.youtube.com/watch?app=desktop&v=tF1WRCrd_HQ)
* [For an Idea of how to create a Battleships game in Python](https://bigmonty12.github.io/battleship)
* [W3Schools Python](https://www.w3schools.com/python/)


### Acknowledgements

* I would like to thank Code Institute for the course and support.
* I would like to thank my family for their help and support.