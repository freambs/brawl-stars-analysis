import json
from collections import defaultdict

with open("type_output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

result = {
    "Treino": defaultdict(lambda: defaultdict(list)),
    "Torneio": defaultdict(lambda: defaultdict(list))
}

for category in ["Treino", "Torneio"]:
    for battle in data[category]:
        event = battle.get("event", {})
        mode = event.get("mode", "UnknownMode")
        map_name = event.get("map", "UnknownMap")

        result[category][mode][map_name].append(battle)

print("Classificação por modo e mapa concluída.")

with open("map_output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)