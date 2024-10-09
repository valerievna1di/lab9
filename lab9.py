def create_file(filename):
    try:
        # Створення файлу та запис рядків різної довжини
        with open(filename, 'w') as file:
            file.write("Це перший рядок\n")
            file.write("Рядок з цифрами: 101010\n")
            file.write("Ще один рядок з цифрами: 111000\n")
        print(f"Файл {filename} успішно створено.")
    except Exception as e:
        print(f"Помилка при створенні файлу {filename}: {e}")

def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Заміна символів нового рядка (\n) на пробіли
        content = content.replace('\n', '_')

        # Замінюємо символи "1" на "0" і навпаки
        new_content = content.replace('1', 'x').replace('0', '1').replace('x', '0')

        # Видаляємо зайві пробіли між словами, щоб не було зайвих перед новими рядками
        new_content = new_content.strip()

        # Записуємо новий вміст у файл по 15 символів на рядок
        with open(output_file, 'w') as outfile:
            for i in range(0, len(new_content), 15):
                # Вставляємо саме стільки символів, скільки є, не додаючи зайвих пробілів
                outfile.write(new_content[i:i+15] + '\n')

        print(f"\nФайл {output_file} успішно створено після обробки.")
    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено.")
    except Exception as e:
        print(f"Помилка під час обробки файлу {input_file}: {e}")

def read_and_print_file(filename):
    try:
        with open(filename, 'r') as file:
            print(f"\nВміст файлу {filename}:\n")
            for line in file:
                print(line.strip())  # Виводимо кожен рядок без зайвих переносів
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    except Exception as e:
        print(f"Помилка під час читання файлу {filename}: {e}")

# Головна програма
if __name__ == "__main__":
    # Крок а) Створення файлу TF23_1
    create_file("TF23_1.txt")

    # Виведення вмісту файлу TF23_1
    read_and_print_file("TF23_1.txt")

    # Крок б) Обробка файлу TF23_1 і запис у TF23_2
    process_file("TF23_1.txt", "TF23_2.txt")

    # Крок в) Читання і виведення вмісту файлу TF23_2
    read_and_print_file("TF23_2.txt")
