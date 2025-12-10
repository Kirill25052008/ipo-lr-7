import json

file_name = "dump.json"

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"Файл {file_name} не найден!!!!!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

qualification_input = input("Введите номер квалификации: ")

found_list = []

for item in data:
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
