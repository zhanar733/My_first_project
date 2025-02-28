import os


def generate_html_characteristics(parallelepipeds, characteristics):
    """
    Генерирует HTML-файл на основе данных о параллелепипедах и их характеристиках.
    Объединяет данные в одну таблицу по имени фигуры.

    :param parallelepipeds: Словарь с данными о параллелепипедах.
    :param characteristics: Словарь с характеристиками параллелепипедов.
    :return: None
    """
    # Создаем строки для объединенной таблицы
    combined_rows = ""
    for figure_name in parallelepipeds.keys():
        # Данные о параллелепипеде
        figure_data = parallelepipeds.get(figure_name, {})
        a = figure_data.get("a", "N/A")
        b = figure_data.get("b", "N/A")
        c = figure_data.get("c", "N/A")

        # Данные о характеристиках
        char_data = characteristics.get(figure_name, {})
        diag = char_data.get("diag", "N/A")
        volume = char_data.get("volume", "N/A")
        surface_area = char_data.get("surface_area", "N/A")
        alpha = char_data.get("alpha", "N/A")
        beta = char_data.get("beta", "N/A")
        gamma = char_data.get("gamma", "N/A")
        radius_described_sphere = char_data.get("radius_described_sphere", "N/A")
        volume_described_sphere = char_data.get("volume_described_sphere", "N/A")

        # Добавляем строку в таблицу
        combined_rows += f"""
        <tr>
            <td>{figure_name}</td>
            <td>{a}</td>
            <td>{b}</td>
            <td>{c}</td>
            <td>{diag}</td>
            <td>{volume}</td>
            <td>{surface_area}</td>
            <td>{alpha}</td>
            <td>{beta}</td>
            <td>{gamma}</td>
            <td>{radius_described_sphere}</td>
            <td>{volume_described_sphere}</td>
        </tr>
        """

    # HTML-шаблон
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Summary</title>
    <style>
        body {{
            background-color: #000000;
            color: #FFFFFF;
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: 0;
            padding: 20px;
        }}

        .container {{
            background: #1c1c1c;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            animation: fadeIn 1.5s ease-in-out;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(-20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .table-container {{
            overflow-x: auto;
            width: 100%;
            margin-top: 20px;
        }}

        table {{
            border-collapse: collapse;
            width: 100%;
            background-color: #222;
            border-radius: 10px;
            overflow: hidden;
        }}

        th, td {{
            border: 1px solid #444;
            padding: 12px;
            text-align: center;
            white-space: nowrap;
        }}

        th {{
            background-color: #333;
            font-weight: bold;
        }}

        td {{
            background-color: #2a2a2a;
        }}

        h1, p {{
            margin: 10px;
            text-align: center;
        }}

        .header {{
            color: #FFD700;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}

        footer {{
            margin-top: 30px;
            text-align: center;
            font-size: 0.9em;
            color: #888;
        }}

        @media (max-width: 600px) {{
            .container {{
                width: 100%;
                padding: 10px;
            }}
            th, td {{
                padding: 8px;
            }}
            .header {{
                font-size: 2em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1 class="header">Data characteristics paralipipeds</h1>
        <p>Мы обработали полученные фигуры</p>

        <h2>Объединенные данные</h2>
        <div class="table-container">
            <table>
                <tr>
                    <th>Название</th>
                    <th>A</th>
                    <th>B</th>
                    <th>C</th>
                    <th>Диагональ</th>
                    <th>Объем</th>
                    <th>Площадь поверхности</th>
                    <th>Угол Alpha</th>
                    <th>Угол Beta</th>
                    <th>Угол Gamma</th>
                    <th>Радиус сферы</th>
                    <th>Объем сферы</th>
                </tr>
                {combined_rows}
            </table>
        </div>
    </div>
    <footer>
        Developed with ❤️ by Your Name
    </footer>
</body>
</html>
    """

    # Сохраняем HTML-файл
    try:
        with open(
            "html_files/characteristics_paralipipeds.html", "w", encoding="utf-8"
        ) as file:
            file.write(html_content)
        print("Файл data_summary_1.html успешно создан.")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")
