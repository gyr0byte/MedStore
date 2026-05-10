def load_inventory(filename):
    inventory = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                if not line.strip():  # Skip empty lines
                    continue
                parts = line.strip().split(',')
                if len(parts) != 6:  # validate that line has 6 comma separated fields
                    continue
                name, brand, quantity, rate_per_tablet, rate_per_strip, num_of_tablet_in_strip = parts
                try:
                    inventory.append({
                        'name': name.strip(),
                        'brand': brand.strip(),
                        'stock': int(quantity),
                        'rate_tablet': float(rate_per_tablet),
                        'rate_strip': float(rate_per_strip),
                        'strip_size': int(num_of_tablet_in_strip)
                    })
                except ValueError:
                    continue
    except FileNotFoundError:
        print("Inventory file not found. Starting with an empty inventory.")
    return inventory
