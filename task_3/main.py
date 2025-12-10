[# добавить в файл json
    {"id" : 1, "name" : "Солнце", "constellation " : "нет", "is_visible " : "True", "radius " : 1.0},
    {"id" : 2, "name" : "Сириус", "constellation " : "Большой Пес", "is_visible " : "True", "radius " : 1.7},
    {"id" : 3, "name" : "Арктур", "constellation " : "Волопас", "is_visible " : "True", "radius " : 25.7},
    {"id" : 4, "name" : "Вега", "constellation " : "Лира", "is_visible " : "True", "radius " : 2.7},
    {"id" : 5, "name" : "Альтаир", "constellation " : "Орел", "is_visible " : "True", "radius " : 1.6}
]



import json# Добавляем библиотеку json

file_name = "List.json"# Создаём переменную file_name и присвайваем ей название json файла
operations_count = 0# Создаём переменную operations_count для подсчёта количества выполненных команд

try:# Пробуем
    with open(file_name, 'r', encoding = 'utf - 8') as File:# Открыть файл file_name на чтение
        data = json.load(File)# Переменной data присвайваем содержимое файла file_name
except FileNotFoundError:# Проверяем на ошибку FileNotFoundError
    print(f"Файл {file_name} не найден!!!!!")# Если она есть, то выводим этот текст
except Exception as e:# Проверяем на ошибку Exception e
    print(f"Произошла ошибка: {e}")# Если она есть, то выводим этот текст

while True:
    print("\nМеню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю (id)")
    print("3. Добавить запись")
    print("4. Удалить запись по полю (id)")
    print("5. Выйти из программы")

    choice = int(input("Выберите пункт меню (1-5): "))

    if choice == 1:
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("\nВсе записи:")
        for record in data:
            print(f"ID: {f['id']}, Название: {f['name']}, Созвездие: {f['constellation']}, Видима: {f['is_visible']}, Радиус (солн.): {f['radius']}")
        operations_count += 1

    elif choice == 2:
        id_str = input("Введите ID записи для поиска: ")
        try:
            id = int(id_str)
            with open(file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
            found  = False
            for index, record in enumerate(data):
                if record['id'] == id:
                    print(f"\nНайдена запись (позиция в списке: {index}):")
                    print(f"ID: {f['id']}, Название: {f['name']}, Созвездие: {f['constellation']}, Видима: {f['is_visible']}, Радиус (солн.): {f['radius']}")
                    found = True
                    break
            if not found:
                print(f"Предупреждение: Запись с ID {id} не найдена.")

            operations_count += 1

        except ValueError:
            print("Ошибка: ID должен быть целым числом.")



---------------------------------------------------------------------------------------------------------------



elif choice == '3':
        # Пункт "Добавить запись"
        try:
            new_id = int(input("Введите ID новой записи (целое число): "))
            new_name = input("Введите название звезды: ")
            new_constellation = input("Введите название созвездия: ")
            new_is_visible_str = input("Видима без телескопа? (True/False): ")
            new_is_visible = new_is_visible_str.lower() == 'true'
            new_radius = float(input("Введите радиус звезды (солнечный радиус): "))

            new_record = {
                "id": new_id,
                "name": new_name,
                "constellation": new_constellation,
                "is_visible": new_is_visible,
                "radius": new_radius
            }
            
            with open(FILE_NAME, 'r', encoding='utf-8') as f:
                data = json.load(f)
            data.append(new_record)

            with open(FILE_NAME, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Запись с ID {new_id} добавлена.")
            operations_count += 1
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    elif choice == '4':
        # Пункт "Удалить запись по полю (id)"
        record_id_str = input("Введите ID записи для удаления: ")
        try:
            record_id = int(record_id_str)
            with open(FILE_NAME, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            initial_len = len(data)
            data = [record for record in data if record['id'] != record_id]
            
            if len(data) < initial_len:
                with open(FILE_NAME, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                print(f"Запись с ID {record_id} удалена.")
                operations_count += 1
            else:
                print(f"Предупреждение: Запись с ID {record_id} не найдена.")

        except ValueError:
            print("Ошибка: ID должен быть целым числом.")

    elif choice == '5':
        # Пункт "Выйти из программы"
        print(f"Количество выполненных операций с записями: {operations_count}")
        break
    
    else:
        print("Неверный ввод, пожалуйста, выберите пункт от 1 до 5.")
