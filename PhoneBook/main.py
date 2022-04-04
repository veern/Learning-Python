from PhoneBook import PhoneBook, Contact
import requests
import json
import html

ENDPOINT = 'https://randomuser.me/api/'
AMOUNT_TO_GENERATE = 20

def call_request(url, params=[]):
    r = requests.get(url)
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

def main():
    Book = generate_sample_PhoneBook(AMOUNT_TO_GENERATE)
    Book.save(r"C:\Users\Krystian-Laptop\Desktop\Python\Moje\Katas\PhoneBook\Phonebook.txt")

if __name__ == "__main__":
    main()