#!/usr/bin/python3
def multiple_returns(sentence):
    """
    If the sentence is empty, the first character should be equal to None
    """
    s_len = 0
    first_char = None
    if isinstance(sentence, str):
        s_len = len(sentence)
        if s_len > 0:
            first_char = sentence[0]
        return (s_len, first_char)
