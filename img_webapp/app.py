import time, os
import redis, mysql.connector
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379, password=os.environ['REDIS_AUTH'])

mysqlcon = mysql.connector.connect(
          user=os.environ['MYSQL_USER'],
          password=os.environ['MYSQL_PASSWORD'],
          host='mysql',
          database=os.environ['MYSQL_DATABASE']
)
#mysqlcon.close()


def get_hit_count():
  retries = 5
  while True:
    try:
      return cache.incr('hits')
    except redis.exceptions.ConnectionError as exc:
      if retries == 0:
        raise exc
      retries -= 1
      time.sleep(0.5)

@app.route('/')
def hello():
  count = get_hit_count()
  return 'Hello World! I have been seen {} times.\n'.format(count)
