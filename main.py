import sys
from pathlib import Path
from pdf2image import convert_from_path

def process_books(directory_name='books'):
    # Создаем объект пути
    base_dir = Path(directory_name)

    # Проверка существования папки
    if not base_dir.exists():
        print(f"Ошибка: Папка '{directory_name}' не найдена.")
        return

    print(f"Начинаю обработку файлов в папке: {base_dir.absolute()}")

    # Ищем все файлы .pdf в папке
    pdf_files = list(base_dir.glob('*.pdf'))

    if not pdf_files:
        print("PDF файлы в папке не найдены.")
        return

    for pdf_file in pdf_files:
        try:
            print(f"Обработка: {pdf_file.name}...")

            # Конвертируем ТОЛЬКО первую страницу (first_page=1, last_page=1) для экономии памяти
            # Если вы на Windows и не добавили Poppler в PATH, раскомментируйте строку ниже и укажите путь:
            # poppler_path = r'C:\Program Files\poppler-xx\bin'
            
            pages = convert_from_path(
                pdf_file, 
                first_page=1, 
                last_page=1,
                # poppler_path=poppler_path  # Добавьте этот аргумент, если нужно
            )

            if pages:
                # Берем первую (и единственную) страницу из списка
                cover_image = pages[0]

                # Формируем имя выходного файла: меняем расширение .pdf на .jpg
                output_filename = pdf_file.with_suffix('.jpg')

                # Сохраняем изображение
                cover_image.save(output_filename, 'JPEG')
                print(f"✔ Сохранено: {output_filename.name}")
            
        except Exception as e:
            print(f"✖ Ошибка при обработке {pdf_file.name}: {e}")

    print("\nГотово!")

if __name__ == '__main__':
    process_books()