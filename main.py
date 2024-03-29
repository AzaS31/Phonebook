import json
import os

# Функция очистки консоли для удобство
def clear_console():
    if os.name == 'nt':  # для Windows
        os.system('cls')
    else:  # для Linux и macOS
        os.system('clear')

# Сохранения контактов
def save_contacts(contacts):
    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False)

# Загрузка контактов
def load_contacts():
        with open("contacts.json", "r", encoding="utf-8") as f:
            return json.load(f)

# Функция для добавления контактов
def add_contact(contacts):
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronomyc = input("Введите отчество: ")
    email = input("Введите электронную почту: ")

    mobile_numbers = []
    while True:
        numbers = input("Введите номер телефона (или оставьте пустым для завершения): ")
        if not numbers:
            break
        mobile_numbers.append(numbers)
    
    contact = {
        'surname': surname,
        'name': name,
        'patronomyc': patronomyc,
        'email': email,
        'mobile_numbers': mobile_numbers
    }  

    contacts.append(contact)
    print("Контакт успешно добавлен")

# Функция для поиска контактов
def find_contact(query, contacts):
    found_contacts = []
    for contact in contacts:
        if query.lower() in contact['surname'].lower() or \
           query.lower() in contact['name'].lower() or \
           query.lower() in contact['patronomyc'].lower() or \
           query in contact['mobile_numbers']:
            found_contacts.append(contact)
    return found_contacts

# Функция для отображения найденных контактов
def search_contacts(contacts):
    search_query = input("Введите фамилию, имя, отчество или номер телефона для поиска: ")
    result = find_contact(search_query, contacts)

    if result:
        print("Найденные контакты:")
        for contact in result:
            contact_info = f"{contact['surname']} {contact['name']} {contact['patronomyc']}, email: {contact['email']}, телефоны: {', '.join(contact['mobile_numbers'])}"
            print(contact_info)
    else:
        print("Контакт не найден.")

# Функция для отображения всех контактов
def display_contacts(contacts):
    for contact in contacts:
            contact_info = f"{contact['surname']} {contact['name']} {contact['patronomyc']}, email: {contact['email']}, телефоны: {', '.join(contact['mobile_numbers'])}"
            print(contact_info)

# Функция для изменения контактов
def change_contacts(contacts):
    search_query = input("Введите фамилию, имя, отчество или номер телефона для поиска: ")
    results = find_contact(search_query, contacts)

    if not results:
        print("Контакт не найден.")
        return

    for i, contact in enumerate(results, start=1):
        contact_info = f"{i}. {contact['surname']} {contact['name']} {contact['patronomyc']}, email: {contact['email']}, телефоны: {', '.join(contact['mobile_numbers'])}"
        print(contact_info)
    
    contact_choice = int(input("Введите номер контакта для изменения: ")) - 1
    if 0 <= contact_choice < len(results):
        chosen_contact = results[contact_choice]

        def ask_save_or_continue():
            while True:
                choice = input("Сохранить изменения и выйти ('1') или продолжить редактирование ('2')?: ")
                if choice.lower() == '1':
                    save_contacts(contacts)
                    print("Изменения сохранены.")
                    return True  
                elif choice.lower() == '2':
                    return False 
                else:
                    print("Некорректный ввод. Пожалуйста, выберите '1' или '2'.")

        while True:
            print("\nЧто вы хотите изменить?")
            print("1. Фамилия")
            print("2. Имя")
            print("3. Отчество")
            print("4. Электронная почта")
            print("5. Номера телефонов")
            print("6. Вернуться назад")

            choice = input("Выберите опцию: ")

            if choice == '1':
                chosen_contact['surname'] = input("Введите новую фамилию: ")
                if ask_save_or_continue():
                    break
            elif choice == '2':
                chosen_contact['name'] = input("Введите новое имя: ")
                if ask_save_or_continue():
                    break
            elif choice == '3':
                chosen_contact['patronomyc'] = input("Введите новое отчество: ")
                if ask_save_or_continue():
                    break
            elif choice == '4':
                chosen_contact['email'] = input("Введите новый email: ")
                if ask_save_or_continue():
                    break
            elif choice == '5':
                print("Текущие телефоны: " + ", ".join(chosen_contact['mobile_numbers']))
                change_phones = input("Введите новые номера телефонов через запятую: ")
                chosen_contact['mobile_numbers'] = [phone.strip() for phone in change_phones.split(",")]
                if ask_save_or_continue():
                    break
            elif choice == '6':
                break
            else:
                print("Некорректный ввод. Пожалуйста, попробуйте снова.")

# Функция удаления контактов
def remove_contacts(contacts):
    search_query = input("Введите фамилию, имя, отчество или номер телефона для поиска: ")
    results = find_contact(search_query, contacts)

    if results:
        for i, contact in enumerate(results, start=1):
            contact_info = f"{i}. {contact['surname']} {contact['name']} {contact['patronomyc']}, email: {contact['email']}, телефоны: {', '.join(contact['mobile_numbers'])}"
            print(contact_info)
        contact_choice = int(input("Введите номер контакта для удаления: ")) - 1
        if 0 <= contact_choice < len(results):
            contacts.remove(results[contact_choice])
            print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")



def main():
    clear_console()
    contacts = load_contacts()

    while True:
        print("\n1. Добавить контакт\n2. Найти контакт\n3. Показать все контакты\n4. Изменить контакт\n5. Удалить контакт\n6. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            clear_console()
            add_contact(contacts)
        elif choice == '2':
            clear_console()
            search_contacts(contacts)
        elif choice == '3':
            clear_console()
            display_contacts(contacts)
        elif choice == '4':
            clear_console()
            change_contacts(contacts)
        elif choice == '5':
            clear_console()
            remove_contacts(contacts)             
        elif choice == '6':
            break
        else:
            print("Неверный ввод. Попробуйте снова.")
        save_contacts(contacts)

main()