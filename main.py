import random 

cards_game = ['2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K", "A"]

def count(cards, som):
    for card in cards:
        if card.isnumeric(): som += int(card)
        elif card == "A":
            if som + 11 <= 21: som += 11
            else: som += 1 
        else: som += 10
    
    return som 

def start(gamer, computer):
    for i in range(2):
        gamer.append(random.choice(cards_game))
        computer.append(random.choice(cards_game))

def game(cards):
    for i in range(1):
        cards.append(random.choice(cards_game))

def game_computer(computer_cards, count_gamer, count_computer):
    while True:
        print(f"\ncomputer cards: {computer_cards}: {count_computer}")
        if count_computer > 21: return ('gamer win', count_computer)
        elif count_computer == count_gamer and count_computer >= 17: return ('draw', count_computer)
        elif count_computer > count_gamer: return ('computer wins', count_computer)
        if count_computer < 17: 
            game(computer_cards)
            count_computer = count([computer_cards[-1]], count_computer)
        elif count_gamer > count_computer: return ('gamer win', count_computer)
        
my_cards = []
computer_cards = []
start(my_cards, computer_cards)
START_COUNT = 0
count_gamer = count(my_cards, START_COUNT)
count_computer = count(computer_cards, START_COUNT)
first_computer_card = count([computer_cards[0]], START_COUNT) # to show

while True:
    print(f"\nyour cards: {my_cards}: {count_gamer}")
    print(f"computer first card: '{computer_cards[0]}': {first_computer_card} \n")
    move = input("click 'n' for one more card or click 'e' for end the turn \n")
    if move == 'n':
        game(my_cards)
        count_gamer = count([my_cards[-1]], count_gamer)
        if count_gamer > 21: 
            result = ("computer wins", None)
            break
    elif move == 'e':
        result = game_computer(computer_cards, count_gamer, count_computer)
        count_computer = result[1]
        break

print("\n-----------------------------------------------\n")
print(f"your cards: {my_cards}: {count_gamer}")
print(f"computer cards: {computer_cards}: {count_computer}")
print(result[0])