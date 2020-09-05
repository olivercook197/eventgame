import services
import event

name = services.name()

print(f'\nWelcome to the kingdom of {name}.')

kingdom_gold = 2
gold_income = 1
kingdom_happiness = 49
happiness_income = 1
kingdom_size = 1


def integer():
    global kingdom_gold
    global gold_income
    global kingdom_happiness
    global happiness_income
    global kingdom_size
    kingdom_gold = int(kingdom_gold * 20) / 20
    gold_income = int(gold_income * 20) / 20
    kingdom_happiness = int(kingdom_happiness * 20) / 20
    happiness_income = int(happiness_income * 20) / 20
    kingdom_size = int(kingdom_size * 20) / 20


loop = True
while loop:
    integer()
    kingdom_gold += gold_income
    kingdom_happiness += happiness_income
    integer()
    print(f'Your current gold is {kingdom_gold}')
    print(f'Your current happiness is {kingdom_happiness}\n')
    loop1 = True
    while loop1:
        next_option = input("What would you like to do next? Next event (1). View current stats (2). ")
        loop2 = True
        while loop2:
            if next_option == "1":
                loop1 = False
                loop2 = False
            elif next_option == "2":
                integer()
                print(f'You currently have {kingdom_gold} gold, with an income of {gold_income}.\n'
                      f'You currently have a happiness of {kingdom_happiness}, which changes by {happiness_income} each turn.\n'
                      f'Your kingdom is currently {kingdom_size} miles².')
                loop2 = False
            else:
                print("Invalid option, please try again.")
                loop2 = False
    event_outcome = event.new_event()
    kingdom_gold += event_outcome[0]
    gold_income += event_outcome[1]
    kingdom_happiness += event_outcome[2]
    happiness_income += event_outcome[3]
    kingdom_size += event_outcome[4]
    if kingdom_size <= 0:
        print("Your kingdom has been destroyed, game over.")
        loop = False
