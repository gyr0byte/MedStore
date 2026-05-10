import operations as op
import read_file as rf
import write_file as wf


def main_menu():
    print("\nMedicine Store Inventory Management")
    print("1. Sale")
    print("2. Restock")
    print("3. View Stock")
    print("4. Exit")

    while True:
        choice = input("Enter your choice (1-4): ").strip()
        if choice in {"1", "2", "3", "4"}:
            return int(choice)
        print("Invalid choice. Please enter 1, 2, 3, or 4.")


def main():
    inventory = rf.load_inventory("medicines.txt")

    while True:
        choice = main_menu()

        if choice == 1:
            inventory = op.process_sale(inventory)
            wf.save_inventory("medicines.txt", inventory)
        elif choice == 2:
            inventory = op.process_restock(inventory)
            wf.save_inventory("medicines.txt", inventory)
        elif choice == 3:
            op.display_inventory(inventory)
        elif choice == 4:
            wf.save_inventory("medicines.txt", inventory)
            print("Goodbye")
            break


if __name__ == "__main__":
    main()
