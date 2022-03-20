from google.cloud import datastore
from google.oauth2 import service_account
import asyncio

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import json
from datetime import datetime

# Connecting to Firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'projectId': "customerservicescheduler"
})
db = firestore.client()

# Connecting to Datastore
credentials = service_account.Credentials.from_service_account_file('keys.json')
client = datastore.Client(credentials=credentials)
counter = 1


def records4mDatastoreToDB():
    global db
    global client

    def processRecords(records):
        global counter
        for record in records:
            query1 = client.query(kind='OrderDetails', ancestor=record.key)
            recordDict = dict(record)
            recordDict['details'] = []
            for order in query1.fetch():
                order = dict(order)
                recordDict['details'].append(order)
            # print(recordDict)

            try:
                refKey = str(recordDict['phoneNumber'][0])
            except:
                refKey = '0000000000'
            try:
                uniqueOrder = str(recordDict['orderDate'])
            except:
                uniqueOrder = '2022-03-16'

            ref = db.collection('Orders').document(refKey)
            ref.set({uniqueOrder: recordDict}, merge=True)
            print(counter)
            print(uniqueOrder)
            counter += 1
            print('')

    cursor = None
    query = client.query(kind='OrderRecords')
    query_iter = query.fetch(start_cursor=cursor, limit=200)
    page = next(query_iter.pages)
    next_cursor = query_iter.next_page_token
    processRecords(list(page))

    while next_cursor is not None:
        cursor = next_cursor
        query_iter = query.fetch(start_cursor=cursor, limit=200)
        page = next(query_iter.pages)
        next_cursor = query_iter.next_page_token
        print(next_cursor)
        processRecords(list(page))



