from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Material:
    code: str
    name: str
    category: str
    unit: str
    minimum: float
    location: str
    quantity: float = 0.0

    def to_dict(self):
        return asdict(self)

@dataclass
class Transaction:
    timestamp: str
    code: str
    material_name: str
    transaction_type: str
    quantity: float
    unit: str
    reference: str
    details: str = ""

    @classmethod
    def create(cls, code, material_name, transaction_type, quantity, unit, reference, details=""):
        return cls(
            datetime.now().isoformat(timespec="seconds"),
            code, material_name, transaction_type, quantity, unit, reference, details
        )

    def to_dict(self):
        return asdict(self)
