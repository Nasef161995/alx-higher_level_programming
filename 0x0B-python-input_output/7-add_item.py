#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


arguments = sys.argv
my_obj = []
for i in range(1, len(arguments)):
    my_obj.append(arguments[i])

filename = "add_item.json"
save_to_json_file(my_obj, filename)
load_from_json_file(filename)
