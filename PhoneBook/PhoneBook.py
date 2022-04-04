from textwrap import indent
from Contact import Contact
import json

class PhoneBook:
    contacts = {}
    
    @property
    def size(self):
        return len(self.contacts)

    def save(self, destination: str) -> None:
        """Saves the phone book as a dictionary to a file designated by the user"""
        with open(destination, "w") as f:
            f.write(json.dumps(self.contacts, indent=4))

    def add_contact(self, *contact: Contact) -> None:
        for person in contact:
            self.contacts[self.size] = {
                "Name": person.name,
                "Lastname": person.lastname,
                "Phone number": person.phone_number
                }

    def del_contact(self, name: str, lastname: str) -> None:
        for i, person in enumerate(self.contacts):
            if (person['name'], person['lastname']) == (name, lastname):
                self.contacts.pop(i)

    def __len__(self) -> int:
        return self.size
