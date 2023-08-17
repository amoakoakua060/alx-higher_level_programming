#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        best_val = -1
        values = []
        for k, v in a_dictionary.items():
            values.append(v)
            if (best_val < v):
                best_val = v
        if values.count(best_val) == 1:
            for key, val in a_dictionary.items():
                if val == best_val:
                    return key
