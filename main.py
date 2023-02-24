import random

# Set up the deck of cards
suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
deck = []

for suit in suits:
    for rank in ranks:
        deck.append(rank + " of " + suit)

# Shuffle the deck
random.shuffle(deck)

# Set up the game board
board = {
    "Stock": deck,
    "Waste": [],
    "Foundation Hearts": [],
    "Foundation Diamonds": [],
    "Foundation Clubs": [],
    "Foundation Spades": [],
    "Tableau 1": [],
    "Tableau 2": [],
    "Tableau 3": [],
    "Tableau 4": [],
    "Tableau 5": [],
    "Tableau 6": [],
    "Tableau 7": []
}

# Deal the cards
for i in range(1, 8):
    for j in range(i):
        board[f"Tableau {i}"].append(board["Stock"].pop(0))

board["Waste"].append(board["Stock"].pop(0))

# Define functions to handle player input and game rules
def draw_card():
    if len(board["Stock"]) > 0:
        board["Waste"].append(board["Stock"].pop(0))
    else:
        board["Stock"] = board["Waste"][::-1]
        board["Waste"] = []
        board["Waste"].append(board["Stock"].pop(0))

def move_card(from_pile, to_pile):
    if len(board[from_pile]) > 0:
        card = board[from_pile][-1]
        if len(board[to_pile]) == 0:
            if card.split()[0] == "Ace":
                board[to_pile].append(board[from_pile].pop())
            else:
                print("Invalid move.")
        else:
            to_card = board[to_pile][-1]
            if card.split()[1] != to_card.split()[1]:
                print("Invalid move.")
            else:
                if ranks.index(card.split()[0]) == ranks.index(to_card.split()[0]) + 1:
                    board[to_pile].append(board[from_pile].pop())
                else:
                    print("Invalid move.")
    else:
        print("Invalid move.")

def move_card_to_foundation(from_pile, to_pile):
    if len(board[from_pile]) > 0:
        card = board[from_pile][-1]
        if len(board[to_pile]) == 0:
            if card.split()[0] == "Ace":
                board[to_pile].append(board[from_pile].pop())
            else:
                print("Invalid move.")
        else:
            to_card = board[to_pile][-1]
            if card.split()[1] != to_card.split()[1]:
                print("Invalid move.")
            else:
                if ranks.index(card.split()[0]) == ranks.index(to_card.split()[0]) + 1:
                    board[to_pile].append(board[from_pile].pop())
                else:
                    print("Invalid move.")
    else:
        print("Invalid move.")

def is_game_over():
    if len(board["Stock"]) == 0:
        for pile in ["Foundation Hearts", "Foundation Diamonds", "Foundation Clubs", "Foundation Spades"]:
            if len(board[pile]) != 13:
                return False
        return True
    else:
        return
