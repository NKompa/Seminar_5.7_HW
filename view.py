def All_view():
    with open('phonebook.csv', encoding='utf-8') as book:
        data = book.readlines()
        return data

print(All_view())