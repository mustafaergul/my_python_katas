import re


def to_camel_case(text):
    words = re.split(r'[-_]', text)
    return words[0] + ''.join([a.capitalize() for a in words[1:]])


to_camel_case("the_stealth-warrior")
to_camel_case("A-B-C")
to_camel_case("")
to_camel_case("The-Stealth-Warrior")
