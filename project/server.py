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
def get_providers():
        return jsonify({"message": "get all providers"})

# Find by id
# curl http://127.0.0.1:5000/providers/1

@app.route('/providers/<int:id>', methods=['GET'])
def provider_by_id(id):
        return "find provider by id"

# Create
#curl -X POST -d "{\"name\":\"test\", \"email\":\"some@gmail.com\", \"phone\":\"01234567\", \"price\":70}" http://127.0.0.1:5000/providers
@app.route('/providers', methods=['POST'])
def create_provider():
        return jsonify({"message": "create provider"})

# update
# curl -X PUT -d "{\"name\":\"test\", \"email\":\"some@gmail.com\", http://127.0.0.1:5000/providers/1

@app.route('/providers/<int:id>', methods=['PUT'])
def update_provider(id):
        jsonstring = request.json
        return f"update provider {id} {jsonstring}"

# Delete
# curl -X DELETE  http://127.0.0.1:5000/providers/1

@app.route('/providers/<int:id>', methods=['DELETE'])
def delete_provider(id):
        return f"delete provider {id}"

# SERVECES

# Get all services
# curl http://127.0.0.1:5000/services

@app.route('/services', methods=['GET'])
def get_services():
        return jsonify({"message": "get all services"})

# Create a service
#curl -X POST -d "{\"name\":\"test\", \"email\":\"some@gmail.com\", \"phone\":\"01234567\", \"price\":70}" http://127.0.0.1:5000/providers
@app.route('/services', methods=['POST'])
def create():
        return jsonify({"message": "create a service"})

# Get service and service providers
# curl http://127.0.0.1:5000//providers/service/1
@app.route('/providers/service/<int:service_id>', methods=['GET'])
def get_by_service(service_id):
    return jsonify({"message": f"providers for service {service_id}"})


if __name__ == "__main__":
    app.run(debug = True)