from Contact import Contact
import json

class PhoneBook:
    contacts = {}
    
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

    def add_contact(self, *contact: Contact) -> None:
        """Add a contact to a phone book"""
        for person in contact:
            self.contacts[self.size] = {
                "Name": person.name,
                "Lastname": person.lastname,
                "Phone number": person.phone_number
                }

    def del_contact(self, name: str, lastname: str) -> None:
        """Delete a contact from a phone book"""
        for i, person in self.contacts.items():
            if (person['Name'], person['Lastname']) == (name, lastname):
                self.contacts.pop(i)
                print(f"\n{name} {lastname} deleted.\n")
                break
        else:
            print(f"\nNo {name} {lastname} found in the Phone book.\n")

    def refresh_numeration_of_contacts(self) -> None:
        i = 0
        for number, person in self.contacts.items():
            if number != str(i):
                tmp = Contact(person['Name'], person['Lastname'], person['Phone number'])
                self.contacts.pop(number)
                self.contacts[str(i)] = tmp
            i += 1

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        strng = ""
        for number, contact in self.contacts.items():
            strng = f"{strng}\n{number}.\t"
            for key, value in contact.items():
                strng = f"{strng}{key}: {value}\t\t\t"
        return strng

    def __repr__(self) -> str:
        return f"PhoneBook class: {self.contacts}"