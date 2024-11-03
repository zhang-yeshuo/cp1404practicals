def extract_name_from_email(email):
    name_part = email.split('@')[0]
    name_components = name_part.replace('.', ' ').split()
    return ' '.join(name_components).title()


def get_user_email_and_names():
    users = {}
    email=input("Email: ")

    while email != '':
        suggested_name = extract_name_from_email(email)
        confirmation = input(f"Is your name {suggested_name}? (Y/n): ").lower()

        if confirmation not in ['y', 'yes', '']:
            name = input("Name: ")
        else:
            name = suggested_name

        users[email] = name
        email = input("Email: ")

    return users


def print_user_info(users):
    for email, name in users.items():
        print(f"{name} ({email})")


user_dict = get_user_email_and_names()
print_user_info(user_dict)
