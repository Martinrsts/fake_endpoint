import json
import random

def create_json():
    rental_price_clp = 1000000
    purchase_price_clp = 50000000
    rental_price_uf = int(rental_price_clp / 30000) # Assuming 1 UF = 30,000 CLP
    purchase_price_uf = int(purchase_price_clp / 30000) # Assuming 1 UF = 30,000 CLP

    rental_prices_clp = []
    purchase_prices_clp = []
    rental_prices_uf = []
    purchase_prices_uf = []

    for i in range(100): # Assuming 5 values for simplicity
        x = int(random.normalvariate(100000, 5000 * (i%10))) # Mean: 100,000, Standard Deviation: 20,000 * (i+1)
        rental_prices_clp.append({"x": x})
        purchase_prices_clp.append({"x": x})
        rental_prices_uf.append({"x": int(x / 30000)}) # Assuming 1 UF = 30,000 CLP
        purchase_prices_uf.append({"x": int(x / 30000)}) # Assuming 1 UF = 30,000 CLP

    data = {
        "rental_price_clp": rental_price_clp,
        "purchase_price_clp": purchase_price_clp,
        "rental_price_uf": rental_price_uf,
        "purchase_price_uf": purchase_price_uf,
        "rental_prices_clp": rental_prices_clp,
        "purchase_prices_clp": purchase_prices_clp,
        "rental_prices_uf": rental_prices_uf,
        "purchase_prices_uf": purchase_prices_uf
    }

    with open("db.json", "w") as file:
        json.dump(data, file)

    print("JSON file created successfully.")

create_json()
