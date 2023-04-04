"""
4. Дан json файл. Найдите в нём все поля "updated" и поменяйте значение на текущие дату и время в формате ISO 8601.
"""

import json
import datetime

def update_json(json_data):
    for key in json_data:
        if isinstance(json_data[key], dict):
            update_json(json_data[key])
        elif key == 'updated':
            json_data[key] = datetime.now().isoformat()
        return json_data

with open('data.json', 'r') as f:
    data = json.load(f)

updated_data = update_json(data)

with open('data_updated.json', 'w') as f:
    json.dump(updated_data, f, indent = 4)
