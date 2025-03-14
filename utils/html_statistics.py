def generate_html_statistics(statistics):
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
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            background: #1c1c1c;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
            width: 90%;
            max-width: 800px;
            animation: fadeIn 1.5s ease-in-out;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(-20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
            background-color: #222;
            border-radius: 10px;
            overflow: hidden;
        }}
        th, td {{
            border: 1px solid #444;
            padding: 12px;
            text-align: center;
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
        #asciiArt {{
            font-family: monospace;
            white-space: pre;
            color: #FFD700;
            position: fixed;
            top: 10px;
            right: 10px;
            opacity: 0.7;
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
        <h1 class="header">Data Summary</h1>
        <p>Мы обработали полученные фигуры и подвели статистику</p>
        <table>
            <tr>
                <th>Parameter</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>Average Diagonal</td>
                <td>{statistics['avg_diag']}</td>
            </tr>
            <tr>
                <td>Average Volume</td>
                <td>{statistics['avg_volume']}</td>
            </tr>
            <tr>
                <td>Average Surface Area</td>
                <td>{statistics['avg_surface_area']}</td>
            </tr>
            <tr>
                <td>Average Alpha</td>
                <td>{statistics['avg_alpha']}</td>
            </tr>
            <tr>
                <td>Average Beta</td>
                <td>{statistics['avg_beta']}</td>
            </tr>
            <tr>
                <td>Average Gamma</td>
                <td>{statistics['avg_gamma']}</td>
            </tr>
            <tr>
                <td>Average Radius of Described Sphere</td>
                <td>{statistics['avg_radius_described_sphere']}</td>
            </tr>
            <tr>
                <td>Average Volume of Described Sphere</td>
                <td>{statistics['avg_volume_described_sphere']}</td>
            </tr>
        </table>
    </div>
    <div id="asciiArt"></div>
    <footer>
        Developed with ❤️ by Your Name
    </footer>
    <script>
        const asciiArt = [
            'MY FIRST SKRIPT\\n\\n',
            '    *********',
            '   *       **',
            '  *       * *',
            ' *********  *',
            ' *       *  *',
            ' *       *  *',
            ' *       * *',
            ' *********',
            '\\n\\nI LOVE PYTHON'
        ];
        let artIndex = 0;
        function displayArt() {{
            if (artIndex < asciiArt.length) {{
                document.getElementById('asciiArt').innerText += asciiArt[artIndex] + '\\n';
                artIndex++;
                setTimeout(displayArt, 400);
            }}
        }}
        displayArt();
    </script>
</body>
</html>
    """

    try:
        with open("html_files/data_statistics.html", "w", encoding="utf-8") as file:
            file.write(html_content)
        print("Файл data_statistics.html успешно создан.")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")


