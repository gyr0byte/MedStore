from datetime import datetime

import write_file as wf


def validate_positive_int(user_input):
    try:
        value = int(user_input)
        return value if value > 0 else None
    except ValueError:
        return None


def validate_positive_float(user_input):
    try:
        value = float(user_input)
        return value if value > 0 else None
    except ValueError:
        return None


def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def _safe_name_for_file(name):
    cleaned = "_".join(name.strip().split())
    return "".join(ch for ch in cleaned if ch.isalnum() or ch in "_-") or "unknown"


def _find_medicine(inventory, medicine_name):
    search_key = medicine_name.strip().lower()
    for medicine in inventory:
        if medicine["name"].strip().lower() == search_key:
            return medicine
    return None


def _select_medicine_by_index(inventory, prompt="Select medicine by index: "):
    while True:
        selection = validate_positive_int(input(prompt))
        if selection is None:
            print("Please enter a valid number.")
            continue
        index = selection - 1
        if 0 <= index < len(inventory):
            return inventory[index]
        print("Index out of range. Choose a number from the list.")


def _get_unit_type(prompt="Enter unit type (tablet/strip): "):
    while True:
        unit_type = input(prompt).strip().lower()
        if unit_type in {"tablet", "strip"}:
            return unit_type
        print("Invalid unit type. Please enter 'tablet' or 'strip'.")


def display_inventory(inventory, show_index=False):
    print("\nCurrent Inventory")
    print("=" * 80)
    if show_index:
        print("Index | Name | Brand | Stock(T) | Strips | Remain(T) | Rate/T | Rate/S | StripSize")
    else:
        print("Name | Brand | Stock(T) | Strips | Remain(T) | Rate/T | Rate/S | StripSize")
    print("-" * 80)

    for idx, med in enumerate(inventory, start=1):
        strips_available = med["stock"] // med["strip_size"]
        tablets_remaining = med["stock"] % med["strip_size"]
        row = (
            str(med["name"])
            + " | "
            + str(med["brand"])
            + " | "
            + str(med["stock"])
            + " | "
            + str(strips_available)
            + " | "
            + str(tablets_remaining)
            + " | "
            + str(round(med["rate_tablet"], 2))
            + " | "
            + str(round(med["rate_strip"], 2))
            + " | "
            + str(med["strip_size"])
        )
        if show_index:
            row = str(idx) + " | " + row
        print(row)


def calculate_price(medicine, quantity_tablets):
    strips = quantity_tablets // medicine["strip_size"]
    tablets = quantity_tablets % medicine["strip_size"]

    subtotal = (strips * medicine["rate_strip"]) + \
        (tablets * medicine["rate_tablet"])
    discount = subtotal * 0.05 if strips >= 2 else 0.0
    total = subtotal - discount

    return {
        "strips": strips,
        "tablets": tablets,
        "subtotal": subtotal,
        "discount": discount,
        "total": total,
    }


def generate_invoice_string(transaction_type, party_name, items_list, totals):
    timestamp = get_timestamp()
    invoice_no = f"INV-{timestamp}"

    lines = [
        "MedStore Pharmacy",
        f"Date: {timestamp}",
        f"Invoice #: {invoice_no}",
        f"{'Customer' if transaction_type == 'sale' else 'Supplier'}: {party_name}",
        "",
    ]

    if transaction_type == "sale":
        lines.append(
            "S.No | Medicine | Brand | Qty | Unit | Strips | Tablets | Discount | Amount")
        lines.append("-" * 90)
        for idx, item in enumerate(items_list, start=1):
            lines.append(
                str(idx)
                + " | "
                + str(item["name"])
                + " | "
                + str(item["brand"])
                + " | "
                + str(item["quantity"])
                + " | "
                + str(item["unit_type"])
                + " | "
                + str(item["strips_used"])
                + " | "
                + str(item["tablets_used"])
                + " | "
                + str(round(item["discount"], 2))
                + " | "
                + str(round(item["total"], 2))
            )
        lines.append("-" * 90)
        lines.append("Subtotal: " + str(round(totals["subtotal"], 2)))
        lines.append("Discount: " + str(round(totals["discount"], 2)))
        lines.append("Grand Total: " + str(round(totals["grand_total"], 2)))
    else:
        lines.append("S.No | Medicine | Brand | Qty | Unit | Rate | Amount")
        lines.append("-" * 70)
        for idx, item in enumerate(items_list, start=1):
            lines.append(
                str(idx)
                + " | "
                + str(item["name"])
                + " | "
                + str(item["brand"])
                + " | "
                + str(item["quantity"])
                + " | "
                + str(item["unit_type"])
                + " | "
                + str(round(item["rate"], 2))
                + " | "
                + str(round(item["total"], 2))
            )
        lines.append("-" * 70)
        lines.append("Total Amount: " + str(round(totals["total_amount"], 2)))

    return "\n".join(lines)


def process_sale(inventory):
    customer_name = input("Enter customer name: ").strip() or "Customer"
    cart = []

    while True:
        display_inventory(inventory, show_index=True)
        print("Tip: Use the index number to select a medicine quickly.")

        medicine = _select_medicine_by_index(
            inventory, "Enter medicine index: ")

        unit_type = _get_unit_type()

        quantity_input = None
        while quantity_input is None:
            quantity_input = validate_positive_int(
                input(f"Enter quantity in {unit_type}s: "))
            if quantity_input is None:
                print("Enter a valid positive integer quantity.")
                continue
            quantity_tablets = quantity_input if unit_type == "tablet" else quantity_input * \
                medicine["strip_size"]
            if quantity_tablets > medicine["stock"]:
                print(
                    f"Insufficient stock. Available tablets: {medicine['stock']}")
                quantity_input = None

        quantity_tablets = quantity_input if unit_type == "tablet" else quantity_input * \
            medicine["strip_size"]
        pricing = calculate_price(medicine, quantity_tablets)
        cart.append(
            {
                "name": medicine["name"],
                "brand": medicine["brand"],
                "quantity": quantity_input,
                "unit_type": unit_type,
                "strips_used": pricing["strips"],
                "tablets_used": pricing["tablets"],
                "subtotal": pricing["subtotal"],
                "discount": pricing["discount"],
                "total": pricing["total"],
            }
        )

        medicine["stock"] -= quantity_tablets

        while True:
            add_more = input("Add more? (y/n): ").strip().lower()
            if add_more in {"y", "n"}:
                break
            print("Please enter 'y' or 'n'.")
        if add_more == "n":
            break

    if not cart:
        print("No sale items added.")
        return inventory

    subtotal = sum(item["subtotal"] for item in cart)
    discount = sum(item["discount"] for item in cart)
    grand_total = sum(item["total"] for item in cart)

    totals = {
        "subtotal": subtotal,
        "discount": discount,
        "grand_total": grand_total,
    }
    invoice = generate_invoice_string("sale", customer_name, cart, totals)
    print("\n" + invoice)

    filename = f"invoices/sale_{get_timestamp()}_{_safe_name_for_file(customer_name)}.txt"
    wf.save_invoice(filename, invoice)

    return inventory


def process_restock(inventory):
    supplier_name = input("Enter supplier name: ").strip() or "Supplier"
    restock_list = []

    while True:
        display_inventory(inventory, show_index=True)
        print("Tip: Use the index number to select a medicine quickly.")

        medicine = _select_medicine_by_index(
            inventory, "Enter medicine index for restock: ")

        unit_type = _get_unit_type("Enter restock unit type (tablet/strip): ")

        quantity_input = None
        while quantity_input is None:
            quantity_input = validate_positive_int(
                input(f"Enter restock quantity in {unit_type}s: "))
            if quantity_input is None:
                print("Enter a valid positive integer quantity.")

        rate = None
        while rate is None:
            current_rate = medicine["rate_tablet"] if unit_type == "tablet" else medicine["rate_strip"]
            prompt = f"Enter rate per {unit_type} (current {current_rate:.2f}): "
            rate = validate_positive_float(input(prompt))
            if rate is None:
                print("Enter a valid positive rate.")

        total = quantity_input * rate
        quantity_tablets = quantity_input if unit_type == "tablet" else quantity_input * \
            medicine["strip_size"]
        restock_list.append(
            {
                "name": medicine["name"],
                "brand": medicine["brand"],
                "quantity": quantity_input,
                "unit_type": unit_type,
                "rate": rate,
                "total": total,
            }
        )

        medicine["stock"] += quantity_tablets
        if unit_type == "tablet":
            medicine["rate_tablet"] = rate
            medicine["rate_strip"] = rate * medicine["strip_size"]
        else:
            medicine["rate_strip"] = rate
            medicine["rate_tablet"] = rate / medicine["strip_size"]

        while True:
            add_more = input("Add more? (y/n): ").strip().lower()
            if add_more in {"y", "n"}:
                break
            print("Please enter 'y' or 'n'.")
        if add_more == "n":
            break

    if not restock_list:
        print("No restock items added.")
        return inventory

    totals = {"total_amount": sum(item["total"] for item in restock_list)}
    invoice = generate_invoice_string(
        "restock", supplier_name, restock_list, totals)
    print("\n" + invoice)

    filename = f"invoices/restock_{get_timestamp()}_{_safe_name_for_file(supplier_name)}.txt"
    wf.save_invoice(filename, invoice)

    return inventory
