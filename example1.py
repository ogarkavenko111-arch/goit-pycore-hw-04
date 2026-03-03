def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            salaries = [int(line.split(",")[1].strip()) for line in f if line.strip()]

        if not salaries:
            return (0, 0)

        total = sum(salaries)
        average = total / len(salaries)
        return total, average

    except FileNotFoundError:
        print("Файл не знайдено!")
        return (0, 0)
    
total, average = total_salary("salary.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")  