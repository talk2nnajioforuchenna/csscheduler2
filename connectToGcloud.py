import os
import json
from google.cloud import datastore
from google.oauth2 import service_account


def getData():
    credentials = service_account.Credentials.from_service_account_file('keys.json')
    datastore_client = datastore.Client(credentials=credentials)
    retValue = ''
    query = datastore_client.query(kind='EndUsers')
    for entity in query.fetch(limit=5):
        retValue += str(entity)
    return retValue

# print(getData())
