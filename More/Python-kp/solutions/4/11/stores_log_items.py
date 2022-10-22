import datetime


def new_log_item(dict_list, level, description):
    act_id = len(dict_list) + 1
    timestamp = str(datetime.datetime.now()).split('.')[0]
    new_dict = {
        'Id': act_id,
        'Timestamp': timestamp,
        'Level': level,
        'Description': description
    }
    return new_dict
