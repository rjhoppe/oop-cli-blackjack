import random
import sys

game_deck = ([2, 3, 4, 5, 6, 7, 8, 9, 10, 
             'Jack', 'Queen', 'King', 'Ace']*4)

round_count = 0
# Add dict/list for player wins / losses

class Player:
    def __init__(self, name, p_cards, p_score, win_loss):
        self.name = name
        self.p_cards = p_cards
        self.p_score = p_score
        self.win_loss = win_loss

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
                    print(f"{self.name}'s score is currently: {p_score} and your cards are: {p_cards}")
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
        
        self.p_score = p_score
        print(f"This is {self.name}'s current score: {p_score}")
    
    def player_hit(p_cards):
        global game_deck
        player1.p_cards.append(game_deck[0])
        game_deck.remove(player1.p_cards[len(player1.p_cards)-1])

    def dealer_hit(p_cards):
        global game_deck
        dealer.p_cards.append(game_deck[0])
        game_deck.remove(dealer.p_cards[len(dealer.p_cards)-1])

    def player_reset(p_cards, p_score):
        global game_deck
        game_deck.clear()
        game_deck = ([2, 3, 4, 5, 6, 7, 8, 9, 10, 
             'Jack', 'Queen', 'King', 'Ace']*4)
        global round_count
        round_count += 1
        player1.p_cards.clear()
        player1.p_score = 0
        # p_cards == None
        # p_score == 0
        # new_score = 0
        # p_score = new_score
        
    # def player_score_reset(p_score):    
    #     player1.p_score = 0

    def dealer_reset(p_cards, p_score):
        dealer.p_cards.clear()
        dealer.p_score == 0

    # Works
    #
    # def player_reset(p_cards, p_score):
    #     global game_deck
    #     game_deck.clear()
    #     game_deck = ([2, 3, 4, 5, 6, 7, 8, 9, 10, 
    #          'Jack', 'Queen', 'King', 'Ace']*4)
    #     player1.p_cards.clear()
    #     player1.p_cards == None
    #     player1.p_score == 0


    # player1.player_reset(player1.p_cards)
    # print(player1.p_cards)



# player1 = Player("Rick", None, 0)
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
    player1 = Player(f"{player_name}", None, 0, win_loss={'Wins': 0, 'Losses': 0})
    print(player1.p_cards)
    return player1
player1 = game_init()

def game_actions(p_cards, p_score):
    if player1.p_cards == None or player1.p_cards == []:
        print("Here are your cards...")
        player1.draw_hand()
        print(player1.p_cards)
        player1.calculate_score(player1.p_cards, player1.p_score)
        # print(f"This is {player1.name}'s current score {player1.p_score}")
    while player1.p_score < 21:
        try:
            print("Select action: Hit | Stand | View Cards | Quit | Test")
            action = input()
            if action == 'Hit' or action == 'hit':
                player1.player_hit()
                print(f"You drew a: {player1.p_cards[(len(player1.p_cards)-1)]}")
                player1.calculate_score(player1.p_cards, player1.p_score)
                # print(player1.p_score)
                if player1.p_score == 21:
                    print("21! You win!")
                    player1.win_loss['Wins'] +=1
                    print("Play again? Y/N")
                    play_again = input()
                    if play_again == 'Y' or play_again == 'y':
                        player1.player_reset(p_score)
                        return game_actions(p_cards, p_score)
                    elif play_again == 'N' or play_again == 'n':
                        sys.exit()
                elif player1.p_score > 21:
                    print("Bust! You lose!")
                    player1.win_loss['Losses'] +=1
                    print("Play again? Y/N")
                    play_again = input()
                    if play_again == 'Y' or play_again == 'y':
                        player1.player_reset(p_score)
                        return game_actions(p_cards, p_score)
                    elif play_again == 'N' or play_again == 'n':
                        print(player1.win_loss)
                        sys.exit()
            elif action == 'Stand' or action == 'stand':
                print("Awaiting dealer turn...")
                if round_count > 1:
                    return dealer_loop(p_cards = dealer.p_cards, p_score = dealer.p_score)
                else:
                    break
            elif action == 'View Cards' or action == 'view cards':
                print(player1.p_cards)
            elif action == 'Quit' or action == 'quit':
                sys.exit()
            elif action == 'Test' or action == 'test':
                # Below works
                player1.player_reset(p_score)
                # dealer.player_reset(p_score)
                print(player1.p_cards)
                # print(dealer.p_score)
                return game_actions(p_cards, p_score)
                # print(len(game_deck))
                # print(player1.p_score)
                # player1.player_score_reset()
                # print(player1.p_score)
            else:
                print("I'm sorry. That command is not recognized, please select another option...")
                return game_actions(p_cards = None, p_score = 0)
        except:
            print("Something went wrong")
            sys.exit()

game_actions(p_cards = player1.p_cards, p_score = player1.p_score)

# Creates dealer instance before dealer turn
dealer = Player("Dealer", None, 0, None)

def dealer_loop(p_cards, p_score):
    dealer.draw_hand()
    print(dealer.p_cards)
    dealer.calculate_score(dealer.p_cards, dealer.p_score)
    # print(f"Dealer score: {dealer.p_score}")
    try: 
        while dealer.p_score <= player1.p_score:
            dealer.dealer_hit()
            print(dealer.p_cards)
            dealer.calculate_score(dealer.p_cards, dealer.p_score)
            # print(f"Dealer score: {dealer.p_score}")
        if dealer.p_score > 21:
            print('Dealer busts! You win!')
            player1.win_loss['Wins'] +=1
            print("Play again? Y/N")
            play_again = input()
            if play_again == 'Y' or play_again == 'y':
                # player1.player_reset(p_cards)
                # dealer.player_reset(p_cards, p_score)
                player1.player_reset(p_score)
                dealer.player_reset(p_score)
                return game_actions(p_cards, p_score)
            elif play_again == 'N' or play_again == 'n':
                sys.exit()
            # return game_actions(p_cards, p_score)
        elif 21 >= dealer.p_score > player1.p_score:
            print('Dealer wins!')
            player1.win_loss['Losses'] +=1
            print("Play again? Y/N")
            play_again = input()
            if play_again == 'Y' or play_again == 'y':
                player1.player_reset(p_score)
                dealer.player_reset(p_score)
                return game_actions(p_cards, p_score)
            elif play_again == 'N' or play_again == 'n':
                sys.exit()
            return game_actions(p_cards, p_score)
    except:
        print('An error occurred')
        print(player1.win_loss)
        sys.exit()

dealer_loop(p_cards = dealer.p_cards, p_score = dealer.p_score)

# try:
#     while dealer.p_score < player1.p_score:
#         dealer.hit()
#         dealer.calculate_score(dealer.p_cards, dealer.p_score)
#         # print(dealer.p_score)
#         # print(dealer.p_cards)
#     # elif dealer.p_score > player1.p_score:
#     #     print(dealer.p_score)
#     #     print('Dealer wins!')
# except:
#     print('An error occurred')
#     sys.exit()


