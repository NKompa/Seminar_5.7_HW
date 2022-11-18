def All_view():
    with open('phonebook.csv', encoding='utf-8') as book:
        data = book.read()
        return data

def Web_view():
    with open('phonebook.csv', encoding='utf-8') as book:
        data = book.readlines()
        return data