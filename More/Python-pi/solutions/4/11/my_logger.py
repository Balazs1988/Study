import datetime
import json

log_items = [
    {
        'id': 1,
        'timestamp': '2022-08-03 09:00:00',
        'level': 'INFO',
        'description': 'Start!'
    },
    {
        'id': 2,
        'timestamp': '2022-08-05 13:00:00',
        'level': 'ERROR',
        'description': 'Error occurred!'
    }
]


def append_log_item(log: list, level: str, description: str) -> None:
    """
    Append a new log item to the logs.
    :param log: list of log items
    :param level: 'INFO' or 'ERROR'
    :param description: textual description of the log item
    :return: None
    """
    item = {
        'id': calc_last_id(log) + 1,
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'level': level,
        'description': description
    }
    log.append(item)


def calc_last_id(log: list) -> int:
    """
    Calculate the last id.
    :param log: list of log items
    :return: id as an integer value
    """
    # NOTE: We can also assume that the log is ordered by id!
    if not log:
        return 0
    max_id = 0
    for item in log:
        if item['id'] > max_id:
            max_id = item['id']
    return max_id


def save_log(log: list, path: str) -> None:
    """
    Save the log into a JSON file.
    :param log: list of log items
    :param path: path of the JSON file
    :return: None
    """
    with open(path, 'w') as json_file:
        json.dump(log, json_file)


def load_log(path: str) -> list:
    """
    Load the log from a JSON file.
    :param path: path of the JSON file
    :return: list of log items
    """
    with open(path, 'r') as json_file:
        log = json.load(json_file)
        return log


if __name__ == '__main__':
    append_log_item(log_items, 'INFO', 'New item has been added!')
    save_log(log_items, 'my_log.json')
    retrieved = load_log('my_log.json')
    print(retrieved)
