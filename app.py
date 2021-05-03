from flask import Flask, request
from flask_cors import CORS
from analyse import Analyzer
import json

app = Flask(__name__)

# extension to stop Cross Origin Resource Sharing error for local server
CORS(app)

# sets root of server to recieve post requests
@app.route('/', methods=['POST'])
def post():
    a = Analyzer()
    data = json.loads(request.data)

    # prints each element recieved to the terminal and passes it to analyzer for
    # processing, returning a json dump of the processed object.
    for sentence in data['data']:
        print(sentence)
        data['data'][sentence] = a.local(sentence)
    return json.dumps(data)

# notification in case server recieves GET request
@app.route('/', methods=['GET'])
def get():
    return "Post your data to this endpoint for sentiment analysis!"