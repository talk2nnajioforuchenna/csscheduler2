from getRecords4mDatastore import records4mDatastoreToDB

def get_all_records():
    print('I have Started Pulling Records from DB')
    records4mDatastoreToDB()
    return "Welcome server is now working"


if __name__ == "__main__":
    get_all_records()
