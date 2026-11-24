import csv
from pathlib import Path
from datetime import datetime

class ReportGenerator:
    def __init__(self, manager):
        self.manager = manager

    def print_inventory(self):
        if not self.manager.materials:
            print("No materials have been registered.")
            return
        print("\nCODE | MATERIAL | CATEGORY | ON HAND | UNIT | MINIMUM | LOCATION")
        print("-" * 88)
        for item in self.manager.materials.values():
            print(f"{item['code']} | {item['name']} | {item['category']} | "
                  f"{float(item['quantity']):g} | {item['unit']} | "
                  f"{float(item['minimum']):g} | {item['location']}")

    def print_low_stock(self):
        items = self.manager.low_stock()
        if not items:
            print("No materials are currently at or below their minimum stock level.")
            return
        print("\nLOW-STOCK MATERIALS")
        for item in items:
            print(f"- {item['name']} ({item['code']}): {item['quantity']} "
                  f"{item['unit']} on hand; minimum {item['minimum']}")

    def export(self):
        output_dir = Path(__file__).parent / "reports"
        output_dir.mkdir(exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = output_dir / f"inventory_report_{stamp}.csv"
        fields = ["code", "name", "category", "quantity", "unit", "minimum", "location"]
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for item in self.manager.materials.values():
                writer.writerow({key: item[key] for key in fields})
        return path
