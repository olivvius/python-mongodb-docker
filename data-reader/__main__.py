from datetime import datetime, timedelta
import pymongo
import time



client = pymongo.MongoClient("mongodb://mongodb:27017/")
db = client["mydatabase"]
collection = db["invoices"]
average_collection = db["average"]  # Création de la collection "average"

def calculate_average_price():
    total_price = 0
    count = 0
    for document in collection.find():
        total_price += document["price"]
        count += 1
    if count > 0:
        average_price = round(total_price / count, 2)
        #print(f"La moyenne des prix est : {average_price}")
         average_collection.insert_one({"average": average_price, "time": datetime.now()})
    else:
        print("Aucun document trouvé dans la collection")

def main():
    last_doc_count = collection.count_documents({})
    while True:
        current_doc_count = collection.count_documents({})
        if current_doc_count > last_doc_count:
            print("Nouveau document ajouté")
            calculate_average_price()
            last_doc_count = current_doc_count
        time.sleep(1)

if __name__ == '__main__':
    main()
