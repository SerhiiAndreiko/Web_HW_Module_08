import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host='localhost', port=27017, password=None)
cache: RedisLRU = RedisLRU(client)