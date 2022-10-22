import os, datetime


def creates_directory():
    directory = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    os.mkdir(directory)
    pass


creates_directory()
