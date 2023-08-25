from flask import Flask
#from redis import Redis
from bprint import blueprint
app = Flask(__name__)
#redis = Redis(host='redis', port=6379)
app.register_blueprint(blueprint)

# @app.route('/')
# def hello():
#     redis.incr('hits')
#     x = redis.command_count()

#     counter = str(redis.get('hits'),'utf-8')
#     return "This webpage has been viewed "+counter+" time(s). Count returned "+ str(x)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
