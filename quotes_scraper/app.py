from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = 'your mongodb uri'
DB_NAME = 'Quotes'
COLLECTION_NAME = 'quotedata'

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

@app.route('/quotes', methods=['POST'])
def receive_quotes():
    try:
        quotes = request.json

        result = collection.insert_many(quotes)

        if result:
            return 'Quotes received and saved to MongoDB successfully!', 200
        else:
            return 'Failed to save quotes to MongoDB', 500

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
