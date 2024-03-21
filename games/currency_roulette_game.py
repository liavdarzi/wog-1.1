import random
from score import add_score,current_scores
from currency_converter import CurrencyConverter


#Retrieves the current USD to ILS exchange rate and calculates an interval for the correct answer based on the game's difficulty level.
def get_money_interval(amount_of_money ,difficulty):
    c = CurrencyConverter()
    exchange_rate = c.convert(1,'USD', 'ILS')
    money_exchange = amount_of_money*exchange_rate
    interval = 10- difficulty
    #the interval of the guess
    interval_list = [float(money_exchange-interval),float(money_exchange+interval)]
    return interval_list

#Prompts the user to input a guess for the converted value of a specified amount in USD.
def get_guess_from_user(ammont_of_money):
    print(f'Guess how many is {ammont_of_money} USD in ILS :', end=" ")
    guess = float(input())
    return guess

#Executes the game by employing the functions above, and returns True if the user wins, and False if the user loses.
def compare_results(guess, inteval_list):
    if inteval_list[0]<= guess and guess <= inteval_list[1]:
        return True
    else:
        return False

#Executes the game by invoking the functions above and returns True if the user wins,a nd False if the user loses.
def play(difficulty):
    print()
    print(f'WELCOME to roulette game! You are playing in difficulty {difficulty}!')
    amount_of_money = random.randint(1,100)
    interval_list = get_money_interval(amount_of_money,difficulty)
    guess = get_guess_from_user(amount_of_money)
    result = compare_results(guess, interval_list)
    if result == True:
        print(f'You are the winner! the real value is {interval_list[1]- 10+ difficulty} !')
        add_score(difficulty)
    else:
        print(f'You lose, maybe next time. The real value is {interval_list[1]-10+ difficulty} !')
    return result

