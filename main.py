class InformationAboutPerson:

    first_name = ''
    last_name = ''
    phone_number = ''
    city = ''
    email_address = ''

    def __init__(self, first_name, last_name, phone_number, city, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.city = city
        self.email_address = email_address

    def data_print(self):
        print(self.first_name, self.last_name, self.phone_number, self.city, self.email_address)
