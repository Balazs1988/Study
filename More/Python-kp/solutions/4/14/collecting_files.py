import os


def collecting_files(path_to_dir):
    py_list = []
    for file_name in os.listdir(path=path_to_dir):
        if file_name.endswith('.py'):
            name = file_name.split('.')[0]
            py_list.append(name)
    return py_list
