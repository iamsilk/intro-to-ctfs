import string

flag = "IBPQHT{QOSGOF_UCH_GCAS_ACJSG}"

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

for i in range(0, 26):
    print(i, caesar_shift(flag, i))