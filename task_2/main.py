import json# Добавляем библиотеку json

file_name = "dump.json"# Создаём переменную file_name и присвайваем ей название json файла

try:# Пробуем 
    with open(file_name, 'r', encoding='utf-8') as file:# Открыть файл file_name на чтение
        data = json.load(file)# Переменной data присвайваем содержимое файла file_name
except FileNotFoundError:# Проверяем на ошибку FileNotFoundError
    print(f"Файл {file_name} не найден!!!!!")# Если она есть, то выводим этот текст
except Exception as e:# Проверяем на ошибку Exception e
    print(f"Произошла ошибка: {e}")# Если она есть, то выводим этот текст

qualification_input = input("Введите номер квалификации: ")# Просим пользователя ввести строку для поиска с клавиатуры

found_list = []# Создаём пустой список

for item in data:# Создаём цикл, который будет пробегаться по переменной data, которую мы создали раньше
    fields = item.get("fields", {})
    item_code = fields.get("code")

    if  item_code == qualification_input:
        model = item.get("model")
        title = fields.get("title")
        output_line = ""

        if model == "data.specialty":
            c_type = fields.get("c_type", "")
            output_line = f"{item_code} >> Специальность \"{title}\", {c_type}"
        elif model == "data.skill":
            output_line = f"{item_code} >> Квалификация \"{title}\""

        if output_line:
            found_list.append(output_line)

if found_list:
    print("=============== Найдено ===============")
    for i in found_list:
        print(i)
else:
    print("=============== Не найдено ===============")

