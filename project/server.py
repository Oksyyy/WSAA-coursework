# Flask server

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello world"

# PROVIDERS

# Get all
# curl http://127.0.0.1:5000/providers

@app.route('/providers', methods=['GET'])
def getall():
        return jsonify({"message": "get all"})

# Find by id
# curl http://127.0.0.1:5000/providers/1

@app.route('/providers/<int:id>', methods=['GET'])
def findbyid(id):
        return "find by id"

# Create
#curl -X POST -d "{\"name\":\"test\", \"email\":\"some@gmail.com\", \"phone\":\"01234567\", \"price\":70}" http://127.0.0.1:5000/providers
@app.route('/providers', methods=['POST'])
def create():
        return jsonify({"message": "create"})

# update
# curl -X PUT -d "{\"name\":\"test\", \"email\":\"some@gmail.com\", http://127.0.0.1:5000/providers/1

@app.route('/providers/<int:id>', methods=['PUT'])
def update(id):
        jsonstring = request.json
        return f"update {id} {jsonstring}"

# Delete
# curl -X DELETE  http://127.0.0.1:5000/providers/1

@app.route('/providers/<int:id>', methods=['DELETE'])
def delete(id):
        return f"delete {id}"

# SERVECES

# Get all
# curl http://127.0.0.1:5000/services

@app.route('/services', methods=['GET'])
def getall():
        return jsonify({"message": "get all"})

# Create
#curl -X POST -d "{\"name\":\"test\", \"email\":\"some@gmail.com\", \"phone\":\"01234567\", \"price\":70}" http://127.0.0.1:5000/providers
@app.route('/providers', methods=['POST'])
def create():
        return jsonify({"message": "create"})


if __name__ == "__main__":
    app.run(debug = True)