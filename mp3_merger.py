# code
from pydub import AudioSegment
import os

# Путь к директории с MP3-файлами
directory = "/home/tier/Music/abooks/dombrovsky/fakultet_po_glavam/1"  # Замените на путь к вашей папке

# Создание пустого аудиосегмента
combined = AudioSegment.empty()

# Сортировка файлов по имени для последовательного объединения
file_list = sorted(os.listdir(directory))

# Объединение файлов
print(file_list)

for file in file_list:
    if file.endswith(".mp3"):
        path = os.path.join(directory, file)
        audio = AudioSegment.from_mp3(path)
        combined += audio


# Экспорт объединенного файла
out_path = "/home/tier/Music/abooks/dombrovsky/fakultet_po_glavam/combined_file_1.mp3"
combined.export(out_path, format="mp3")
print(f"work is over, result is here: {out_path}")