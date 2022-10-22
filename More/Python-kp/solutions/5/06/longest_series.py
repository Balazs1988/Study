import re


def longest_series(text):
    if text == '?':
        count = 1
    else:
        count = len(max(re.compile("(\?+\?)*").findall(text)))
    return count
