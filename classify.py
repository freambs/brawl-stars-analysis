import json

with open("all_battles_clean.json", "r", encoding="utf-8") as f:
    battles = json.load(f)

organized = {
    "Treino": [],
    "Torneio": []
}

for battle in battles:
    battle_info = battle.get("battle", {})
    battle_type = battle_info.get("type", "")

    if battle_type == "friendly":
        organized["Treino"].append(battle)

    elif battle_type == "tournament":
        organized["Torneio"].append(battle)

print("Treinos:", len(organized["Treino"]))
print("Torneios:", len(organized["Torneio"]))

with open("type_output.json", "w", encoding="utf-8") as f:
    json.dump(organized, f, indent=2, ensure_ascii=False)

print("Arquivo type_output.json salvo.")