import pymongo
import random
import string


def generate_data():
    # Connexion à la bdd MongoDB
    client = pymongo.MongoClient("mongodb://mongodb:27017/")
    db = client["mydatabase"]
    collection = db["customers"]

    # Génération de données randoms
    names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
    for i in range(10):
        name = random.choice(names)
        age = random.randint(18, 65)
        email = f"{name.lower()}_{i}@example.com"
        password = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        data = {"name": name, "age": age, "email": email, "password": password}
        collection.insert_one(data)

if __name__ == "__main__":
    generate_data()
