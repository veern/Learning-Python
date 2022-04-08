from Contact import Contact
import json

class PhoneBook:
    contacts = []
    
    @property
    def size(self):
        return len(self.contacts)

    def load(self, file: str) -> None:
        """Reads the phone book from a file"""
        with open(file, "r") as f:
            self.contacts = json.loads(f.read())
    
    def save(self, destination: str) -> None:
        """Saves the phone book as a dictionary to a file designated by the user"""
        with open(destination, "w") as f:
            f.write(json.dumps(self.contacts, indent=4))

    def add_contact(self, *people_to_add: Contact) -> None:
        """Add a contact to a phone book"""
        for person in people_to_add:
            personal_information = {
                "Name": person.name.capitalize(),
                "Lastname": person.lastname.capitalize(),
                "Phone number": person.phone_number
                }
            self.contacts.append(personal_information)

    def del_contact(self, name: str, lastname: str) -> None:
        """Delete a contact from a phone book"""
        for i, person in enumerate(self.contacts):
            if (person['Name'], person['Lastname']) == (name.capitalize(), lastname.capitalize()):
                self.contacts.pop(i)
                print(f"\n{name.capitalize()} {lastname.capitalize()} deleted.\n")
                break
        else:
            print(f"\nNo {name} {lastname} found in the Phone book.\n")

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        strng = ""
        for contact in self.contacts:
            for key, value in contact.items():
                strng = f"{strng}{key}: {value}\t\t"
            strng = f"{strng}\n"
        return strng

    def __repr__(self) -> str:
        return f"PhoneBook class: {self.contacts}"