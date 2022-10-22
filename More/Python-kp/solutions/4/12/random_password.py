import random, string


def creates_password():
    lower_chars = list(string.ascii_lowercase)
    upper_chars = list(string.ascii_uppercase)
    digits = list(string.digits)
    special_chars = ('<', '>', '#', '&', '@', '+', '%', '(', ')')
    pre_passwd = []
    for i in range(4):
        pre_passwd.append(random.choice(lower_chars))
        pre_passwd.append(random.choice(upper_chars))
        pre_passwd.append(random.choice(digits))
        pre_passwd.append(random.choice(special_chars))
    random.shuffle(pre_passwd)
    passwd_final = ''.join(pre_passwd)
    return passwd_final
