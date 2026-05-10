# MedStore — Simple CLI Medicine Store (University Coursework)

## Overview

MedStore is a minimal command-line interface (CLI) application for managing a small medicine inventory. It was developed as university coursework and is not intended to be a full-fledged, production-grade system. The program demonstrates basic file-based inventory management with simple sale and restock operations.

## Important Notice

- **Academic project**: This repository contains a student assignment implemented for learning purposes only. Do not treat this as production software.
- **Minimal features**: The app is a CLI prototype with limited error handling, no authentication, and plain-text storage.

## Features

- View current inventory
- Process a sale (decrease stock)
- Restock items (increase stock)
- Save changes back to a plain text inventory file

## Files

- [main.py](main.py): Program entry point; shows the menu and orchestrates actions.
- [operations.py](operations.py): Core business logic for sales, restocking, and displaying inventory.
- [read_file.py](read_file.py): Utility to load inventory from `medicines.txt`.
- [write_file.py](write_file.py): Utility to save inventory back to `medicines.txt`.
- [medicines.txt](medicines.txt): Plain-text inventory data used by the app.
- [invoices/](invoices/): Output folder where sale invoices are saved (if the app generates them).

If you want to inspect the code paths, start with [main.py](main.py) which uses `read_file` to load inventory and `operations` to mutate it.

## Requirements

- Python 3.8 or newer (3.10+ recommended)
- No third-party packages required — pure Python and file I/O

## Setup & Run

1. Create and activate a virtual environment (optional but recommended):

   PowerShell:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   Command Prompt:

   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

2. Run the application:

```powershell
python main.py
```

3. Follow the on-screen menu. The main menu provides the following options:

- `1. Sale` — Process a sale and update inventory.
- `2. Restock` — Add stock to existing items.
- `3. View Stock` — Display current inventory to the console.
- `4. Exit` — Save inventory and quit.

All changes are written back to `medicines.txt` by `write_file.py` when sale/restock actions are performed or when exiting.

## Example

Run `python main.py`, choose `3` to view stock, then `1` to make a sale. After a sale, the inventory file is updated and an invoice (if implemented) may be saved under `invoices/`.

## Limitations

- Not secure: no input sanitation beyond basic checks and no access controls.
- Single-user, single-process design — not safe for concurrent access.
- Plain-text storage; no backup or transaction safety.
- Minimal validation — intended for demonstration only.

## Testing

There are no automated tests included. To manually test, run the program and exercise the menu options while observing changes in `medicines.txt` and any files created under `invoices/`.

## Extending this project

Possible improvements if you want to extend the coursework:

- Add unit tests for `operations.py` functions.
- Move storage to a lightweight database (SQLite) or JSON.
- Improve input validation and error handling.
- Add logging and better invoice formatting.

## License & Academic Use

This project is a university coursework submission and is provided "as-is" for educational purposes. Do not use this code in production. If you reuse or adapt parts of this project, acknowledge the original author and follow your institution's rules regarding academic integrity.

---

If you want, I can also:

- Add a short `requirements.txt` or `pyproject.toml`.
- Create basic unit tests for `operations.py`.
- Generate a sample `medicines.txt` and a README usage screenshot.

Tell me which of these you'd like next.
