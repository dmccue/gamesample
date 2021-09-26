import time, os, json
import redis, mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

# Functions
def getMySqlConnector():
    return mysql.connector.connect(
              user=os.environ['MYSQL_USER'],
              password=os.environ['MYSQL_PASSWORD'],
              host='mysql',
              database=os.environ['MYSQL_DATABASE']
    )

def getRedisConnection():
  return redis.Redis(host='redis', port=6379, password=os.environ['REDIS_AUTH'])

def sqlLookupPlayer(player_id, player_name):
  mysqlcon = getMySqlConnector()
  cursor = mysqlcon.cursor(buffered=True)
  if player_name:
    query = "SELECT * FROM " + os.environ['MYSQL_DATABASE'] + ".player WHERE player_name = '" + player_name + "';"
  elif player_id:
    query = "SELECT * FROM " + os.environ['MYSQL_DATABASE'] + ".player WHERE id = " + player_id + ";"
  else:
    return False
  cursor.execute(query)
  if cursor.rowcount < 1:
    return [] 
  return list(cursor.fetchone())

###################
# Player CREATE
###################
@app.route('/player/create', methods=['POST'])
def player_create():
  data = json.loads(request.data)

  # 1. store id and name in mysql
  lookupRow = sqlLookupPlayer(None, data['name'])
  if lookupRow:
    return jsonify("ERROR: record " + data['name'] + " already exists"), 500
  
  mysqlcon = getMySqlConnector()
  cursor = mysqlcon.cursor()
  query = "INSERT INTO " + os.environ['MYSQL_DATABASE'] + ".player(player_name, gold_amount) VALUES ('" + data['name'] + "', 0);"
  cursor.execute(query)
  mysqlcon.commit()
  cursor.close()


  # 2. store id and gold in redis
  cache = getRedisConnection()
  cache.mset({ lookupRow[0]: '0' })

  return {
    "player_create_id": str(lookupRow[0]),
    "player_create_name": str(lookupRow[1])
  }


###################
# Player GET
###################
@app.route('/player/get', methods=['POST'])
def player_get():
  data = json.loads(request.data)

  # 1. retrieve id and name from mysql
  lookupRow = None
  if 'id' in data.keys():
    lookupRow = sqlLookupPlayer(data['id'], None)
  elif 'name' in data.keys():
    lookupRow = sqlLookupPlayer(None, data['name'])
  if not lookupRow:
    return jsonify("ERROR: unable to find player"), 404

  # 2. retrieve gold from redis
  cache = getRedisConnection()
  if cache.exists( str(lookupRow[0]) ):
    goldcount = int(cache.get( lookupRow[0] ))
  else:
    goldcount = int(lookupRow[2])
    cache.mset({ lookupRow[0]: str(goldcount) })

  # 3. Sync redis and mysql
  if lookupRow[2] != goldcount:
    mysqlcon = getMySqlConnector()
    cursor = mysqlcon.cursor(buffered=True)
    query = "UPDATE " + os.environ['MYSQL_DATABASE'] + ".player SET gold_amount = " + str(goldcount) + " WHERE id = " + lookupRow[0] + ";"
    cursor.execute(query)
    lookupRow[2] = goldcount

  return str(lookupRow), 200

@app.route('/debug')
def debug_get():
  mysqlcon = getMySqlConnector()
  cursor = mysqlcon.cursor(buffered=True)
  query = "SELECT * FROM " + os.environ['MYSQL_DATABASE'] + ".player;"
  cursor.execute(query)
  if cursor.rowcount < 1:
    return [], 200
  return jsonify(cursor.fetchall()), 200




@app.route('/')
def hello():
  return 'Hello World!'
