def save_inventory(filename, inventory):
    with open(filename, 'w') as file:
        for item in inventory:
            file.write(
                f"{item['name']},{item['brand']},{item['stock']},{item['rate_tablet']},{item['rate_strip']},{item['strip_size']}\n")


def save_invoice(filename, content_string):
    with open(filename, 'w') as file:
        file.write(content_string)
