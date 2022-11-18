def Search_Entry():
    count = 0
    search_info = input('Введите данные: ')
    with open('phonebook.csv',encoding='utf-8') as book:
        for line in book:
            if search_info in line:
                print(line, end='')
                count+=1
    if count==0:
        print(f'\nТаких данных нет.\n')