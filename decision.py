import random
import services
import decision_setup


def decision():
    choice_1 = [0, 0, 0, 0, 0]     # gold change, gold income change, happiness change, happiness income change, kingdom size change
    choice_2 = [0, 0, 0, 0, 0]
    choice_1_colour = []
    choice_2_colour = []

    all_templates = services.get_templates()
    loop = True
    while loop:         # pick a starting template
        template = random.choice(all_templates)
        start = template.find("[")
        if start != -1:
            loop = False
            continue
        else:
            pass

    template = template[:-1] + " "
    end_symbol = str(template[-2])
    template = template[1:-2]

    decision_setup.pick_nouns(template)

    loop = True
    while loop:  # pick a starting template
        template = random.choice(all_templates)
        start = template.find(end_symbol)
        if start == 0:
            loop = False
            continue
        else:
            pass

    template = template[:-1] + " "
    end_symbol = str(template[-2])
    template = template[1:-1]

    decision_setup.pick_nouns(template)

    for i in range(0, len(choice_1)):
        choice_1[i] += random.randint(-20, 20) / 20
    for i in range(0, len(choice_2)):
        choice_2[i] += random.randint(-2, 5) / 20
    for i in range(0, len(choice_1)):
        if choice_1[i] >= 0:
            choice_1_colour += [1]
        else:
            choice_1_colour += [0]
    for i in range(0, len(choice_2)):
        if choice_2[i] >= 0:
            choice_2_colour += [1]
        else:
            choice_2_colour += [0]

    return choice_1, choice_2, choice_1_colour, choice_2_colour
