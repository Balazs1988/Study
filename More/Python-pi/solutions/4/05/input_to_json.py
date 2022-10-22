import json


if __name__ == '__main__':
    person_data = {}
    person_data['name'] = input('Name? ')
    person_data['email'] = input('E-mail? ')
    person_data['age'] = int(input('Age? '))
    with open('person.json', 'w') as json_file:
        json.dump(person_data, json_file)
