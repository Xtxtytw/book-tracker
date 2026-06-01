import json
import os

# Имя файла для хранения данных
DB_FILE = "books.json"


def load_books():
    """Загружает список книг из JSON-файла.

    Если файл не найден, возвращает пустой список.
    """
    if not os.path.exists(DB_FILE):
        return []

    try:
        with open(DB_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Ошибка: Файл данных поврежден. Создан новый список.")
        return []


def save_books(books):
    """Сохраняет текущий список книг в JSON-файл с отступами для читаемости."""
    try:
        with open(DB_FILE, "w", encoding="utf-8") as file:
            json.dump(books, file, ensure_ascii=False, indent=4)
    except IOError:
        print("Ошибка: Не удалось сохранить данные в файл.")


def is_duplicate(books, author, title):
    """Проверяет, существует ли уже книга с таким автором и названием.

    Регистр символов (заглавные/строчные) и лишние пробелы игнорируются.
    """
    for book in books:
        if (
            book["author"].strip().lower() == author.strip().lower()
            and book["title"].strip().lower() == title.strip().lower()
        ):
            return True
    return False


def add_book(books):
    """Запрашивает данные у пользователя и добавляет новую книгу в список."""
    pass


def list_and_stats(books, mode="all"):
    """Универсальная функция для вывода списков и расчета статистики."""
    pass


def delete(books):
    """Выводит список книг и удаляет выбранную пользователем книгу по ее номеру."""
    if not books:
        print("\nВаш трекер пуст. Удалять нечего.")
        return books

    list_and_stats(books, mode="all")

    print("\n--- Удаление книги ---")
    while True:
        try:
            choice = input(
                "Введите номер книги для удаления (или '0' для отмены): "
            )
            choice_idx = int(choice)

            if choice_idx == 0:
                print("Удаление отменено.")
                return books

            if 1 <= choice_idx <= len(books):
                removed_book = books.pop(choice_idx - 1)
                save_books(books)
                print(
                    f"Успешно: Книга '{removed_book['title']}' "
                    f"автора {removed_book['author']} удалена."
                )
                return books

            print(f"Неверный номер. Введите число от 1 до {len(books)}.")
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите корректное число.")



def main():
    """Основной цикл управления консольным меню."""
    books = load_books()

    while True:
        print("\n=== МЕНЮ ТРЕКЕРА КНИГ ===")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("\nВыберите действие (1-6): ").strip()

        if choice == "1":
            books = add_book(books)
        elif choice == "2":
            list_and_stats(books, mode="all")
        elif choice == "3":
            list_and_stats(books, mode="rating")
        elif choice == "4":
            list_and_stats(books, mode="authors")
        elif choice == "5":
            books = delete(books)
        elif choice == "6":
            print("\nСпасибо за использование трекера! До свидания!")
            break
        else:
            print("\nНеверный пункт меню. Пожалуйста, повторите ввод.")


if __name__ == "__main__":
    main()
