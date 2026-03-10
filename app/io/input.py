import pandas as pd

# Функція для вводу тексту з консолі
def input_from_console():
    """ 
    Зчитує текст, введений користувачем з консолі

    Повертає:
    Текст, введений користувачем
    """
    text = input("Введіть текст: ")
    return text

# Функція для зчитування тексту з файлу за допомогою вбудованих можливостей python
def read_text_from_file(file_path):
    """
    Зчитує текст з файлу за допомогою вбудованих можливостей python

    Аргументи:
    file_path: шлях до файлу

    Повертає:
    Вміст файлу
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

# Функція для зчитування даних з файлу за допомогою бібліотеки pandas
def read_data_from_file(file_path):
    """
    Зчитує дані з файлу за допомогою бібліотеки pandas
    
    Аргументи:
    file_path: шлях до файлу

    Повертає:
    Дані, зчитані з файлу
    """
    data = pd.read_csv(file_path)
    return data