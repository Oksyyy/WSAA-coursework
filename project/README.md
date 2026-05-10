# Local Service Provider Finder
by Oksana Abrosimova

This is a Flask web application developed for the *Web Services and Applications* module.  
The project demonstrates creating and consuming a RESTful API using Flask, SQLite, AJAX and an HTML/CSS/JavaScript frontend.

The application allows users to manage local providers for services such as plumbing, carpentery, electrical and more.

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- jQuery
- PythonAnywhere for deployment

## Database Structure

The application uses two SQLite tables:

### services

| Field | Description |
|---|---|
| id | Primary key |
| name | Service name |

### providers

| Field | Description |
|---|---|
| id | Primary key |
| name | Provider name |
| email | Provider email |
| phone | Provider phone number |
| price_per_hour | Hourly rate |
| service_id | Foreign key linked to services table |

## API Endpoints

### Providers

| Method | Endpoint | Description |
|---|---|---|
| GET | `/providers` | Get all providers |
| GET | `/providers/<id>` | Get one provider by ID |
| POST | `/providers` | Create a new provider |
| PUT | `/providers/<id>` | Update a provider |
| DELETE | `/providers/<id>` | Delete a provider |
| GET | `/providers/service/<service_id>` | Get providers by service ID |

### Services

| Method | Endpoint | Description |
|---|---|---|
| GET | `/services` | Get all services |
| POST | `/services` | Create a new service |

## How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/Oksyyy/WSAA-coursework.git
cd WSAA-coursework/project
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create the database schema:
```bash
python3 createschema.py
```
4. Run the Flask server:
```bash
python3 server.py
```
5. Open the application in a browser:
```bash
http://127.0.0.1:5000/
```

## Deployment
The project has been deployed on PythonAnywhere.

Live application: https://oksy.pythonanywhere.com/

## References

Parts of the project development, debugging and troubleshooting were assisted using ChatGPT by OpenAI.

The frontend interface (HTML/CSS/JavaScript) was generated and iteratively refined using prompt-based assistance with ChatGPT.

Frontend generation prompt: [https://chatgpt.com/](https://chatgpt.com/c/69f45a26-2f0c-83eb-ab07-b149995df1f4).