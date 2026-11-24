# Construction Material Tracking

A small command-line application for tracking construction materials, deliveries,
consumption, available quantities, and minimum stock levels.

## Features
- Register materials by code, category, unit, and storage location.
- Record deliveries with delivery ticket or purchase-order references.
- Record material usage by work area or activity.
- Prevent usage entries that exceed the recorded stock balance.
- View current inventory and low-stock alerts.
- Export a timestamped inventory CSV report.
- Persist material balances in JSON and transaction history in CSV.

## Project files
- `main.py` — command-line menu and user interaction.
- `models.py` — material and transaction data structures.
- `validators.py` — required-field and quantity validation.
- `inventory_manager.py` — inventory business logic.
- `storage.py` — local JSON/CSV persistence.
- `report_generator.py` — inventory display and CSV export.

## Requirements
Python 3.9 or newer. Uses only the Python standard library.

## Run
Open a terminal in this folder and execute:

```bash
python main.py
```

The program creates `data/` automatically when materials or transactions are saved.
CSV inventory reports are written to the `reports/` folder.

## Important note
This is a basic material-control and recordkeeping tool. It does not replace
purchase-order approvals, delivery inspections, material certifications,
quantity verification, or the project's approved inventory-control procedures.
