import json

DataPath = { "crops":'./Data/crops.json',
        "events":'./Data/events.json',
        "foods":'./Data/foods.json',
        "ui":'./Data/ui.json' }

def get(name: str):
    with open(DataPath[name], 'r', encoding='utf-8') as file:
        return json.load(file)