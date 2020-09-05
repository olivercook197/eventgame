import random
import decision
import services


def new_event():
    all_titles = services.get_titles()
    all_names = services.get_names()
    title = random.choice(all_titles)
    title = title[:-1] + " "
    first_name = random.choice(all_names)
    first_name = first_name[:-1] + " "
    last_name = random.choice(all_names)
    last_name = last_name[:-1]
    if (last_name[-1]) == "l" and (last_name[-2]) == "l":
        last_name = last_name[:-1]
    last_name = ''.join((last_name, "son"))
    print(f'\n{title}{first_name}{last_name} requests your attention.')

    choices = decision.decision()
    list_of_choices = list(choices)

    interpret_choices = list_of_choices[0], list_of_choices[2], 1

    services.interpreted_choices(interpret_choices)

    interpret_choices = list_of_choices[1], list_of_choices[3], 2

    services.interpreted_choices(interpret_choices)

    choice_1 = choices[0]
    choice_2 = choices[1]

    loop = True
    while loop:
        selection = input("\n1/2? ")
        if selection == "1" or selection == "2":
            if selection == "1":
                user_choice = choice_1
                print("")
            if selection == "2":
                user_choice = choice_2
                print("")
            loop = False
        else:
            print("Only the numbers 1 and 2 are valid, try again.")

    return user_choice

