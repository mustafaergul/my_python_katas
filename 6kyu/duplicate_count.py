# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
def duplicate_count(text):
    print(len([a for a in set(text.lower()) if text.lower().count(a) > 1]))


duplicate_count("abbcde")
duplicate_count("abcde")
duplicate_count("abcdeaa")
duplicate_count("abcdeaB")
