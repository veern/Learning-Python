class Contact:

    def __init__(self, name: str, lastname: str, phone_number: int) -> None:
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number

    def __str__(self) -> str:
        return f"Full name: {self.name} {self.lastname}, Phone_number: {self.phone_number}, email: {self.email}"

    @property
    def email(self) -> str:
        return f"{self.name}.{self.lastname}@email.com"

    @email.setter
    def email(self, name: str, lastname: str) -> str:
        self.email = f"{name}.{lastname}@email.com"

        