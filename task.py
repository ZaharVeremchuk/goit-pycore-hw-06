from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    # реалізація класу
		pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone: str) -> None:
        if re.match("\d{10}", phone):
            self.phones.append(Phone(phone))
        else:
            print("Phone need to have 10")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
          for phone in self.phones:
                if phone.value == old_phone:
                      phone.value = new_phone

    def find_phone(self, phone: str) -> str:
          for ph in self.phones:
                if ph.value == phone:
                    return phone
          return "Phone not found"
    
    def remove_phone(self, phone : str) -> None:
          for ph in self.phones:
                if ph.value == phone:
                      self.phones.remove(ph) 
                      
class AddressBook(UserDict):
    
    def add_record(self, record: Record):
          self.data[record.name.value] = record

    def find(self, name: str) -> Record:
          return self.data.get(name)
    
    def delete(self, name: str) -> None:
          self.data.pop(name)


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

# Видалення телефону
john.remove_phone("5555555555")
print(john)
