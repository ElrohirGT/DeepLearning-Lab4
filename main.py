import json

with open("lab4.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)
    for cell in nb.get("cells", []):
        if "widgets" in cell.get("metadata", {}):
            del cell["metadata"]["widgets"]

with open("final.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f)