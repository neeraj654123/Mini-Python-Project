class PhoneBook:
    phone_directory=[]

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number    
        PhoneBook.phone_directory.append(self)

    def show_contacts(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}"


    @classmethod
    def show_all_contacts(cls):
        print(f"The contacts are: \n") 
        if  len(cls.phone_directory)==0:
            print("Phonebook is empty!")
        else:
            for contact in cls.phone_directory:
                print(contact.show_contacts()) 
    @classmethod
    def search_contact(cls,search_contact):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_contact.lower():
                return print(contact.show_contacts())

        else:
            print(f"Contact not found! for {search_contact}")    

    @staticmethod
    def validate_contact(number):
        if len(number) >=8 and number.isdigit():
            return True
        else:
            return False

n_contacts = int(input("How many contacts you want to add: "))
for i in range(n_contacts):
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    if PhoneBook.validate_contact(phone_number):
        PhoneBook(name, phone_number)
    else:
        print(f"Invalid phone number! for {phone_number}")

c1 =PhoneBook("John", "1234567890")
c2 =PhoneBook("Jane", "0987654321")
c3 = PhoneBook("Doe", "1234567890")
c4 = PhoneBook("Mike", "1234567890") 
PhoneBook.show_all_contacts()
PhoneBook.search_contact(input("Enter the name to search: "))  

    
    

        