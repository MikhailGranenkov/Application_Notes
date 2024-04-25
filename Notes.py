# Задание
# Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок. Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки. Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой). Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры запуска программы (команда, данные), можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.Например:
# python note.py
# Введите команду: add
# Введите заголовок заметки: новая заметка Введите тело заметки: тело новой заметки Заметка успешно сохранена
# Введите команду:
# При чтении списка заметок реализовать фильтрацию по дате.


import json
from datetime import datetime

# Функция для загрузки заметок из файла JSON
def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []  # Если файл не найден, возвращаем пустой список заметок
    return notes

# Функция для сохранения заметок в файл JSON
def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

# Функция для добавления новой заметки
def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Получаем текущую дату и время
    note = {
        "id": len(notes) + 1,  # ID заметки увеличивается на 1 относительно количества уже существующих заметок
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)  # Добавляем новую заметку в список
    save_notes(notes)   # Сохраняем список заметок в файл
    print("Заметка успешно сохранена")

# Функция для чтения списка заметок с фильтрацией по дате
def read_notes():
    filter_date = input("Введите дату для фильтрации (гггг-мм-дд): ")
    filtered_notes = [note for note in notes if note["timestamp"].startswith(filter_date)]  # Фильтруем заметки по дате
    if filtered_notes:
        print("Список заметок за выбранную дату:")
        for note in filtered_notes:
            print(f"{note['id']}: {note['title']} - {note['timestamp']}")
    else:
        print("Нет заметок за выбранную дату")

# Функция для редактирования заметки
def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            note["title"] = input("Введите новый заголовок заметки: ")
            note["body"] = input("Введите новое тело заметки: ")
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Обновляем дату и время изменения заметки
            save_notes(notes)  # Сохраняем изменения
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным ID не найдена")

# Функция для удаления заметки
def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)  # Удаляем заметку из списка
            save_notes(notes)   # Сохраняем изменения
            print("Заметка успешно удалена")
            return
    print("Заметка с указанным ID не найдена")

# Основной блок кода
if __name__ == "__main__":
    notes = load_notes()  # Загружаем список заметок из файла
    while True:
        command = input("Введите команду (add/read/edit/delete/exit): ").strip().lower()
        if command == "add":
            add_note()
        elif command == "read":
            read_notes()
        elif command == "edit":
            edit_note()
        elif command == "delete":
            delete_note()
        elif command == "exit":
            break
        else:
            print("Неверная команда")
