def process_custom_purchase_file(filename):
    total_items = 0
    free_items = 0
    amount_to_pay = 0
    discount_given = 0 
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue             
                parts = line.split()
                if not parts:
                    continue    
                item_name = parts[0]
                value_str = parts[-1]
                if item_name.lower() == 'discount' and value_str.isdigit():
                    discount_given = int(value_str)
                    continue 
                if value_str.lower() == 'free':
                    free_items += 1
                    total_items += 1
                    continue
                try:
                    price = float(value_str)
                    quantity = 1 
                    total_items += quantity
                    amount_to_pay += price * quantity
                except ValueError:
                    print(f"Warning: Skipping unrecognised line format in {filename}: {line}")
                    continue
        final_amount_paid = amount_to_pay - discount_given
        print(f"Sample output for {filename} file:")
        print(f"No of items purchased: {total_items}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {amount_to_pay:.2f}")
        print(f"Discount given: {discount_given:.2f}")
        print(f"Final amount paid: {final_amount_paid:.2f}")
        print(f"\n")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except IOError as e:
        print(f"An I/O error occurred while reading {filename}: {e}")
def create_custom_test_files():
    with open("purchase1.txt", "w") as f1:
        f1.write("Chocolate 50\n")
        f1.write("Biscuit 35\n")
        f1.write("Icecream 50\n")
        f1.write("\n") 
        f1.write("Discount 5\n")
    with open("purchase2.txt", "w") as f2:
        f2.write("Chocolate 50\n")
        f2.write("Biscuit 35\n")
        f2.write("Icecream 50\n")
        f2.write("Rice 100\n")
        f2.write("Chicken 250\n")
        f2.write("\n")
        f2.write("Perfume Free\n")
        f2.write("Soup Free\n")
        f2.write("\n")
        f2.write("Discount 80\n")
create_custom_test_files()
process_custom_purchase_file("purchase1.txt")
process_custom_purchase_file("purchase2.txt")