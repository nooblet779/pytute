filename = 'guest.txt'


def get_formatted_name(first_name, last_name):
    """Return a full name , neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()


    # This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First_name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")

    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)

with open(filename, 'a') as file_object:
    file_object.write("\nWelcome " + formatted_name.title() + "!")
    print("\nWelcome, " + formatted_name.title() + "!")
