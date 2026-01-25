from flask import Flask
import redis
app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)


@app.route('/')
def hello_world():
    return 'CoderCo Containers Session!'

@app.route('/count')
def counter():
   new_count = r.incr('visit_count')
   return f'This page has been visited {new_count} times!'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)