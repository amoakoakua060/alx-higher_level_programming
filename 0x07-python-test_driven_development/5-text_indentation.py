#!/usr/bin/python3

"""
Module containing an text_indentation function
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    l_text = len(text)
    while c < l_text and text[c] == ' ':
        c += 1

    while c < l_text:
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < l_text and text[c] == ' ':
                c += 1
            continue
        c += 1
