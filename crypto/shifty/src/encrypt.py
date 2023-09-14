import random
import string

flag = "UNBCTF{CAESAR_GOT_SOME_MOVES}"

def caesar_shift(text, shift):
    text_shifted = ''
    for char in text:
        if char in string.ascii_uppercase:
            char_num = ord(char) - ord('A')
            char_num = (char_num + shift) % 26 + ord('A')
            text_shifted += chr(char_num)
        else:
            text_shifted += char
    return text_shifted

flag = caesar_shift(flag, random.randint(10, 16))

print(flag)