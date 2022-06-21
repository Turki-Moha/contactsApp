contacts = {}

def display_contacts():
    print('Number\t\t\tname')
    for key in contacts:
        print("{}\t\t{}".format(key,contacts.get(key)))

while True:
    n = int(input('[1] Add\n[2] Search\n[3] Display all'))
    if n == 1:
        name = input('Contact name')
        number = input('Enter the number')
        if len(number) ==10:
            contacts[number] = name
        else:
            print('This is invalid number')
    elif n == 2:
        find_n = input("enter the number of the contact")
        if len(find_n) == 10 and find_n.isdigit():
            if find_n in contacts:
                print(find_n,'contact name is',contacts[find_n])
            else:
                print('Sorry, the number is not found ')
        else:
            print('invalid format')
    elif n ==3:
        if not contacts:
            print('no contacts found')
        else:
            display_contacts()
    else:
        break