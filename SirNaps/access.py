import json
from pathlib import Path

file_path = Path("Module5") / "student.json"

with open("student.json", "r", newline="", encoding="utf-8") as file:
    reader = json.load(file)

for i in reader:
    print(i)


