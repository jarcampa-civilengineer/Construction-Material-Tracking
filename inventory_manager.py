from models import Material, Transaction
from validators import required, positive_number
import storage

class InventoryManager:
    def __init__(self):
        self.materials = storage.load_materials()

    def add_material(self, data):
        code = required(data["code"], "Material code").upper()
        if code in self.materials:
            raise ValueError(f"Material code {code} already exists.")
        material = Material(
            code=code,
            name=required(data["name"], "Material name"),
            category=required(data["category"], "Category"),
            unit=required(data["unit"], "Unit"),
            minimum=positive_number(data["minimum"], "Minimum stock", allow_zero=True),
            location=required(data["location"], "Storage location"),
        )
        self.materials[code] = material.to_dict()
        storage.save_materials(self.materials)

    def _get_material(self, code):
        code = required(code, "Material code").upper()
        if code not in self.materials:
            raise KeyError(f"Material code {code} was not found.")
        return self.materials[code]

    def receive(self, code, quantity, reference="N/A", notes=""):
        material = self._get_material(code)
        qty = positive_number(quantity, "Received quantity")
        material["quantity"] = float(material["quantity"]) + qty
        storage.save_materials(self.materials)
        tx = Transaction.create(code.upper(), material["name"], "RECEIVED", qty,
                                material["unit"], reference, notes)
        storage.append_transaction(tx.to_dict())

    def use(self, code, quantity, work_area, reference="N/A"):
        material = self._get_material(code)
        qty = positive_number(quantity, "Used quantity")
        available = float(material["quantity"])
        if qty > available:
            raise ValueError(f"Insufficient stock. Available: {available:g} {material['unit']}.")
        material["quantity"] = available - qty
        storage.save_materials(self.materials)
        tx = Transaction.create(code.upper(), material["name"], "USED", qty,
                                material["unit"], reference, work_area)
        storage.append_transaction(tx.to_dict())

    def low_stock(self):
        return [
            item for item in self.materials.values()
            if float(item["quantity"]) <= float(item["minimum"])
        ]
