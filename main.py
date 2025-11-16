# main.py
# KAYALAN AI - Mixed Reality Scrap Management System

from utils import calculate_price

def main():
    print("Welcome to KAYALAN AI - Mixed Reality Scrap Management System\n")

    # Sample scrap data
    scrap_items = {
        "Copper": 10,  # weight in kg
        "Aluminium": 5,
        "Plastic": 8
    }
    
    # Sample rates per kg
    rates = {
        "Copper": 500,
        "Aluminium": 200,
        "Plastic": 50
    }
    
    print("Scrap Items and Prices:\n")
    for item, weight in scrap_items.items():
        price = calculate_price(weight, rates[item])
        print(f"{item}: {weight} kg -> ₹{price}")

if __name__ == "__main__":
    main()


























