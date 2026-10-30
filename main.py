#Blackjack with a flat 1 ace and player auto wins on 21
import random
choices = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
values = {
    'Ace':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'Jack':10,
    'Queen':10,
    'King':10,
}
print('Ace is always equal to 1 in this game')

def handCalc(hand):
    total = 0
    for entry in hand:
        total += values[entry]
    return(total)

def dealerTurn(playerCards, dCards, deck):
    while True:
        dealerCardsValue = handCalc(dCards)
        playerCardsValue = handCalc(playerCards)
        if dealerCardsValue > 21:
            print(f'You win! Dealer went over 21 with {dCards}')
            break
        elif dealerCardsValue < 17:
            print(f"Dealer has {dCards} and has to hit")
            dCards.append(deck.pop())
        elif dealerCardsValue == playerCardsValue:
            print('It is a tie! Nobody wins')
            break
        elif dealerCardsValue > playerCardsValue:
            print(f"You lost! Dealer has {dealerCardsValue} meanwhile you have {playerCardsValue}, they had {dCards}")
            break
        else:
            print(f"You win! Dealer has {dealerCardsValue} and you have {playerCardsValue}")
            break


playing = True
while playing:
    print()
    deck = choices*4
    random.shuffle(deck)
    cards = []
    dealerCards = []
    for _ in range(2):
        cards.append(deck.pop())
        dealerCards.append(deck.pop())
    while True:
        cardsValue = handCalc(cards)
        print(f"Your cards are {cards}, with a value of {cardsValue}, and dealer's up card is {dealerCards[0]}")
        choice = input('Will you stand or hit, or will you quit and run away? ').strip().lower()
        if choice == 'stand':
            print(f'You stand with a value of {cardsValue}')
            dealerTurn(cards,dealerCards, deck)
            break
        elif choice == 'hit':
            cards.append(deck.pop())
            cardsValue = handCalc(cards)
            if cardsValue > 21:
                print(f"You lost! You went over 21, dealer's cards were {dealerCards}, and you had {cards}")
                break
            if cardsValue == 21:
                print(f'You win! You have 21 in your hand, with the dealer having {dealerCards}')
                break
        elif choice == 'quit':
            print("It's okay to be scared...")
            playing = False
            break
        else:
            print('Not a valid choice')
            continue
