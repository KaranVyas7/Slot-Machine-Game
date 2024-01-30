import random

# Constants for the game
MAX_LINES=3
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3

# Dictionary defining the count of each symbol in the slot machine
symbol_count={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Dictionary defining the count of each symbol in the slot machine
symbol_value={
     "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

'''
    Checks for winning combinations in the slot machine.

    Parameters:
        columns (list): The columns of the slot machine.
        lines (int): Number of lines the player is betting on.
        bet (int): The bet amount per line.
        values (dict): Symbol values.

    Returns:
        tuple: Total winnings and winning lines.
'''
def checkWinnings(columns,lines,bet,values):
    winnings=0
    winningLines= []
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            winningLines.append(line+1)
    return winnings,winningLines

'''
Generates a random spin for the slot machine.

    Parameters:
        rows (int): Number of rows in the slot machine.
        cols (int): Number of columns in the slot machine.
        symbols (dict): Symbol count.

    Returns:
        list: Columns representing the slot machine spin.
'''
def getSlotMachineSpin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

'''
    Prints the slot machine spin.

    Parameters:
        columns (list): Columns representing the slot machine spin.
'''
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

'''
    Handles player deposit.

    Returns:
        int: Player's deposit amount.
'''
def deposit():
    while True:
        amount=input("What would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0!")
        else:
            print("Please enter a number!")
    return amount

'''
Gets the number of lines the player wants to bet on.

Returns:
    int: Number of lines.
'''
def getNumLines():
    while True:
        lines=input("Enter the number of lines you would like to bet on (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Enter a valid number of lines!")
        else:
            print("Please enter a number!")
    return lines

'''
    Gets the bet amount per line from the player.

    Returns:
        int: Bet amount.
'''
def getBet():
    while True:
        bet=input("What would you like to bet on each line? $")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET<bet<MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}.")
        else:
            print("Please enter a number!")
    return bet

'''
    Simulates a spin in the slot machine.

    Parameters:
        balance (int): Current balance of the player.

    Returns:
        int: Remaining balance after the spin.
'''
def spin(balance):
    lines = getNumLines()
    while True:
        bet = getBet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = getSlotMachineSpin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = checkWinnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

'''
    Main function to run the slot machine game.
'''
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()

