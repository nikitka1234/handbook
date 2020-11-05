from main import InformationAboutPerson


class Handbook:

    name = ''
    handbook = []

    def __init__(self, name):
        self.name = name

    def registration_person(self, first_name, last_name, phone_number, city, email_address):
        person = InformationAboutPerson(first_name, last_name, phone_number, city, email_address)
        self.handbook.append(person)

    def search_by_email_address(self):
        person_0 = InformationAboutPerson('Такой', 'email', 'address', 'не', 'существует')
        for obj in self.handbook:
            if obj.email_address == input('Введите email address: '):
                person_0 = obj
        return person_0

    def delete_person(self):
        self.handbook.remove(input('Введите email address: '))
