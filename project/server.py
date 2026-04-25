# Flask server

from flask import Flask, request, jsonify
from pa import ServiceProviderDAO

app = Flask(__name__)

@app.route('/')
def index():
        return jsonify({"message": "Service Provider API running"})

# PROVIDERS

# Get all
# curl http://127.0.0.1:5000/providers

@app.route('/providers', methods=['GET'])
def get_providers():
        return jsonify(ServiceProviderDAO.get_all())

# Find by id
# curl http://127.0.0.1:5000/providers/2

@app.route('/providers/<int:id>', methods=['GET'])
def provider_by_id(id):
        provider = ServiceProviderDAO.find_by_id(id)
        if provider is None:
                return jsonify({"error": "Provider not found"}), 404

        return jsonify(provider)

# Create
# curl -X POST http://127.0.0.1:5000/providers \-H "Content-Type: application/json" \-d '{"name":"Elaine","email":"elaine_mn@tgmail.com","phone":"086","price_per_hour":47,"service_id":2}'
@app.route('/providers', methods=['POST'])
def create_provider():
        return jsonify(ServiceProviderDAO.create_provider(request.json))

# Update
# curl -X PUT http://127.0.0.1:5000/providers/2 \-H "Content-Type: application/json" \-d '{"name":"Jack","email":"some_jack@gmail.com","phone":"123","price_per_hour":61,"service_id":1}'

@app.route('/providers/<int:id>', methods=['PUT'])
def update_provider(id):
        jsonstring = request.json
        existing_provider = ServiceProviderDAO.find_by_id(id)
        if existing_provider is None:
                return jsonify({"error": "Provider not found"}), 404

        ServiceProviderDAO.update_provider(id, jsonstring)
        return jsonify({"message": "updated"})

# Delete
# curl -X DELETE http://127.0.0.1:5000/providers/1

@app.route('/providers/<int:id>', methods=['DELETE'])
def delete_provider(id):
        existing = ServiceProviderDAO.find_by_id(id)
        if existing is None:
                return jsonify({"error": "Provider not found"}), 404

        ServiceProviderDAO.delete_provider(id)
        return jsonify({"message": "deleted"})

# SERVICES

# Get all services
# curl http://127.0.0.1:5000/services

@app.route('/services', methods=['GET'])
def get_services():
        return jsonify(ServiceProviderDAO.get_all_services())

# Create a service
# curl -X POST http://127.0.0.1:5000/services \-H "Content-Type: application/json" \-d '{"name":"Painting","service_id":2}'
@app.route('/services', methods=['POST'])
def create_service():
        return jsonify(ServiceProviderDAO.create_service(request.json))

# Get service and service providers
# curl http://127.0.0.1:5000/providers/service/1
@app.route('/providers/service/<int:service_id>', methods=['GET'])
def get_by_service(service_id):
    return jsonify(ServiceProviderDAO.get_by_service(service_id))


if __name__ == "__main__":
    app.run(debug = True)