import random
import sys

game_deck = ([2, 3, 4, 5, 6, 7, 8, 9, 10, 
             'Jack', 'Queen', 'King', 'Ace']*4)

class Player:
    def __init__(self, name, p_cards, p_score):
        self.name = name
        self.p_cards = p_cards
        self.p_score = p_score

    def draw_hand(self, p_cards=None):
        global game_deck
        if p_cards is None:
            p_cards = []

        random.shuffle(game_deck)
        p_cards.append(game_deck[0])
        p_cards.append(game_deck[1])
        for c in p_cards:
            game_deck.remove(c)

        self.p_cards = p_cards

    def calculate_score(self, p_cards, p_score) -> int:
        if isinstance(p_score, tuple):
            p_score = int(p_score)
        else:
            p_score = 0

        for c in p_cards:
            if isinstance(c, (int)):
                p_score += c
            else:
                if c == 'Jack' or c == 'Queen' or c == 'King':
                    p_score += 10
                else:
                    print(f"Your score is currently: {p_score} and your cards are: {p_cards}")
                    print("Would you like your Ace to be scored as a 1 or an 11?")
                    choice = input()
                    if choice == '1' or '11:':
                        choice = int(choice)
                        p_score += choice
                        for p in range(len(p_cards)):
                            if p_cards[p] == 'Ace':
                                p_cards[p] = choice
                    else:
                        print("Selection invalid, choosing 1 by default")
                        p_score =+ 1
        if p_score == 21:
            print("21! You win!")
            print("Play again?")
        
        self.p_score = p_score
    
    def hit(p_cards):
        global game_deck
        player1.p_cards.append(game_deck[0])
        game_deck.remove(player1.p_cards[len(player1.p_cards)-1])


# player1 = Player("Rick", None, 0)
dealer = Player("Dealer", None, 0)
# player1.draw_hand()
# print(player1.p_cards)
# player1.calculate_score(player1.p_cards, player1.p_score)
# print(player1.p_score)
# player1.hit()
# print(player1.p_cards)
# player1.calculate_score(player1.p_cards, player1.p_score)
# print(player1.p_score)

# def game_init() -> Player:
#     print("Hello and welcome to the casino! What is your name?")
#     player_name = input()
#     player1 = Player(f"{player_name}", None, 0)

# game_init()


def game_init() -> Player:
    print("Hello and welcome to the casino! What is your name?")
    player_name = input()
    player1 = Player(f"{player_name}", None, 0)
    return player1
player1 = game_init()

def game_actions(p_cards, p_score):
    if player1.p_cards == None:
        print("Here are your cards...")
        player1.draw_hand()
        print(player1.p_cards)
        player1.calculate_score(player1.p_cards, player1.p_score)
        print(f"This is your current score {player1.p_score}")
    else:
        print('Restarting your game...')
    while player1.p_score < 21:
        try:
            print("Select action: Hit | Stand | View Cards | Quit")
            action = input()
            if action == 'Hit' or action == 'hit':
                player1.hit()
                print(f"You drew a: {player1.p_cards[(len(player1.p_cards)-1)]}")
                player1.calculate_score(player1.p_cards, player1.p_score)
                print(player1.p_score)
                if player1.p_score == 21:
                    print("21! You win!")
                    print("Play again?")
                    play_again = input()
                    if play_again == 'Y' or play_again == 'y':
                        return game_actions(p_cards, p_score)
                    elif play_again == 'N' or play_again == 'n':
                        sys.exit()
                elif player1.p_score > 21:
                    print("Bust! You lose!")
                    print("Play again? Y/N")
                    play_again = input()
                    if play_again == 'Y' or play_again == 'y':
                        return game_actions(p_cards, p_score)
                    elif play_again == 'N' or play_again == 'n':
                        sys.exit()
            elif action == 'Stand' or action == 'stand':
                print("Awaiting dealer turn...")
                break
            elif action == 'View Cards' or action == 'view cards':
                print(player1.p_cards)
            elif action == 'Quit' or action == 'quit':
                sys.exit()
            else:
                print("I'm sorry. That command is not recognized, please select another option...")
                return game_actions(p_cards = None, p_score = 0)
        except:
            print("Something went wrong")
            sys.exit()

game_actions(p_cards = player1.p_cards, p_score = player1.p_score)


dealer.draw_hand()
dealer.calculate_score(dealer.p_cards, dealer.p_score)
print(dealer.p_score)
try:
    if dealer.p_score < player1.p_score:
        dealer.hit()
        dealer.calculate_score(dealer.p_cards, dealer.p_score)
        print(dealer.p_score)
        print(dealer.p_cards)
    elif dealer.p_score > player1.p_score:
        print(dealer.p_score)
        print('Dealer wins!')
except:
    print('An error occurred')
    sys.exit()

        
        
            

