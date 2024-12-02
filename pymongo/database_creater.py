from pymongo import MongoClient
import csv 


try:
    uri = "mongodb+srv://alsan632:ZH4SHl5cGhjtZ8gT@humanrights-cloud.4itum.mongodb.net/?retryWrites=true&w=majority&appName=humanrights-cloud"
    client = MongoClient(uri)
    db = client['humanrights_database']
    collection = db['committiee_against_torture']
    
    # with open('../data-sets/ohchr_cat_2022_2024.csv', 'r') as file :
    #     reader = csv.DictReader(file)
    #     for row in reader: 
    #         collection.insert_one(row)
            
    count = collection.count()
    print("You have", count , "documents")            
    client.close()

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
