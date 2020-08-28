#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'Andrew Canter'

from morse_dict import MORSE_2_ASCII
import re
import itertools


def decode_bits(bits):
    bits = bits.strip('0')
    letters = re.split(('0+'), bits)
    spaces = re.split(('1+'), bits)
    spaces.remove('')
    spaces.remove('')
    multiplyer = len(letters[0])

    # Looks through the string in order to find the time unit multiplyer
    for i in letters:
        if len(i) < multiplyer:
            multiplyer = len(i)
    for i in spaces:
        if len(i) < multiplyer:
            multiplyer = len(i)

    # Iterates through the binary string adding morse to the message
    message = ''

    for i, j in itertools.zip_longest(letters, spaces):
        if len(i)/multiplyer == 1:
            message += '.'
        elif len(i)/multiplyer == 3:
            message += '-'

        if j is None:
            pass
        elif len(j)/multiplyer == 3:
            message += ' '
        elif len(j)/multiplyer == 7:
            message += '   '

    return message


def decode_morse(morse):
    message = ''
    morse = morse.strip().replace('  ', ' space ').split()

    for letter in morse:
        if letter == 'space':
            message += ' '
        else:
            message += MORSE_2_ASCII[letter]

    return message


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011" # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
