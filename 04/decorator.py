def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Error: Missing arguments."
    return inner
