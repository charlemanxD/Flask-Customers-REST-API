"""Importing flask, requests and jsonify modules."""
from flask import Flask, request, jsonify

# Creating an instance of flask from its module
app = Flask(__name__)

# Python List of customers
customers = [
    {
        "id": 1, 
        "firstname": "John",
        "lastname": "Doe", 
        "gender": "m", 
        "country": "Australia"
        },

    {
        "id": 2, 
        "firstname": "Suzane", 
        "lastname": "Hitch", 
        "gender": "f", 
        "country": "United States"
        },

    {
        "id": 3, 
        "firstname": 
        "François", 
        "lastname": 
        "Lemaire", 
        "gender": "m", 
        "country": "France"
        },
]

def _find_next_id():
    """Function generate an ID for the next customer to be added."""
    return max(customer["id"] for customer in customers) + 1

@app.get("/")
def homepage():
    """Function returns the main page."""
    return "Flask app is running"

@app.get("/customers")
def get_countries():
    """Function list all countries."""
    return jsonify(customers)

@app.post("/customers")
def add_country():
    """Function add a new country to the list."""
    if request.is_json: # check if the request is in JSON format
        customer = request.get_json()
        customer["id"] = _find_next_id()
        customers.append(customer)
        return customer, 201
    return {"error": "Request must be JSON"}, 415
