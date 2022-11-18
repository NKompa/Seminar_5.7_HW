def New_Entry():
    name = input('Введите имя: ')
    sirname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    with open('phonebook.csv','a', encoding='utf-8') as book:
        book.write(f'{sirname}, {name}, {phone}, {comment};\n')