import os


def count_modules(path: str, extension='py') -> int:
    """
    Count the modules at the given path.
    :param path: path of the directory
    :return: count of the .py files
    """
    count = 0
    for file_name in os.listdir(path):
        if file_name.endswith('.' + extension):
            count += 1
    return count


if __name__ == '__main__':
    n = count_modules('.')
    print(f'Number of Python modules: {n}')
    n = count_modules('.', 'exe')
    print(f'Number of exe files: {n}')
