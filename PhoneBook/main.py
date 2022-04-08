from PhoneBook import PhoneBook, Contact
import requests
import html
import os

ENDPOINT = 'https://randomuser.me/api/'
AMOUNT_TO_GENERATE = 3

def call_request(url, params=[]):
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r
# parameters = {"amount": 20}

def generate_contact() -> Contact:
    r = call_request(ENDPOINT).json()
    r = r["results"][0]
    name, lastname, phone_number = html.unescape(str(r['name']['first'])), html.unescape(str(r['name']['last'])), html.unescape(str(r['phone']))
    return Contact(name, lastname, phone_number)

def generate_sample_PhoneBook(amount: int) -> PhoneBook:
    Book = PhoneBook()
    for _ in range(amount):
        person = generate_contact()
        Book.add_contact(person)
    return Book

def engine() -> None:
    os.system("cls")
    possible_actions = ["SAVE", "LOAD", "ADD", "DELETE", "DISPLAY", "SAMPLE"]
    print("Welcome to the phone book simulator.\nFollowing actions are possible:\n1.Load a PhoneBook\n2.Save a PhoneBook\n3.Add a contact\n4.Delete a contact\n5.Display all contacts\n")
    phone_book = PhoneBook()
    while True:
        action = input(f'Your choice of action {possible_actions}: ').upper()
        if action not in possible_actions:
            continue
        elif action == "SAVE":
            address = input("Give a full path to where to save this PhoneBook to: ")
            name_of_phone_book_file = input("Name the file to save the PhoneBook: ")
            phone_book.save(f"{address}\{name_of_phone_book_file}")
        elif action == "LOAD":
            while True:
                try:
                    address_of_file_to_load = input("Give a full path of a file to load a PhoneBook: ")
                    break
                except FileNotFoundError:
                    print("File not found!")
            phone_book.load(address_of_file_to_load)
        elif action == "ADD":
            person = input("Give a persons name, lastname and phone number, each separated by a single space: ")
            person = person.split(" ")
            contact = Contact(person[0], person[1], int(person[2]))
            phone_book.add_contact(contact)
        elif action == "DELETE":
            person = input("Give a persons name and lastname, each separated by a single space, that you want to delete from a phone book: ") 
            person = person.split(" ")
            phone_book.del_contact(person[0], person[1])
        elif action == "DISPLAY":
            print(phone_book)
        elif action == "SAMPLE":
            phone_book = generate_sample_PhoneBook(AMOUNT_TO_GENERATE)

def main():
    engine()

if __name__ == "__main__":
    main()