# Flask Customers REST API

`REST` is a software architecture style that defines a pattern  for client and server communication over a network.

REST APIs are essential for modern  web and mobile applications to scale and remain flexible.

This is a simple customer API that has an endpoint */customers* and handles two types of requests: 
1. `GET` /customers (returns a list of customers) 
2. `POST` /customers  (creates a new customer).

Let's start:

`Step 1:` In the terminal, we create the project directory
```bash
mkdir flask-customers-api
```
	
`Step 2:` In the project folder, create and activate  your virtual environment
```bash
	python -m venv venv
```

Virtual environment activation (Windows)
```bash
	source venv/Script/activate
```

`Step 3:` Install Flask module
```bash
pip install flask
```

`Step 4:` In our project directory, we create the `app.py` application file that will hold our API code.

`Step 5:` I tried to run the `Flask application` by setting an environment variable called `FLASK_APP` to `app.py` in my current shell. This tells Flask which file contains my application.
```bash
export FLASK_APP=app.py
```

I set `FLASK_ENV` to `development`, which puts Flask in **debug mode** to provide helpful error messages.
```bash
export FLASK_ENV=development
```

With all the environment variables set, I started the Flask development server by calling `flask run`
```bash
flask run
```

However, the above commands did not work as expected, as the debug mode was not responding (I haven't figured out why).

Without environment variables, I tried the following command.
```bash
flask run --debug
```
The above command ran the app in debug mode.

## Errors encountered (And solutions)

**Error:**

![Screenshot 2025-05-04 225305](https://github.com/user-attachments/assets/e7699b65-0f5e-4da8-a753-914ce04d616b)


**reason:**  I did not set up a route to / 

**Solution:**  I created a view function route to /

**Output**

![Screenshot 2025-05-16 234538](https://github.com/user-attachments/assets/e15eaa0b-a729-4201-8137-fdfd9dd26e8b)


**Error:**

![Screenshot 2025-05-17 175243-1](https://github.com/user-attachments/assets/525e8dbb-fb3d-4068-92d1-57d9fa41e13c)


**Reason**: The server was not running when adding new data

**Solution:** 
I run the app in one terminal, in another instance of the same terminal, I added the data.  Et voila! It worked.

**Output**

![Screenshot 2025-05-17 180356-1](https://github.com/user-attachments/assets/15ddf609-d9fd-4229-b43d-b00dbfb74ca2)


### What I learned

-  REST API
- Troubleshooting
- Project documentation

### Conclusion 

This project broadened my understanding of APIs. 

This API `does not have a database`, so any data added is not retained after the server shuts down.

The next step would be to add a database.

