# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
import re


def is_pangram(s):
    print(s.lower())
    print(True if len(re.findall(r'[a-z]', s.lower())) >= 26 and len(s) > len(set(s)) else False)


is_pangram("The quick, brown fox jumps over the lazy dog!")
is_pangram("1bcdefghijklmnopqrstuvwxyz")
is_pangram("Aacdefghijklmnopqrstuvwxyz")
