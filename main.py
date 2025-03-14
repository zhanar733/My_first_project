import json
from utils.data_loader import load_parallelepipeds
from utils.data_processor import calculate_characteristics
from utils.statistics_calculator import calculate_statistics
from utils.characteristics_html import generate_html_characteristics
from utils.html_statistics import generate_html_statistics
import os

os.makedirs("html_files", exist_ok=True)  # Создаст папку, если её нет


# Загрузка данных
parallelepipeds = load_parallelepipeds(
    "/root/My_first_project/json_files/parallelepipeds.json"
)

# Вычисление характеристик
characteristics = calculate_characteristics(parallelepipeds)

# Сохранение характеристик в файл
try:
    with open("json_files/characteristics.json", "w") as file:
        json.dump(characteristics, file, indent=4)
    print("Файл characteristics.json успешно создан.")
except Exception as e:
    print(f"Ошибка при создании файла: {e}")

# Вычисление статистики
statistics = calculate_statistics(characteristics)

# Сохранение статистики в файл
try:
    with open("json_files/statistics.json", "w") as file:
        json.dump(statistics, file, indent=4)
    print("Файл cstatistics.json успешно создан.")
except Exception as e:
    print(f"Ошибка при создании файла: {e}")

generate_html_characteristics(parallelepipeds, characteristics)


generate_html_statistics(statistics)
