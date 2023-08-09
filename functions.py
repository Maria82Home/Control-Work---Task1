from datetime import date

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. вывод всех заметок из файла\n"
          "2. добавление заметки\n"
          "3. удаление заметки\n"
          "4. редактирование заметки\n"
          "5. выборка заметок по дате\n"
          "6. показать заметку по id\n"
          "7. выход\n")
    choice = int(input())
    return choice

def work_with_notebook():
    choice = show_menu()
    notebook = read_csv('notebook.csv')


    while (choice != 7):
        if choice == 1:
            print_result(notebook)
        elif choice == 2:
            note = get_new_note()
            add_note(notebook, note)
            write_txt('notebook.csv', notebook)
        elif choice == 3:
            id = get_id()
            delete_note(notebook, id)
            write_txt('notebook.csv', notebook)
        elif choice == 4:
            id = get_id()
            changes = get_new_note()
            make_changes(notebook, changes, id)
            write_txt('notebook.csv', notebook)
        elif choice == 5:
            date = get_date()
            print(find_by_date(notebook, date))
        elif choice == 6:
            id = get_id()
            print(find_by_id(notebook, id))
        choice = show_menu()

def read_csv(filename: str) -> list:
    notes = []
    with open(filename, 'r', encoding='utf-8') as filein:
        for line in filein:
            note = {}
            list = line.split(',') 
            note['Id'] = list[0]
            note['Title'] = list[1].strip()
            note['Content'] = list[2].strip()
            note['Date'] = str(date.today())
            notes.append(note)
    return notes

def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def delete_note(data: list, id: str):
    for el in data:
        if el.get("Id") == id:
            return data.pop(data.index(el))
    return "Note doesn't exist"

def make_changes(notes: list, line:str, id:str):
    for note in notes:
        if note['Id'] == id:
            list = line.split(',') 
            note['Id'] = list[0]
            note['Title'] = list[1].strip()
            note['Content'] = list[2].strip()
            note['Date'] = str(date.today())
            return notes

def find_by_date(data: list, date: str) -> str:
    for el in data:
        if el.get("Date") == date:
            return f'Id: {el.get("Id")}; Title: {el.get("Title")}; Content: {el.get("Content")}; Date: {el.get("Date")}'
    return "Note doesn't exist"

def find_by_id(data: list, id: str) -> str:
    for el in data:
        if el.get("Id") == id:
            return f'Id: {el["Id"]}; Title: {el.get("Title")}; Content: {el.get("Content")}; Date: {el.get("Date")}'   
    return "Note doesn't exist"

def add_note(notes:list, line: str):
    note = {}
    list = line.split(',') 
    note['Id'] = list[0]
    note['Title'] = list[1].strip()
    note['Content'] = list[2].strip()
    note['Date'] = str(date.today())
    notes.append(note)

def print_result(data: list):
    for item in data:
        for k,v in item.items():
            print(k,v)
        print('\n')

def get_date():
    return input('Введите date: ')

def get_id():
    return input('Введите id: ')

def get_new_note():
    return input('Введите id, title, note content, date: ')

def get_file_name():
    return input('Введите название файла: ')

