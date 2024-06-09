import random


MAX_Lines = 3
MAX_Bet = 1000
MIN_Bet = 1

ROWS = 4
COLS = 4

symbol_count={
    "A": 6,
    "B": 4,
    "C": 8,
    "D": 4
}

def check_winnings(columns,lines,bet,value):
    winnings=0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_Check = column[line]
            if symbol != symbol_to_Check:
                break
        else:
            winnings  += value[symbol] * bet
            winning_lines.append(line+1)
    return winnings, winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(cols):
        column = []
        current_symbols= all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row], end=" ")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Please enter a number greater than 0")
        else:
            print("Please enter a valid amount")
    return amount

def get_no_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-"+str(MAX_Lines)+")?")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_Lines:
                break
            else:
                print("Enter a valid number: ")
        else:
            print("Please enter a number: ")
    return lines

def get_bet():
    while True:
        bet = input("Enter the bet amount: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_Bet<=bet<=MAX_Bet:
                break
            else:
                print(f"Enter a valid amount between ${MAX_Bet} and ${MIN_Bet}")
        else:
            print("Please enter a number: ")
    return bet

def spin(balance):
    lines = get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet* lines
        if total_bet>balance:
            print(f"You do not have enough to bet that amount. Your current balance${balance} ")
        else: break
    print(f"You have bet ${bet} on {lines} lines. The total bet is ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines =check_winnings(slots, lines,bet, symbol_count)
    print(f"You won ${winnings}")
    print(f"You won on", *winning_lines)
    return winnings-total_bet


def main():
    balance =  deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
main()
