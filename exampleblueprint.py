from flask import Blueprint
from redis import Redis
example_blueprint = Blueprint('example_blueprint', __name__)
portnum = 6379
redis = Redis(host='redis', port=portnum)
@example_blueprint.route('/')
def index():
    redis.incr('hits')
    x = redis.command_count()

    counter = str(redis.get('hits'),'utf-8')
    return "This webpage has been viewed "+counter+" time(s). Count returned "+ str(x)
    #return "This is an example app"
