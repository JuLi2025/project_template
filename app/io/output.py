# Функція для виводу тексту у консоль
def output_to_console(text):
    """
    Виводить текст у консоль

    Аргументи:
    text: Текст, який потрібно вивести
    """
    print(text)

# Функція для запису тексту у файл за допомогою вбудованих можливостей python
def write_to_file(file_path, text):
    """
    Записує текст у файл за допомогою вбудованих можливостей python

    Аргументи:
    file_path:  шлях до файлу
    text: текст, який потрібно записати у файл
    """
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(text + "\n")