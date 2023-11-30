import random


def calculator_cards_total(numbersTotal, cards):
    if cards[1:] == "Jack":
        numbersTotal += 10

    elif cards[1:] == "Queen":
        numbersTotal += 10

    elif cards[1:] == "King":
        numbersTotal += 10

    elif cards[1:] == "Ace":
        if numbersTotal >= 11:
            numbersTotal += 1

        else:
            numbersTotal += 11

    else:
        numbersTotal += int(cards[1:])

    return numbersTotal


def main():
    deckOfCards = ["C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJack", "CQueen", "CKing", "CAce",
                   "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJack", "DQueen", "DKing", "DAce",
                   "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJack", "HQueen", "HKing", "HAce",
                   "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJack", "SQueen", "SKing", "SAce",
                   ]
    dealersNumberTotal = 0
    playersNumberTotal = 0
    dealerCards = list()
    playerCards = list()
    random.shuffle(deckOfCards)

    dealerCards1 = deckOfCards.pop()
    dealersNumberTotal = calculator_cards_total(dealersNumberTotal, dealerCards1)
    dealerCards2 = deckOfCards.pop()
    dealersNumberTotal = calculator_cards_total(dealersNumberTotal, dealerCards2)

    dealerCards.append(dealerCards1)
    dealerCards.append(dealerCards2)

    playersCards1 = deckOfCards.pop()
    playersNumberTotal = calculator_cards_total(playersNumberTotal, playersCards1)
    playersCards2 = deckOfCards.pop()
    playersNumberTotal = calculator_cards_total(playersNumberTotal, playersCards2)

    playerCards.append(playersCards1)
    playerCards.append(playersCards2)

    print("Dealers Cards: ", '  '.join(dealerCards), " Total number value is ", dealersNumberTotal)

    print("Players Cards: ", '  '.join(playerCards), " Total number Value is ", playersNumberTotal)

    if dealersNumberTotal == 21 and playersNumberTotal == 21:
        print("Tie Game by both player and dealer having blackjack.")
        return "Tie"

    if dealersNumberTotal == 21:
        print("Dealer Win by BlackJack")
        return "Lost"

    elif playersNumberTotal == 21:
        print("Player Win by BlackJacks")
        return "Win"

    print()
    hitOrStand = input("Do you want to hit or stand: ")
    hitOrStand = hitOrStand.lower().strip()
    print()

    while hitOrStand != "stand":

        if hitOrStand == "hit":
            playerNewCards = deckOfCards.pop()
            playersNumberTotal = calculator_cards_total(playersNumberTotal, playerNewCards)
            playerCards.append(playerNewCards)

            print("Players Cards: ", '  '.join(playerCards), " Total number value is ", playersNumberTotal, end="\n")

            if playersNumberTotal > 21:
                print("Player lost by going pass 21.")
                return "Lost"

        else:
            print("You have not put in the correct words. Please try again.")

        hitOrStand = input("Do you want to hit or stand: ")
        hitOrStand = hitOrStand.lower().strip()
        print()

    while dealersNumberTotal <= 16:

        print("Dealer Hit. ", end="\n")
        dealerNewCards = deckOfCards.pop()
        dealersNumberTotal = calculator_cards_total(dealersNumberTotal, dealerNewCards)
        dealerCards.append(dealerNewCards)

        print("Dealers Cards: ", '  '.join(dealerCards), " Total number value is ", dealersNumberTotal, end="\n")

        if dealersNumberTotal > 21:
            print("Dealer lost by going pass 21.")
            return "Win"

    print("Dealer Stand")
    if dealersNumberTotal > playersNumberTotal:
        print("Dealer win.")
        return "Lost"

    elif playersNumberTotal > dealersNumberTotal:
        print("Player win.")
        return "Win"

    else:
        print("Tie game.")
        return "Tie"


if __name__ == "__main__":
    main()
