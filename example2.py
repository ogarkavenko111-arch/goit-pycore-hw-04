def get_cats_info(path):
    cats_list = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()  # прибираємо пробіли та символи нового рядка
                if not line:
                    continue  # пропускаємо порожні рядки
                parts = line.split(",")
                if len(parts) != 3:
                    print(f"Попередження: рядок некоректний -> {line}")
                    continue
                cat_id, name, age_str = parts
                try:
                    age = int(age_str)  # перетворюємо вік у число
                except ValueError:
                    print(f"Попередження: вік некоректний -> {age_str} у рядку {line}")
                    continue
                cats_list.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Помилка: файл за шляхом '{path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    return cats_list

# Приклад використання

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
