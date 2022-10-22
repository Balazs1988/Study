import random_password


def checks_password(passwd):
    special_chars = ('<', '>', '#', '&', '@', '+', '%', '(', ')')
    if sum(1 for i in passwd if i.islower()) > 3 and sum(1 for j in passwd if j.isupper()) > 3 and \
    sum(1 for k in passwd if k.isdigit()) > 3 and sum(1 for i in passwd if i in special_chars) > 3:
        print('Strong password!')
    else:
        print('Weak password, change it!')


created_password = random_password.creates_password()
checks_password(created_password)
