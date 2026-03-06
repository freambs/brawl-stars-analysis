import json
from collections import Counter

with open("all_battles_clean.json", "r", encoding="utf-8") as f:
    battles = json.load(f)

types_counter = Counter()

for battle in battles:
    battle_info = battle.get("battle", {})
    battle_type = battle_info.get("type", "unknown")
    types_counter[battle_type] += 1

print("Distribuição por tipo de partida:")
for t, count in types_counter.items():
    print(f"{t}: {count}")