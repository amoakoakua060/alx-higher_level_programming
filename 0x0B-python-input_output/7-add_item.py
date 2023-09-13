#!/usr/bin/python3

"""
module to load and dump from and to a file
"""


from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
n_list = argv[1:]
_list = []

try:
    with open(filename, 'r') as file:
        content = file.read()
    if len(content):
        _list = load_from_json_file(filename)
except FileNotFoundError:
    _list = []

for item in n_list:
    _list.append(item)

save_to_json_file(_list, filename)
