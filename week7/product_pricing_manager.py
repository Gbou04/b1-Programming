import logging

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_category_discount(category):
    if category == "Electronics":
        return 10
    elif category == "Clothing":
        return 15
    elif category == "Books":
        return 5
    elif category == "Home":
        return 12
    else:
        return 0

def get_tier_discount(tier):
    if tier == "Premium":
        return 5
    elif tier == "Standard":
        return 0
    elif tier == "Budget":
        return 2
    else:
        return 0

# Read product data, calculate final prices, generate pricing report, handle errors
def process_products(input_file, output_file):
    try:
        products = []
        total_discount = 0.0

        # READ PRODUCT DATA INPUT
        with open(input_file, "r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, 1):
                try:
                    parts = line.strip().split(",")
                    if len(parts) != 4:
                        logging.warning(f"Line {line_number}: Invalid format, skipping.")
                        continue

                    name, price_string, category, tier = parts
                    base_price = float(price_string)

                    category_discount = get_category_discount(category)
                    tier_discount = get_tier_discount(tier)
                    discount_total = category_discount + tier_discount

                    discount_amount = base_price * (discount_total / 100)
                    final_price = base_price - discount_amount

                    products.append({
                        "name": name,
                        "base_price": base_price,
                        "discount_total": discount_total,
                        "discount_amount": discount_amount,
                        "final_price": final_price,
                    })

                    total_discount += discount_total

                except ValueError as e:
                    logging.error(f"Line {line_number}: Invalid price format - {e}")
                    continue

        # PRICING REPORT
        with open(output_file, "w", encoding="utf-8") as f:
            width = 90
            f.write("=" * width + "\n")
            f.write("PRICING REPORT\n")
            f.write("=" * width + "\n")
            f.write(
                f"{'Product Name':<30} {'Base Price':>12} {'Discount %':>12} "
                f"{'Discount $':>12} {'Final Price':>12}\n"
            )
            f.write("-" * width + "\n")

            # WRITE PRODUCT DATA OUTPUT
            for product in products:
                f.write(
                    f"{product['name']:<30} "
                    f"${product['base_price']:>11.2f} "
                    f"{product['discount_total']:>11.1f}% "
                    f"${product['discount_amount']:>11.2f} "
                    f"${product['final_price']:>11.2f}\n"
                )

            f.write("=" * width + "\n")

        # Print a summary
        avg_discount = total_discount / len(products) if products else 0.0
        print("\nProcessing Complete!")
        print(f"Total Products Processed: {len(products)}")
        print(f"Average Discount Applied: {avg_discount:.2f}%")
        print(f"Report Saved To: {output_file}")
        logging.info(f"Successfully processed {len(products)} products.")

    except FileNotFoundError:
        logging.error(f"Input file '{input_file}' not found")
        print(f"Error: Could not find input file: '{input_file}'")

    except PermissionError:
        logging.error(f"Permission denied writing to '{output_file}'")
        print(f"Error: Could not write to '{output_file}'")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    process_products("products.txt", "pricing_report.txt")