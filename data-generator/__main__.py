from time import sleep
import pymongo
import random
import string
from datetime import datetime, timedelta


def generate_data():
    # Connexion à la bdd MongoDB
    client = pymongo.MongoClient("mongodb://mongodb:27017/")
    db = client["mydatabase"]
    collection = db["invoices"]

    # Génération de données randoms
    customers = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
    products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
    payment_methods = ["Visa", "MasterCard", "American Express", "PayPal"]
    now = datetime.now()
    while(True):
        for i in range(1):
            customer = random.choice(customers)
            product = random.choice(products)
            quantity = random.randint(1, 10)
            price = random.randint(50, 2000) / 100  # montant entre 0,50 et 20,00
            total_amount = round(quantity * price, 2)
            payment_method = random.choice(payment_methods)
            payment_date = now - timedelta(days=random.randint(1, 30))
            data = {
                "customer": customer,
                "product": product,
                "quantity": quantity,
                "price": price,
                "total_amount": total_amount,
                "payment_method": payment_method,
                "payment_date": payment_date
            }
            collection.insert_one(data)
        sleep(3)


if __name__ == "__main__":
    generate_data()
