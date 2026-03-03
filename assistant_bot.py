# assistant_bot.py

def parse_input(user_input):
    """Розбирає рядок користувача на команду та аргументи"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """Додає новий контакт у словник"""
    if len(args) < 2:
        return "Error: please provide name and phone."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """Змінює номер телефону існуючого контакту"""
    if len(args) < 2:
        return "Error: please provide name and new phone."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Error: contact '{name}' not found."

def show_phone(args, contacts):
    """Показує номер телефону для контакту"""
    if len(args) < 1:
        return "Error: please provide a name."
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return f"Error: contact '{name}' not found."

def show_all(contacts):
    """Виводить всі контакти"""
    if not contacts:
        return "No contacts found."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue  # пропускаємо пустий ввід

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()