import random
import services


def pick_nouns(template):
    loop = True
    while loop:
        template_as_list = template.split()
        template = ' '.join(template_as_list)
        try:
            location_of_fist_noun = template_as_list.index("noun")
        except ValueError:
            loop = False
            continue
        if "noun" not in template_as_list:
            loop = False
            continue
        if location_of_fist_noun != -1:
            suitable_nouns = services.deal_with_tags(template)  # when adding a new tag go to deal_with_tags
            pluralcheck = True
            while pluralcheck:
                random_suitable_noun = random.choice(suitable_nouns)
                if "plural" in template_as_list:
                    if "implural" in random_suitable_noun:
                        continue
                pluralcheck = False

            random_suitable_noun = random_suitable_noun[1:]
            suitable_noun_as_list = random_suitable_noun.split(" ")
            location_of_tags = suitable_noun_as_list.index("tags")
            end_of_template_call = template_as_list.index("|")

            try:
                if template_as_list.index("plural") < end_of_template_call:

                    if "notplural" in suitable_noun_as_list:
                        pluralable = True
                    elif "plural" in suitable_noun_as_list:
                        pluralable = True
                    else:
                        pluralable = False
                    if pluralable:
                        for i in range(location_of_tags, len(suitable_noun_as_list)):
                            if suitable_noun_as_list[i] == "notplural":
                                location_of_hash = suitable_noun_as_list.index("#")
                                for j in range(0, len(suitable_noun_as_list)):
                                    if not i < j < location_of_hash:
                                        suitable_noun_as_list[j] = ""
                            elif suitable_noun_as_list[i] == "plural":
                                for j in range(location_of_tags, len(suitable_noun_as_list)):
                                    suitable_noun_as_list[j] = ""
                            else:
                                pass
                    else:
                        for i in range(location_of_tags, len(suitable_noun_as_list)):
                            suitable_noun_as_list[i] = ""
                        suitable_noun_as_list += "s "
                        random_suitable_noun = ''.join(suitable_noun_as_list)
                        suitable_noun_as_list = random_suitable_noun.split()

                else:
                    for i in range(location_of_tags, len(suitable_noun_as_list)):
                        suitable_noun_as_list[i] = ""

            except ValueError:
                suitable_noun_as_list = suitable_noun_as_list[0:location_of_tags]

            random_suitable_noun = ' '.join(suitable_noun_as_list)
            end_of_template_call = template_as_list.index("|") + 1
            for i in range(location_of_fist_noun, end_of_template_call):
                template_as_list[i] = ""
            template_as_list[location_of_fist_noun] = random_suitable_noun
            template = ' '.join(template_as_list)
        continue

    print(template, end=" ")
