#!/usr/bin/python
# -*- coding: utf-8 -*-


def enc(string):
    encodedMessage = []
    for letter in string:
        if ord(letter) not in range(65, 91) and ord(letter) \
            not in range(97, 123) and ord(letter) != 32:
            return 'Unknown Character ' + letter
        elif ord(letter) == 32:
            encodedMessage.append(' ')
        else:
            if ord(letter) + 3 not in range(65, 91) and ord(letter) + 3 \
                not in range(97, 123):

                encodedMessage.append(chr(ord(letter) - 23))  # Exceeded Z or z
            else:
                encodedMessage.append(chr(ord(letter) + 3))  # In range
    else:
        return ''.join(encodedMessage)


def dec(string):
    decodedMessage = []
    for letter in string:
        if ord(letter) not in range(65, 91) and ord(letter) \
            not in range(97, 123) and ord(letter) != 32:
            return 'Unknown Character ' + letter
        elif ord(letter) == 32:
            decodedMessage.append(' ')
        else:
            if ord(letter) - 3 not in range(65, 91) and ord(letter) - 3 \
                not in range(97, 123):

                decodedMessage.append(chr(ord(letter) + 23))  # Exceeded Z or z
            else:
                decodedMessage.append(chr(ord(letter) - 3))  # In range
    else:
        return ''.join(decodedMessage)


# Call with dec("data to be decoded") or enc("data to be encoded")
