import random
import os


def name():
    loop = True
    while loop:
        temp_name = input("What do you want your kingdom to be called? ")
        confirm = input(f'Your kingdom shall be called {temp_name}. Is this correct? (Y/N)').upper()
        if confirm == "Y":
            return temp_name
        else:
            continue


def get_titles():
    with open('./titles.txt') as f:
        titles = f.readlines()
    return titles


def get_names():
    with open('./names.txt') as f:
        names = f.readlines()
    return names


def get_subjects():
    with open('noun.txt') as f:
        noun = f.readlines()
    return noun


def get_templates():
    with open('./decision_template.txt') as f:
        animal = f.readlines()
    return animal


def find_plural(random_suitable_noun):
    random_suitable_noun_list = random_suitable_noun.split(" ")
    if "plural" in random_suitable_noun_list:
        subject = str(random_suitable_noun_list[0])
        return subject
    elif "notplural" in random_suitable_noun_list:
        position = random_suitable_noun_list.index("notplural") + 1
        subject = str(random_suitable_noun_list[position])
        return subject
    else:
        subject = str(random_suitable_noun_list[0])
        subject = subject + "s"
        return subject


def deal_with_tags(template):

    try:
        os.remove("./temporary_noun.txt")  # remove the temporary file
    except FileNotFoundError:
        pass
    open('./temporary_noun.txt', "w")
    tags = ["edible", "farmed", "animal", "all", "relationship"]  # list of all tags

    noun_list = get_subjects()

    template_list = template.split()  # turn template into a list of each word

    end_of_template_first_noun = template_list.index("|")
    for i in range(0, end_of_template_first_noun):
        if template_list[i] in tags:
            with open('./temporary_noun.txt', "a") as temporary_noun_txt:
                temporary_noun_txt.write("\n")
                for j, line in enumerate(noun_list):
                    if line.find(" ", len(line) - 1) != -1:     # ensure no blank space at the end
                        line = line[:-2]
                    line = line[:-1]
                    line = " | " + line + " | "  # split each noun
                    line_list = line.split(" ")  # split noun with all tags into individual words - dog animal = dog, animal
                    if template_list[i] in line_list:  # if the tag in the template is in the noun, add it to
                        temporary_noun_txt.write(line)
                        temporary_noun_txt.write("\n")


    with open('./temporary_noun.txt') as f:
        suitable_nouns = f.readlines()

    suitable_nouns = str(suitable_nouns)

    suitable_nouns = suitable_nouns.replace("|", "").replace("[", "").replace("'", "").replace("  ", "").replace("\\n", "")
    suitable_nouns = suitable_nouns.split(",")
    suitable_nouns = suitable_nouns[1:len(suitable_nouns)]

    return suitable_nouns


def interpreted_choices(interpret_choices):
    choice_attributes = interpret_choices[0]
    gold_change = choice_attributes[0]
    gold_income_change = choice_attributes[1]
    happiness_change = choice_attributes[2]
    happiness_income_change = choice_attributes[3]
    kingdom_size_change = choice_attributes[4]
    colour = interpret_choices[1]
    text_op1 = "\nOption 1"
    text_op2 = "\nOption 2"
    text_1 = f' gold by'
    text_2 = f' gold income by'
    text_3 = f' happiness by'
    text_4 = f' happiness per turn by'
    text_5 = f' kingdom size by'
    last_zero = -1

    last_zero_start = True
    while last_zero_start:
        for i in range(0, len(choice_attributes)):
            if last_zero_start:
                if choice_attributes[i] == 0:
                    if i != 0:
                        last_zero = i - 1
                    else:
                        last_zero = 0
                    last_zero_check = True
                    while last_zero_check:
                        for j in range(i, len(choice_attributes)):
                            if last_zero_check:
                                if choice_attributes[j] != 0:
                                    last_zero = -1
                                    last_zero_check = False
                                    continue
                                if j == len(choice_attributes) - 1:
                                    last_zero_start = False
                                    last_zero_check = False
                elif i == len(choice_attributes) - 1:
                    last_zero = -1
                    last_zero_start = False

    if last_zero == -1 or last_zero == len(choice_attributes):
        last_zero = len(choice_attributes) - 1

    text = [text_1, text_2, text_3, text_4, text_5]
    if interpret_choices[2] == 1:
        print(text_op1, end=" ")
    if interpret_choices[2] == 2:
        print(text_op2, end=" ")
    if gold_change == 0 and gold_income_change == 0 and happiness_change == 0 and happiness_income_change == 0 and kingdom_size_change == 0:
        print("will have no effect")
    else:
        print("will change", end="")
        first = True
        printed = False
        for i in range(0, len(choice_attributes)):
            if choice_attributes[i] != 0:
                if i == last_zero:
                    if printed:
                        print(" and", end="")
                elif first:
                    first = False
                else:
                    print(",", end="")
                print(text[i], end="")
                if colour[i] == 0:
                    print(f' \033[31m{choice_attributes[i]}\033[m', end="")
                if colour[i] == 1:
                    print(f' \033[32m{choice_attributes[i]}\033[m', end="")
                printed = True
        print(".", end="")