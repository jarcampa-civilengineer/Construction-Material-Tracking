import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
MATERIALS_FILE = DATA_DIR / "materials.json"
TRANSACTIONS_FILE = DATA_DIR / "transactions.csv"

def load_materials():
    DATA_DIR.mkdir(exist_ok=True)
    if not MATERIALS_FILE.exists():
        return {}
    with MATERIALS_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

def save_materials(materials):
    DATA_DIR.mkdir(exist_ok=True)
    with MATERIALS_FILE.open("w", encoding="utf-8") as f:
        json.dump(materials, f, indent=2)

def append_transaction(transaction):
    DATA_DIR.mkdir(exist_ok=True)
    exists = TRANSACTIONS_FILE.exists()
    with TRANSACTIONS_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(transaction.keys()))
        if not exists:
            writer.writeheader()
        writer.writerow(transaction)

def load_transactions():
    if not TRANSACTIONS_FILE.exists():
        return []
    with TRANSACTIONS_FILE.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
