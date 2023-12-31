"""
Group: Nicholas Pacejka, Patrick Dimichele, Noah Garner, Nathanon 'Nat' Laobappha
Instructor: Mr. Man-Chi Leung
Course: CSC-249-0001
Purpose: Simulating a gambling game experience using data structures and other design features
"""
from diegame import *
# import subprocess

# currency related variables:
wallet = int(500)
account = int(0)
emer_fund = int(100)


def main():
    global wallet
    global emer_fund
    if wallet <= 0:
        print(f'Emergency funds allocated: {emer_fund}$')
        wallet += emer_fund
        print(f'Wallet: {wallet}$')
    print('---Welcome to the Casino---')
    print(f'Your current wallet balance is: {wallet}$')
    print(
        'Please Select from the following areas:' + '\n' +
        '1. Dice Game' + '\n' +
        '2. Even or Odd' + '\n' +
        '3. Not yet implemented')
    response = input('Choose where to go (1-3): ')
    if response == '1':
        print(
            '---Welcome to the Dice Game Room!---' + '\n' +
            'Guess the total number that will appear on three cast dice.' + '\n' +
            'Correct predictions will double your bet.' + '\n' +
            'Three matching dice will triple it.')
        response2 = input('Buy-in is 25$. Would you like to play? (y/n) ').lower()
        if response2 == 'y' and wallet > 25:
            guess = input('Select a guessing range:' + '\n' +
                          'Option 1: Between 3 and 10' + '\n' +
                          'Option 2: Between 11 and 18' + '\n')
            if guess == '1' or guess == '2':
                d1 = Die()
                d2 = Die()
                d3 = Die()
                pass
                d1.roll()
                d2.roll()
                d3.roll()
                the_sum = int(d1.value) + int(d2.value) + int(d3.value)
                profit = int(50)
                loss = int(25)
                if the_sum % 3 == 0:
                    profit = int(75)
                print(f'The sum of the dice is {the_sum}.')
                if guess == '2' and the_sum >= 11:
                    print('Correct Prediction')
                    wallet += profit
                    print(f'Wallet: {wallet}$')
                    main()
                elif guess == '1' and the_sum <= 10:
                    print('Correct Prediction')
                    wallet += profit
                    print(f'Wallet: {wallet}$')
                    main()
                elif guess == '2' and the_sum < 11:
                    print('Incorrect Prediction')
                    wallet -= loss
                    print(f'Wallet: {wallet}$')
                    main()
                elif guess == '1' and the_sum > 10:
                    print('Incorrect Prediction')
                    wallet -= loss
                    print(f'Wallet: {wallet}$')
                    main()
            else:
                print('Invalid Entry Detected')
                main()

        elif response2.upper == 'n':
            main()
        else:
            main()
    elif response == '2':
        # If another game is created subprocess will serve to access it
        # subprocess.run(["python", "casino_game.py"])
        print(
            '---Welcome to the Even or Odd Room!---' + '\n' +
            'Guess if the total number that will appear on three cast dice will be Even or Odd.' + '\n' +
            'Correct predictions will double your bet.' + '\n' +
            'Three matching dice will triple it.')
        response2 = input('Buy-in is 25$. Would you like to play? (y/n) ').lower()
        if response2 == 'y':
            guess = input('Select your guessing choice:' + '\n' +
                          'Choice 1: Even' + '\n' +
                          'Choice 2: Odd' + '\n')
            if guess == '1' or guess == '2':
                d1 = Die()
                d2 = Die()
                d3 = Die()
                pass
                d1.roll()
                d2.roll()
                d3.roll()
                the_sum = int(d1.value) + int(d2.value) + int(d3.value)
                profit = int(50)
                loss = int(25)
                if the_sum % 3 == 0:
                    profit = int(75)
                print(f'The sum of the dice is {the_sum}.')
                if guess == '1' and the_sum % 2 == 0:
                    print('Correct Prediction')
                    wallet += profit
                    print(f'Wallet: {wallet}$')
                    main()
                elif guess == '2' and the_sum % 2 == 1:
                    print('Correct Prediction')
                    wallet += profit
                    print(f'Wallet: {wallet}$')
                    main()
                elif guess == '2' and the_sum % 2 == 0:
                    print('Incorrect Prediction')
                    wallet -= loss
                    print(f'Wallet: {wallet}$')
                    main()
                elif guess == '1' and the_sum % 2 == 1:
                    print('Incorrect Prediction')
                    wallet -= loss
                    print(f'Wallet: {wallet}$')
                    main()
            else:
                print('Invalid Entry Detected')
                main()

        elif response2.upper == 'n':
            main()
        else:
            main()
    elif response == '3':
        # If another game is created subprocess will serve to access it
        # subprocess.run(["python", "casino_game2.py"])
        main()
    else:
        print('Invalid Entry Detected')
        main()


if __name__ == '__main__':
    main()
