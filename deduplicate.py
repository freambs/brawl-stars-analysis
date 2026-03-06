import json

with open("all_battles_raw.json", "r", encoding="utf-8") as f:
    battles = json.load(f)

unique_battles = {}

for battle in battles:
    battle_time = battle.get("battleTime")

    event = battle.get("event")
    if not event:
        continue

    mode = event.get("mode")
    map_name = event.get("map")

    if not battle_time or not mode or not map_name:
        continue

    battle_id = f"{battle_time}{mode}{map_name}"
    unique_battles[battle_id] = battle

print("Partidas brutas:", len(battles))
print("Partidas únicas:", len(unique_battles))

with open("all_battles_clean.json", "w", encoding="utf-8") as f:
    json.dump(list(unique_battles.values()), f, indent=2, ensure_ascii=False)

print("Arquivo all_battles_clean.json salvo com sucesso.")