def from_file(file):
    with open(file, 'Phonebook.txt', encoding='utf-8') as data:
        dictionary = data.read()
    return dictionary
