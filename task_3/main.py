import json



    choice = int(input("Выберите пункт меню (1-5): "))

    if choice == 1:
        with open(file_name, 'r', encoding = 'utf - 8') as f:
            data = json.load(f)
        print("\nВсе записи:")
        for record in data:
            print(f"ID: {record['id']}, Название: {record['name']}, Созвездие: {record['constellation']}, Видима: {record['is_visible']}, Радиус (солн.): {record['radius']}")
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
                    print(f"ID: {record['id']}, Название: {record['name']}, Созвездие: {record['constellation']}, Видима: {record['is_visible']}, Радиус (солн.): {record['radius']}")
                    found = True
                    break
            if not found:
                print(f"Предупреждение: Запись с ID {id} не найдена.")

            operations_count += 1

        except ValueError:
            print("Ошибка: ID должен быть целым числом.")

    elif choice == 3:
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
            
            with open(file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
            data.append(new_record)

            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Запись с ID {new_id} добавлена.")
            operations_count += 1
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")

    elif choice == '4':
        record_id_str = input("Введите ID записи для удаления: ")
        try:
            record_id = int(record_id_str)
            with open(file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            initial_len = len(data)
            data = [record for record in data if record['id'] != record_id]
            
            if len(data) < initial_len:
                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                print(f"Запись с ID {record_id} удалена.")
                operations_count += 1
            else:
                print(f"Предупреждение: Запись с ID {record_id} не найдена.")

        except ValueError:
            print("Ошибка: ID должен быть целым числом.")

    elif choice == '5':
        print(f"Количество выполненных операций с записями: {operations_count}")
        break
    
    else:
        print("Неверный ввод, пожалуйста, выберите пункт от 1 до 5.")



