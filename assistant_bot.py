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
    
    commands = {
        "hello": lambda args: print("How can I help you?"),
        "add": lambda args: print(add_contact(args, contacts)),
        "change": lambda args: print(change_contact(args, contacts)),
        "phone": lambda args: print(show_phone(args, contacts)),
        "all": lambda args: print(show_all(contacts)),
        "exit": lambda args: exit("Good bye!"),
        "close": lambda args: exit("Good bye!"),
    }

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue

        command, *args = parse_input(user_input)

        # Викликаємо команду через словник або повідомляємо про невідому
        if command in commands:
            commands[command](args)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()