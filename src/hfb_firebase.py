import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(r"./firestore.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection('restaurants')

def write(entry):
    data = {
        'name': entry[0],
        'cuisine': entry[1],
        'address': entry[2]
    }
    document = doc_ref.document(str(time.time()))
    document.set(data)

    print(f"Added {data['name']} as {document.id}")

def get_documents():
    ray = []
    docs = doc_ref.stream()
    for doc in docs:
        ray.append(doc.id)
    return ray

def get_restaurant(doc):
    restaurant = doc_ref.document(doc).get().to_dict()
    return restaurant
