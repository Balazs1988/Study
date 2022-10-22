import stores_log_items
import json

with open('log_items.json', 'r') as json_file:
    dict_list = json.load(json_file)

level = input("Please type the level (INFO or ERROR): ")
description = input("Please type the description: ")

new_item = stores_log_items.new_log_item(dict_list, level, description)
dict_list.append(new_item)
with open('log_items.json', 'w') as json_file:
    json.dump(dict_list, json_file)
