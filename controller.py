import m_New
import view
import m_Search
import m_Web


def Choose():
    while True:
        print('\n1. Добавить новый контакт; 2. Посмотреть все контакты; 3. Найти контакт; 4. Выгрузить в web все контакты; 5. Выход')
        choice = input('\nВыберите вариант и введите цифру: ')
        if choice == '1':
            m_New.New_Entry()
        if choice == '2':
            print(f'\n{view.All_view()}')
        if choice == '3':
            m_Search.Search_Entry()
        if choice == '4':
            m_Web.All_Web()
        if choice == '5':
            print('\nКонец!\n')
            break