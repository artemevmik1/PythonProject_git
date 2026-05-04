import re
from config import NAMES_TXT

def clear_names (file_name: str) -> list:
    """ функция, для оочистки имен от лишгних символов """
    new_names_list = list()
    with open(file_name, 'r', encoding='utf-8') as names_file:
        names_list = names_file.read().split()
        for name_item in names_list:
            new_name = ''
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_names_list.append(new_name)
    return new_names_list



def is_cyrillic (name_item: str, pattern=None) -> bool:
    """ проверкка на вхождение кириллицы в строку"""
    return bool(re.search('[а-яА-Я]', name_item))


def filter_russian_names (names_list: list) -> list:
    """фильтрация имен написанных на русском"""
    new_names_list = list()
    for name_item in names_list:
        if is_cyrillic(name_item):
            new_names_list.append(name_item)
    return new_names_list


def save_to_file(file_name: str, data: str) -> None:
    """Сохраняет данные в файл"""
    with open(file_name, 'w', encoding='utf-8') as names_file:
        names_file.write(data)



if __name__ == '__main__':
    cleared_name = clear_names(NAMES_TXT)

    #for i in cleared_name:
     #   print(i)

    filtered_names = filter_russian_names(cleared_name)
    save_to_file('russian_names.txt', '\n'.join(filtered_names)   )