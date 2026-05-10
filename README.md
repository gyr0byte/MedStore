# MedStore — CLI Medicine Store (University Coursework)

## Overview

MedStore is a minimal command-line interface (CLI) application for managing a small medicine inventory. It is university coursework, built for learning, and not a full-fledged or production-ready system. The app demonstrates simple inventory updates, basic pricing, and invoice generation using plain-text files.

## Important Notice

- Academic project: This repository is a student assignment for learning purposes only.
- Minimal scope: CLI prototype with limited validation, no authentication, and plain-text storage.

## Table of Contents

- Overview
- Features
- Quick Start
- How It Works
- Inventory File Format
- Pricing Rules
- Project Structure
- Limitations
- Testing
- Extending This Project
- License & Academic Use

## Features

- View current inventory
- Process a sale (decrease stock)
- Restock items (increase stock)
- Generate text invoices for sales and restocks
- Save inventory updates to a plain-text file

## Quick Start

PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python main.py
```

Command Prompt:

```cmd
python -m venv venv
venv\Scripts\activate
python main.py
```

Menu options:

- 1. Sale
- 2. Restock
- 3. View Stock
- 4. Exit

## How It Works

- Startup loads inventory from [medicines.txt](medicines.txt).
- Sale flow prompts for a customer, lets you select a medicine by index, choose `tablet` or `strip`, and updates stock.
- Restock flow prompts for a supplier, accepts new quantities and rates, and updates stock and prices.
- After each sale or restock, a text invoice is generated under [invoices/](invoices/).
- On exit, inventory is saved back to [medicines.txt](medicines.txt).

Entry point: [main.py](main.py) orchestrates the menu and calls into [operations.py](operations.py).

## Inventory File Format

Inventory is stored as CSV-like rows in [medicines.txt](medicines.txt) with six fields per line:

1. Name
2. Brand
3. Stock (tablets)
4. Rate per tablet
5. Rate per strip
6. Strip size (tablets per strip)

Example:

```csv
Paracetamol 500mg,Lomus,795,5.0,45.0,10
```

## Pricing Rules

- Sales compute totals using strip and tablet quantities.
- A 5% discount is applied when at least 2 strips are purchased for a medicine.
- Restock updates the rate for both `tablet` and `strip` units based on the input.

## Project Structure

- [main.py](main.py): CLI menu and control flow.
- [operations.py](operations.py): Sale, restock, pricing, and invoice logic.
- [read_file.py](read_file.py): Inventory loader.
- [write_file.py](write_file.py): Inventory and invoice writer.
- [medicines.txt](medicines.txt): Inventory data.
- [invoices/](invoices/): Generated sale/restock invoices.
- [docs/](docs/): Supplementary documentation artifacts.

## Limitations

- Not secure and not validated for real pharmacy use.
- Single-user and file-based; no concurrency safeguards.
- Minimal input validation and no automated tests.

## Testing

There are no automated tests included. For manual testing, run the app and verify that [medicines.txt](medicines.txt) and [invoices/](invoices/) update as expected after each action.

## Extending This Project

Potential improvements:

- Add unit tests for pricing and inventory updates.
- Migrate storage to SQLite or JSON.
- Add stronger validation and error handling.
- Improve invoice formatting and logging.

## License & Academic Use

This project is a university coursework submission and is provided "as-is" for educational purposes. Do not use this code in production. If you reuse or adapt parts of this project, acknowledge the original author and follow your institution's academic integrity rules.
