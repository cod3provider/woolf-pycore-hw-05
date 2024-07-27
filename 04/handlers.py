from decorator import input_error


def parse_input(user_input):
    if not user_input.strip():
        return None, []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Give me name and phone please.")
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Give me name and phone please.")
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated."
    else:
        raise KeyError("Contact not found.")


@input_error
def show_contact(args, contacts):
    if len(args) != 1:
        raise IndexError("Please provide a name.")
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        raise KeyError("Contact not found.")


@input_error
def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
