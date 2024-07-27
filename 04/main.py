from handlers import (
    parse_input,
    add_contact,
    change_contact,
    show_contact,
    show_all_contacts
)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)

            if command is None:
                print("Please enter a command.")
                continue

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
                print(show_contact(args, contacts))
            elif command == "all":
                print(show_all_contacts(contacts))
            else:
                print("Invalid command.")

        except KeyboardInterrupt:
            print("\nGood bye!")
            break


if __name__ == "__main__":
    main()
