import random
import string


def check_password(password: str) -> bool:
    """
    Check that the password is strong enough!
    - It should be at least 8 characters long,
    - It should contain at least one letter, number and other character.
    :param password: password
    :return: True, on strong password, else False
    """
    if len(password) < 8:
        return False
    n_letters = 0
    n_numbers = 0
    n_others = 0
    for c in password:
        if c.isalpha():
            n_letters += 1
        elif c.isdigit():
            n_numbers += 1
        else:
            n_others += 1
    if n_letters and n_numbers and n_others:
        return True
    else:
        return False


def generate_password() -> str:
    """
    Generate a random password.
    :return: the generated password
    """
    password = ''
    n_letters = random.randint(3, 5)
    for _ in range(n_letters):
        password += random.choice(string.ascii_letters)
    n_numbers = random.randint(3, 5)
    for _ in range(n_numbers):
        password += random.choice(string.digits)
    n_others = random.randint(3, 5)
    for _ in range(n_others):
        password += random.choice(string.punctuation)
    chars = list(password)
    random.shuffle(chars)
    password = ''.join(chars)
    return password


if __name__ == '__main__':
    new_password = generate_password()
    assert check_password(new_password)
    print(f'Password: {new_password}')
