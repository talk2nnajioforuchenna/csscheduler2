import os
from flask import Flask
from getRecords4mDatastore import records4mDatastoreToDB


from runInBackground import runInBackground

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Welcome server is now working"


@app.route("/getallrecords")
def get_all_records():
    print('I have Started Pulling Records from DB')
    runInBackground(records4mDatastoreToDB)
    return "We are now getting records from Datastore and Sending it to FireStore"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
