# Docker Learning

In this repistory, it contains hands on experience which consists of being able to create a multi-container application which include a simple Python Flask web application and a Redis Database.  The Flask application should use Redis to store and retrieve data whenever the User enters and refreshes the page.


## File In Order
`````
├── Dockerfile
├── count.py
├── docker-compose.yaml
├── nginx.conf
└── venv
`````

## Requirements for this Assignment

The Flask app has two routes

1 |Flask Web Application | 
| ------------- |:-------------:|
| / : Dispplays a welcome message
| /count : Increment and displays a visit count stored in Redis
