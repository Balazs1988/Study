class Person:
    def __init__(self, person_id, first_name, family_name):
        self.person_id = person_id
        self.first_name = first_name
        self.family_name = family_name


class Developer(Person):
    def __init__(self, person_id, first_name, family_name, languages: set):
        super().__init__(person_id, first_name, family_name)
        self.languages = languages


class DeveloperDatabase:
    developers = []


def add_developer(add_id, add_firstname, add_familyname, add_languages):
    curr_dev = Developer(add_id, add_firstname, add_familyname, add_languages)
    DeveloperDatabase.developers.append(curr_dev)


def remove_developer(rem_id):
    for i in DeveloperDatabase.developers:
        if i.person_id == rem_id:
            DeveloperDatabase.developers.remove(i)


def collect_developers_by_languages():
    dev_by_languages = {}
    for i in DeveloperDatabase.developers:
        for j in i.languages:
            if j in dev_by_languages:
                names_list = list(dev_by_languages[j])
                names_list.append(i.person_id)
                dev_by_languages[j] = names_list
            else:
                dev_by_languages[j] = i.person_id
    print(dev_by_languages)


def find_developer(find_name):
    for i in DeveloperDatabase.developers:
        if i.family_name == find_name:
            print(f'Id: {i.person_id}, Name: {i.first_name} {i.family_name}, Languages: {i.languages}')


def highest_languages():
    count = 0
    person = 0
    for i in DeveloperDatabase.developers:
        if count < len(i.languages):
            count = len(i.languages)
            person = i.person_id
    for j in DeveloperDatabase.developers:
        if j.person_id == person:
            print(f'The highest number of known languages is {count} by Id: {j.person_id}, Name: {j.first_name} '
                  f'{j.family_name}, Languages: {j.languages}')


add_developer('1', 'Peter', 'Klinga', {'Python', 'HTML', 'CSS', 'Bootstrap'})
add_developer('2', 'Pete', 'Key', {'Python', 'HTML'})
add_developer('3', 'Pet', 'Ka', {'Python', 'Bootstrap'})
remove_developer('2')
collect_developers_by_languages()
find_developer('Klinga')
highest_languages()

