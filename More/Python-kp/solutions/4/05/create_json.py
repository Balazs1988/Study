import json


def creates_json():
    name = input('Type your name: ')
    email = input('Type your email: ')
    age = int(input('Type your age: '))
    with open('user.json', 'w') as json_file:
        json_file.write(json.dumps({'name': name, 'email': email, 'age': age}))
