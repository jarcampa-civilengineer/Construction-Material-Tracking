from inventory_manager import InventoryManager
from report_generator import ReportGenerator

def ask(prompt, default=""):
    value = input(f"{prompt}" + (f" [{default}]" if default else "") + ": ").strip()
    return value or default

def main():
    manager = InventoryManager()
    reports = ReportGenerator(manager)

    while True:
        print("\n=== CONSTRUCTION MATERIAL TRACKING ===")
        print("1. Add material")
        print("2. Record material received")
        print("3. Record material used")
        print("4. View inventory")
        print("5. View low-stock materials")
        print("6. Export inventory report")
        print("7. Exit")
        choice = input("Select an option: ").strip()

        try:
            if choice == "1":
                item = {
                    "code": ask("Material code"),
                    "name": ask("Material name"),
                    "category": ask("Category (concrete, masonry, steel, etc.)"),
                    "unit": ask("Unit (yd3, ton, bag, piece, ft, etc.)"),
                    "minimum": ask("Minimum stock level", "0"),
                    "location": ask("Storage location", "Main yard"),
                }
                manager.add_material(item)
                print("Material added.")
            elif choice == "2":
                code = ask("Material code")
                qty = ask("Quantity received")
                reference = ask("Delivery ticket / PO number", "N/A")
                notes = ask("Notes")
                manager.receive(code, qty, reference, notes)
                print("Receipt recorded.")
            elif choice == "3":
                code = ask("Material code")
                qty = ask("Quantity used")
                work_area = ask("Work area / activity")
                reference = ask("Work order / placement reference", "N/A")
                manager.use(code, qty, work_area, reference)
                print("Material usage recorded.")
            elif choice == "4":
                reports.print_inventory()
            elif choice == "5":
                reports.print_low_stock()
            elif choice == "6":
                path = reports.export()
                print(f"Reports exported to: {path}")
            elif choice == "7":
                print("Goodbye.")
                break
            else:
                print("Please select a valid option.")
        except (ValueError, KeyError) as exc:
            print(f"Error: {exc}")

if __name__ == "__main__":
    main()
