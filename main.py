import json
from data_loader import load_parallelepipeds
from data_processor import calculate_characteristics
from statistics_calculator import calculate_statistics
from characteristics_html import generate_html_characteristics
from html_statistics import generate_html_statistics
import os

os.makedirs("html_files", exist_ok=True)  # Создаст папку, если её нет


# Загрузка данных
parallelepipeds = load_parallelepipeds(
    "/root/My_first_project/json_files/parallelepipeds.json"
)

# Вычисление характеристик
characteristics = calculate_characteristics(parallelepipeds)

# Сохранение характеристик в файл
with open("json_files/characteristics.json", "w") as file:
    json.dump(characteristics, file, indent=4)

# Вычисление статистики
statistics = calculate_statistics(characteristics)

# Сохранение статистики в файл
with open("json_files/statistics.json", "w") as file:
    json.dump(statistics, file, indent=4)

generate_html_characteristics(parallelepipeds, characteristics)


generate_html_statistics(statistics)
