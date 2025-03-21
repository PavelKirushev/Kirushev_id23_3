import os
import shutil

def main():
    work_dir = os.path.abspath("file_manager_workspace")
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)

    current_dir = work_dir

    while True:
        try:
            print(f"Текущая папка: {os.path.relpath(current_dir, work_dir) or '/'}")
            print("1. Создать папку\n2. Удалить папку\n3. Перейти в папку\n4. Выйти вверх")
            print("5. Создать файл\n6. Записать в файл\n7. Просмотреть файл\n8. Удалить файл")
            print("9. Копировать файл\n10. Переместить файл\n11. Переименовать файл\n12. Выход")
            choice = input("Выберите действие: ")

            if choice == '1':
                name = input("Введите имя папки: ")
                create_folder(current_dir, name)
            elif choice == '2':
                name = input("Введите имя папки: ")
                delete_folder(current_dir, name)
            elif choice == '3':
                name = input("Введите имя папки: ")
                new_dir = os.path.join(current_dir, name)
                if is_valid_path(new_dir, work_dir):
                    if os.path.isdir(new_dir):
                        current_dir = new_dir
                    else:
                        print("Ошибка: Это не папка!")
                else:
                    print("Ошибка: Недопустимый путь!")
            elif choice == '4':
                parent_dir = os.path.dirname(current_dir)
                if is_valid_path(parent_dir, work_dir):
                    current_dir = parent_dir
                else:
                    print("Ошибка: Невозможно выйти за пределы рабочей директории!")
            elif choice == '5':
                name = input("Введите имя файла: ")
                create_file(current_dir, name)
            elif choice == '6':
                name = input("Введите имя файла: ")
                write_to_file(current_dir, name)
            elif choice == '7':
                name = input("Введите имя файла: ")
                view_file(current_dir, name)
            elif choice == '8':
                name = input("Введите имя файла: ")
                delete_file(current_dir, name)
            elif choice == '9':
                src_name = input("Введите имя файла для копирования: ")
                dst_name = input("Введите имя файла для сохранения: ")
                copy_file(current_dir, src_name, dst_name)
            elif choice == '10':
                src_name = input("Введите имя файла для перемещения: ")
                dst_name = input("Введите имя файла для сохранения: ")
                move_file(current_dir, src_name, dst_name)
            elif choice == '11':
                old_name = input("Введите текущее имя файла: ")
                new_name = input("Введите новое имя файла: ")
                rename_file(current_dir, old_name, new_name)
            elif choice == '12':
                print("Выход из программы.")
                break
            else:
                print("Недопустимый выбор. Пожалуйста, выберите действие из списка.")
        except Exception as e:
            print(f"Ошибка: {str(e)}")


def is_valid_path(path: str, work_dir: str) -> bool:
    return os.path.commonpath([work_dir]) == os.path.commonpath([work_dir, path])

def create_folder(current_dir: str, name: str):
    path = os.path.join(current_dir, name)
    if os.path.exists(path):
        raise Exception("Папка уже существует")
    os.mkdir(path)
    print(f"Папка '{name}' создана")

def delete_folder(current_dir: str, name: str):
    path = os.path.join(current_dir, name)
    if not os.path.exists(path):
        raise Exception("Папка не существует")
    if not os.path.isdir(path):
        raise Exception("Это не папка")
    if os.listdir(path):
        raise Exception("Папка не пуста")
    os.rmdir(path)
    print(f"Папка '{name}' удалена")


def create_file(current_dir: str, name: str):
    path = os.path.join(current_dir, name)
    if os.path.exists(path):
        raise Exception("Файл уже существует")
    open(path, 'w').close()
    print(f"Файл '{name}' создан")


def write_to_file(current_dir: str, name: str):
    path = os.path.join(current_dir, name)
    if not os.path.exists(path):
        raise Exception("Файл не существует")
    if not os.path.isfile(path):
        raise Exception("Это не файл")
    text = input("Введите текст для записи: ")
    with open(path, 'w') as file:
        file.write(text)
    print(f"Текст записан в файл '{name}'")


def view_file(current_dir: str, name: str):
    path = os.path.join(current_dir, name)
    if not os.path.exists(path):
        raise Exception("Файл не существует")
    if not os.path.isfile(path):
        raise Exception("Это не файл")
    with open(path, 'r') as file:
        content = file.read()
        print(f"Содержимое файла '{name}':\n{content}")


def delete_file(current_dir: str, name: str):
    path = os.path.join(current_dir, name)
    if not os.path.exists(path):
        raise Exception("Файл не существует")
    if not os.path.isfile(path):
        raise Exception("Это не файл")
    os.remove(path)
    print(f"Файл '{name}' удален")


def copy_file(current_dir: str, src_name: str, dst_name: str):
    src_path = os.path.join(current_dir, src_name)
    dst_path = os.path.join(current_dir, dst_name)
    if not os.path.exists(src_path):
        raise Exception("Исходный файл не существует")
    if not os.path.isfile(src_path):
        raise Exception("Исходный файл не является файлом")
    if os.path.exists(dst_path):
        raise Exception("Файл с таким именем уже существует")
    shutil.copy(src_path, dst_path)
    print(f"Файл '{src_name}' скопирован в '{dst_name}'")


def move_file(current_dir: str, src_name: str, dst_name: str):
    src_path = os.path.join(current_dir, src_name)
    dst_path = os.path.join(current_dir, dst_name)
    if not os.path.exists(src_path):
        raise Exception("Исходный файл не существует")
    if not os.path.isfile(src_path):
        raise Exception("Исходный файл не является файлом")
    if os.path.exists(dst_path):
        raise Exception("Файл с таким именем уже существует")
    shutil.move(src_path, dst_path)
    print(f"Файл '{src_name}' перемещен в '{dst_name}'")


def rename_file(current_dir: str, old_name: str, new_name: str):
    old_path = os.path.join(current_dir, old_name)
    new_path = os.path.join(current_dir, new_name)
    if not os.path.exists(old_path):
        raise Exception("Файл не существует")
    if not os.path.isfile(old_path):
        raise Exception("Это не файл")
    if os.path.exists(new_path):
        raise Exception("Файл с таким именем уже существует")
    os.rename(old_path, new_path)
    print(f"Файл '{old_name}' переименован в '{new_name}'")


if __name__ == "__main__":
    main()
