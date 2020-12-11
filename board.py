COL_LENGTH = 10

class Board:
    # Constructor for the board class
    def __init__(self, answer):
        self.rows = []
        self.answer = answer
        self.win = False
        self.lose = False

    # Method to input a given play to the board
    def input_play(self, p):
        self.rows.append(p)
        self.process_play(p)

    # Method to process the results of a play
    def process_play(self, p):
        # If all 4 match, the player has won
        if p.red == 4:
            self.win = True
        # Else, check to make sure they have more guesses
        else:
            if len(self.rows) == 10:
                self.lose = True

        # Display the board to the user
        self.display_board()

    # Method that prints out the board to the console
    def display_board(self):
        # Print every guess that has been made so far
        for i in range(0, len(self.rows)):
            self.rows[i].printout()

        # For every empty row of the board, print out blank guesses
        if len(self.rows) != COL_LENGTH:
            for i in range(len(self.rows), COL_LENGTH):
                print("0 0 0 0 - R:0 W:0")




