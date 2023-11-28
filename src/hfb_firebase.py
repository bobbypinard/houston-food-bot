import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(r"./firestore.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def write(entry):
    data = {
        'name': entry[0],
        'cuisine': entry[1],
        'address': entry[2]
    }

    doc_ref = db.collection('restaurants').document()
    doc_ref.set(data)

    print(f"Added {data['name']} as {doc_ref.id}")