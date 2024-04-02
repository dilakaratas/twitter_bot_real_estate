import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json



cred = credentials.Certificate('/Users/dilakaratas/Desktop/twitter_database/keyAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


with open('/Users/dilakaratas/Desktop/twitter_database/istanbul_emlakjet_all_records_clean.json', 'r') as json_file:
    data = json.load(json_file)

    for record in data:

        db.collection('emlakjet_data_cleaned').add(record) 


