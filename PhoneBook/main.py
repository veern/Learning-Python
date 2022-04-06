from PhoneBook import PhoneBook, Contact
import requests
import html

ENDPOINT = 'https://randomuser.me/api/'
AMOUNT_TO_GENERATE = 3

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
    # Book = generate_sample_PhoneBook(AMOUNT_TO_GENERATE)
    # Book.save(r"C:\Users\Krystian-Laptop\Desktop\Python\Moje\Katas\PhoneBook\Phonebook.txt")
    Book = PhoneBook()
    Book.load(r"C:\Users\Krystian-Laptop\Desktop\Python\Moje\Katas\PhoneBook\Phonebook.txt")
    Shane = Contact("Shane", "Dawson", 239238123)
    Dave = Contact("Dave", "Tribiani", 123456789)
    Book.add_contact(Dave, Shane)
    Book.del_contact("Dave", "Tribiani")
    print(Book.contacts)
    # print(Book)

if __name__ == "__main__":
    main()