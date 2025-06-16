import random
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['H', 'S', 'D', 'C']
GAMES_TO_WIN = 3
WINNING_SCORE = 21
DEALER_THRESHOLD = 17

def shuffle(deck):
    random.shuffle(deck)

def prompt(text):
    print(f'==> {text}')

def initialize_deck():
    deck = [[suit, card] for suit in SUITS for card in CARDS]
    return deck

def total(cards):
    sum_val = 0
    values = [card[1] for card in cards]
    for value in values:
        if value == 'A':
            sum_val += 11
        elif value in ['J', 'Q', 'K']:
            sum_val += 10
        else:
            sum_val += int(value)
    aces = values.count('A')
    while sum_val > WINNING_SCORE and aces:
        sum_val -= 10
        aces -= 1
    return sum_val


def deal_card(hand_1, hand_2):
    cards_dealt = len(hand_1) + len(hand_2)
    hand_1.append(deck[cards_dealt])

def busted(cards):
    if total(cards) > WINNING_SCORE:
        return "busted"
    else:
        return None
    
def evaluate_hands():
    if player_total > dealer_total:
        return "Player"
    if dealer_total > player_total:
        return "Dealer"
    if player_total == dealer_total:
        return "Tie"
    
def play_again():
    answer = input('Do you want to play again? y / n')
    return answer == 'y'

def pop_two_from_deck(deck):
    return [deck.pop(), deck.pop()]

deck = initialize_deck()

player_wins = 0
dealer_wins = 0
while True:
    #setup
    shuffle(deck)
    player_hand = pop_two_from_deck(deck)
    dealer_hand = pop_two_from_deck(deck)
    player_total = total(player_hand)
    dealer_total = total(dealer_hand)
    prompt(f'Dealer has {dealer_hand}, you have {player_hand}')
    while True:
    #player turn
        answer = input('hit or stay?')
        if answer == 'hit':
            player_hand.append(deck.pop())
            player_total = total(player_hand)
            prompt(f"Your hand is now {player_hand}")
            prompt(f"Your total is now {player_total}")
        elif answer == 'stay':
            prompt("You've chosen to stay.")
            break
        if busted(player_hand):
            dealer_wins += 1
            break
    if busted(player_hand):
        prompt(f'Your hand is {player_hand}, totalling to {player_total}. Busted! You lose')
        prompt(f"Dealer wins! Updated score is Player – {player_wins}, Dealer score is {dealer_wins}")
        if (player_wins >2 or dealer_wins > 2) or not play_again():
            break
        continue 
    
    while True:
        prompt(f'Dealer total is {dealer_total}')
        if busted(dealer_hand):
            break
        if total(dealer_hand) >= DEALER_THRESHOLD:
            break
        else:
            prompt('dealer hits!')
            dealer_hand.append(deck.pop())
            dealer_total = total(dealer_hand)
            prompt(f"Dealer's hand is {dealer_hand}")
    
    if busted(dealer_hand):
        prompt(f'Dealer busted with hand {dealer_hand} totalling to {dealer_total}')
        player_wins += 1
        if (player_wins >2 or dealer_wins > 2) or not play_again(): 
            prompt(f"Player wins! Updated score: Player – {player_wins}, Dealer – {dealer_wins}")
            break
        continue
    
    match evaluate_hands():
        case 'Player': 
            player_wins +=1
            prompt(f"Player wins! Updated score: Player – {player_wins}, Dealer – {dealer_wins}")
        case 'Dealer': 
            dealer_wins +=1
            prompt(f"Dealer wins! Updated score: Player – {player_wins}, Dealer – {dealer_wins}")
            
    if (player_wins >= GAMES_TO_WIN or dealer_wins >= GAMES_TO_WIN) or not play_again():
        break