import json
import os

filename = "stars.json"
operations_count = 0
stars = []

def load_data():
    """Загрузка данных из файла"""
    global stars
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            stars = json.load(f)
    else:
        stars = [
            {"id": 1, 
             "name": "Сириус", 
             "constellation": "Большой Пес", 
             "is_visible": True, 
             "radius": 1.711},
            {"id": 2, 
             "name": "Канопус", 
             "constellation": "Киль", 
             "is_visible": True, 
             "radius": 71.4},
            {"id": 3, "name": 
             "Арктур", "constellation": 
             "Волопас", 
             "is_visible": True, 
             "radius": 25.4},
            {"id": 4, 
             "name": "Вега", 
             "constellation": "Лира", 
             "is_visible": True, 
             "radius": 2.818},
            {"id": 5, 
             "name": "Капелла", 
             "constellation": "Возничий", 
             "is_visible": True, 
             "radius": 11.98},
        ]
        save_data()

def save_data():
    """Сохранение данных в файл"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(stars, f, ensure_ascii=False, indent=2)

def show_all():
    """Вывод всех записей"""
    print("\n" + "=" * 50)
    print("ВСЕ ЗАПИСИ:")
    print("=" * 50)
    for i, star in enumerate(stars, 1):
        print(f"Запись {i}:")
        print(f"  ID: {star['id']}")
        print(f"  Название: {star['name']}")
        print(f"  Созвездие: {star['constellation']}")
        print(f"  Видима без телескопа: {'Да' if star['is_visible'] else 'Нет'}")
        print(f"  Радиус (солнечных): {star['radius']}")
        print("-" * 30)

def find_by_id():
    """Поиск записи по ID"""
    try:
        search_id = int(input("Введите ID звезды для поиска: "))
        for star in stars:
            if star["id"] == search_id:
                print(f"\nНайдена запись:")
                print(f"  ID: {star['id']}")
                print(f"  Название: {star['name']}")
                print(f"  Созвездие: {star['constellation']}")
                print(f"  Видима без телескопа: {'Да' if star['is_visible'] else 'Нет'}")
                print(f"  Радиус (солнечных): {star['radius']}")
                return
        print("\nЗапись с таким ID не найдена!")
    except ValueError:
        print("\nОшибка: ID должен быть числом!")

def add_star():
    """Добавление новой записи"""
    try:
        new_id = int(input("Введите ID новой звезды: "))
        
        if any(star["id"] == new_id for star in stars):
            print("\nЗапись с таким ID уже существует!")
            return
        
        name = input("Введите название звезды: ").strip()
        if not name:
            print("\nОшибка: название не может быть пустым!")
            return
        
        constellation = input("Введите название созвездия: ").strip()
        if not constellation:
            print("\nОшибка: название созвездия не может быть пустым!")
            return
        
        is_visible_input = input("Видна без телескопа? (да/нет): ").lower()
        is_visible = is_visible_input in ["да", "yes", "y", "1", "true"]
        
        radius = float(input("Введите радиус в солнечных радиусах: "))
        if radius <= 0:
            print("\nОшибка: радиус должен быть положительным числом!")
            return

        new_star = {
            "id": new_id,
            "name": name,
            "constellation": constellation,
            "is_visible": is_visible,
            "radius": radius,
        }
        
        stars.append(new_star)
        save_data()
        print("\nЗапись успешно добавлена!")
        
    except ValueError:
        print("\nОшибка ввода данных! Проверьте корректность введенных значений.")

def delete_star():
    """Удаление записи по ID"""
    try:
        delete_id = int(input("Введите ID звезды для удаления: "))
        
        for i, star in enumerate(stars):
            if star["id"] == delete_id:
                del stars[i]
                save_data()
                print("\nЗапись успешно удалена!")
                return
        
        print("\nЗапись с таким ID не найдена!")
        
    except ValueError:
        print("\nОшибка: ID должен быть числом!")

def show_menu():
    """Отображение меню"""
    print("\n" + "=" * 50)
    print("МЕНЮ:")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю")
    print("3. Добавить запись")
    print("4. Удалить запись по полю")
    print("5. Выйти из программы")
    print("=" * 50)

def main():
    """Основная функция программы"""
    global operations_count
    load_data()
    
    while True:
        show_menu()
        choice = input("Выберите пункт меню (1-5): ")
        
        if choice == "1":
            operations_count += 1
            show_all()
            
        elif choice == "2":
            operations_count += 1
            find_by_id()
            
        elif choice == "3":
            operations_count += 1
            add_star()
            
        elif choice == "4":
            operations_count += 1
            delete_star()
            
        elif choice == "5":
            print(f"\nВсего выполнено операций: {operations_count}")
            print("До свидания!")
            break
            
        else:
            print("\nНеверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main()
