import time, os, json
import redis, mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)


def getMySqlConnector():
    return mysql.connector.connect(
              user=os.environ['MYSQL_USER'],
              password=os.environ['MYSQL_PASSWORD'],
              host='mysql',
              database=os.environ['MYSQL_DATABASE']
    )

def getRedisConnection():
  return redis.Redis(host='redis', port=6379, password=os.environ['REDIS_AUTH'])

###################
# Player CREATE
###################
@app.route('/player/create', methods=['POST'])
def player_create():
  data = json.loads(request.data)

  # 1. store id and name in mysql
  mysqlcon = getMySqlConnector()
  try:
    cursor = mysqlcon.cursor()
    query = "INSERT INTO " + os.environ['MYSQL_DATABASE'] + ".player(identifier, player_name) VALUES (" + data['id'] + ",'" + data['name'] + "');"
    cursor.execute(query)
    mysqlcon.commit()
    cursor.close()
  except mysql.connector.Error as error:
    return jsonify("ERROR: record " + data['name'] + "-" + data['id'] + " already exists"), 500

  # 2. store id and gold in redis
  cache = getRedisConnection()
  cache.mset({ str(data['id']): '0' })

  return {
    "player_create_id": str(data['id']),
    "player_create_name": str(data['name'])
  }


###################
# Player GET
###################
@app.route('/player/get', methods=['POST'])
def player_get():
  data = json.loads(request.data)

  # 1. retrieve id and name from mysql
  mysqlcon = getMySqlConnector()
  cursor = mysqlcon.cursor(buffered=True)
  query = "SELECT * FROM " + os.environ['MYSQL_DATABASE'] + ".player WHERE identifier = " + str(data['id']) + " AND player_name = '" + data['name'] + "'"
  cursor.execute(query)
  if cursor.rowcount < 1:
    return jsonify("ERROR: unable to find name and id: " + data['name'] + " " + str(data['id'])), 404

  # 2. retrieve gold from redis
  cache = getRedisConnection()
  goldcount = cache.get( str(data['id']) )

  data['gold'] = int(goldcount)

  cursor.close()
  mysqlcon.close()

  return str(data), 200


@app.route('/')
def hello():
  return 'Hello World!'
