from pathlib import Path
from colorama import init, Fore
import sys

init(autoreset=True)

def show_directory_structure(path, indent=""):
    for item in path.iterdir():
        if item.is_dir():
            print(indent + Fore.BLUE + item.name)
            show_directory_structure(item, indent + "    ")
        else:
            print(indent + Fore.GREEN + item.name)

def main():
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: вкажіть шлях до директорії.")
        return

    path = Path(sys.argv[1])
    if not path.exists():
        print(Fore.RED + "Помилка: шлях не існує.")
        return
    if not path.is_dir():
        print(Fore.RED + "Помилка: це не директорія.")
        return

    # Додано вивід верхньої папки
    print(Fore.YELLOW + path.name)
    show_directory_structure(path)

if __name__ == "__main__":
    main()