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
    fields = item.get("fields", {})# Извлекает значение по ключу "fields" из текущего item, или пустой словарь, если ключ отсутствует
    item_code = fields.get("code")# Извлекает значение по ключу "code" из текущего fields

    if  item_code == qualification_input:# Условная проверка: выполняет следующий блок если извлеченный item_code совпадает с искомым qualification_input
        model = item.get("model")# Извлекает значение по ключу "model" из текущего item
        title = fields.get("title")# Извлекает значение по ключу "title" из текущего fields
        output_line = ""# Инициализирует переменную как пустую строку

        if model == "data.specialty":# Проверяем равны ли значения переменной model и "data.specialty"
            c_type = fields.get("c_type", "")# Извлекает значение по ключу "fields" из текущего item, или пустой словарь, если ключ отсутствует
            output_line = f"{item_code} >> Специальность \"{title}\", {c_type}"# Выводим форматированную строку
        elif model == "data.skill":# Проверяем равны ли значения переменной model и "data.skill"
            output_line = f"{item_code} >> Квалификация \"{title}\""# Выводим форматированную строку

        if output_line:# Проверяем: если строка output_line не пуста, то
            found_list.append(output_line)# Добавляем её в созданный ранее список

if found_list:# Проверяем: если список found_list не пуста, то
    print("=============== Найдено ===============")# Выводим эту строку
    for i in found_list:# Создаём цикл, который будет пробегаться по этому списку и 
        print(i)# Выводим элементы этого списка
else:# Иначе
    print("=============== Не найдено ===============")# Выводим эту строку


