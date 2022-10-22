import datetime
import os


if __name__ == '__main__':
    dir_name = datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')
    os.mkdir(dir_name)
