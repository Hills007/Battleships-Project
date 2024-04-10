from random import randint
scores = {"computer": 0, "player": 0}
class Board:
    def __init__(self, size, num_ships, name, board_type):
        self.size = size
        self.board = [["." for _ in range(size)] for _ in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = board_type
        self.guesses = set()
        self.ships = []

    def display(self):
        for row in self.board:
            print(" ".join(row)) 

    def guess(self, x, y):
        if ( x, y) in self.guesses:
            print("You cannot use the same coordinate twice.")
            return "Invalid"

        else:    
            self.guesses.add((x, y))
            self.board[x][y] = "X"
            if (x, y) in self.ships:
                self.board[x][y] = "*"
                return "Hit"
            else:
                return "Miss"

    def add_ship(self, x, y):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
            return
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"

    def display_ships(self):
        for ship in self.ships:
            x, y = ship
            self.board[x][y] = "@"

def random_point(size):
    return randint(0, size-1)  

def valid_coordinates(x, y, board):
    return 0 <= x < board.size and 0 <= y < board.size

def populate_board(board):
    for _ in range(board.num_ships):
        x = random_point(board.size)
        y = random_point(board.size)
        while (x, y) in board.ships:
            x = random_point(board.size)
            y = random_point(board.size)
        board.add_ship(x, y)

def make_guess(board):
    while True:
        try:

            x = int(input("Enter row number to guess: "))
            y = int(input("Enter column number to guess: "))
            if not valid_coordinates(x, y, board):
                print("Invalid coordinates. Please try again.")
                continue
            if (x, y) in board.guesses:
                print("You cannot use the same coordinate twice.")
                continue
            break
        except ValueError:
            print("You must enter a number.")
    result = board.guess(x, y)
    print(result)
    board.display()
    return result

def display_score():
    print("Current Score:")
    print(f"Player: {scores['player']} | Computer: {scores['computer']}")
    
def play_game(computer_board, player_board):
    player_ships_hit = 0
    computer_ships_hit = 0
    while player_ships_hit < computer_board.num_ships and computer_ships_hit < player_board.num_ships:
        print("Player's turn:")
        result = make_guess(computer_board)
        if result == "Hit":
            player_ships_hit += 1
            scores["player"] += 1
            if player_ships_hit == computer_board.num_ships:
                print("Player wins!")
                break
    # Computer's turn
        print("Computer's turn:")
        x = random_point(player_board.size)
        y = random_point(player_board.size)
        result = player_board.guess(x, y)
        print(f"Computer guesses: ({x}, {y}) - {result}")
        if result == "Hit":
            computer_ships_hit += 1
            scores["computer"] += 1
            if computer_ships_hit == player_board.num_ships:
                print("Computer wins!")
                break
        # Display computer's guess on player's board
        player_board.display()
        print("Computer's board:")
        computer_board.display()
        # Diplay score after each round
        display_score()
def new_game():
    size = 5
    num_ships = 4
    scores["player"] = 0
    scores["computer"] = 0   
    print("_" * 35)
    print("Welcome to ULTIMATE BATTLESHIPS!!")
    print(f"Board Size: {size}. Number of ships: {num_ships}")
    print("Top left corner is row: 0, col: 0")
    print("_" * 35)
    player_name = input("Please enter your name: \n")
    print("_" * 35)

    computer_board = Board(size, num_ships, "Computer", board_type="computer")
    player_board = Board(size, num_ships, player_name, board_type="player")


    populate_board(computer_board)

            # Populate player's board
    populate_board(player_board)
        # Display player's ships
    player_board.display_ships()  
    player_board.display()

    play_game(computer_board, player_board)

    #Add a Restart funtion after game ends
    restart = input("Do you want to play again? (yes/no): ")
    if restart.lower() == "yes":
        new_game()
    else:
        print("Thank you for playing!")

new_game()
