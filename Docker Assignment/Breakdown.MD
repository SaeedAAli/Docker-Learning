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

** 1) Flask Web Application: **
   *  This app contain two routes within the URL
          * /: Displays a welcome message.
       * /count: Increments and displays a visit count stored in Redis

** 2 Redis Database: **
    *  Use Redis as a key-value store to keep track of the visit count

** Dockerize Both Services
 * Create Dockerfiles for both the Flask app and Redis
 * Use Docker Compose to manage the multi container application

## Code to Combine both containers into one

Note: You have to use Docker-compose.yml in order to do this
```
docker compose up --build
```

## Results







